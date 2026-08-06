#!/usr/bin/env bash
# 삽화 배치 생성 — codex exec 의 image_generation 을 5개씩 병렬로 실행하고 결과를 검수한다.
#
# 사용법:
#   gen_illustrations.sh <work_dir> "<프롬프트>::<출력파일명>.png" ...
#   gen_illustrations.sh <work_dir> --from-file <specs.txt>     ← 권장
#
# --from-file 은 한 줄에 "<프롬프트>::<출력>.png" 하나씩 담은 파일을 읽는다.
# 프롬프트가 1000자를 넘는 것이 보통이라 호출 측에서 배열로 넘기려다 사고가 난다:
#   - `mapfile` 은 bash 전용이다. macOS 기본 셸(zsh)에서는 인자가 0건이 된다
#   - `while read` 는 마지막 줄에 개행이 없으면 그 줄을 버린다 (`|| [ -n "$line" ]` 필요)
# 둘 다 조용히 실패해 "생성 0건"으로 끝나므로, 파일 경로만 넘기는 쪽이 안전하다.
#
# 동작:
#   - 5개씩 묶어 배치 실행. 한 배치가 끝나면 다음 배치 시작 (6개 이상 동시는 큐잉으로 분산이 커진다)
#   - 각 작업은 독립 codex 세션이므로 진짜 병렬
#   - 배치 종료 후 모든 PNG 를 검수하고 요약을 출력
#   - codex 최종 메시지는 <work_dir>/.codex-logs/ 에 보관
#
# 종료 코드: 0 = 전체 성공, 1 = 사용법 오류/사전점검 실패, 2 = 일부 이미지 실패

set -u -o pipefail

BATCH_SIZE=5

if [ "$#" -lt 2 ]; then
  echo "usage: $0 <work_dir> \"<prompt>::<output>.png\" [more...]" >&2
  exit 1
fi

WORK_DIR="$1"; shift

# --from-file <path> : 한 줄에 하나씩 담긴 스펙을 읽어 위치 인자로 대체한다.
# 마지막 줄에 개행이 없어도 버리지 않도록 `|| [ -n "$line" ]` 를 둔다.
if [ "${1:-}" = "--from-file" ]; then
  spec_file="${2:-}"
  [ -f "$spec_file" ] || { echo "spec file not found: $spec_file" >&2; exit 1; }
  set --
  while IFS= read -r line || [ -n "$line" ]; do
    case "$line" in
      ''|'#'*) continue ;;
    esac
    set -- "$@" "$line"
  done < "$spec_file"
  [ "$#" -gt 0 ] || { echo "no specs read from $spec_file" >&2; exit 1; }
  echo "==> loaded $# spec(s) from $spec_file"
fi

LOG_DIR="$WORK_DIR/.codex-logs"
mkdir -p "$WORK_DIR" "$LOG_DIR" || { echo "cannot create $WORK_DIR" >&2; exit 1; }

# --- 사전 점검 -----------------------------------------------------------
# 미인증 상태로 N개를 띄우면 N개가 모두 실패하므로 먼저 확인한다.
command -v codex >/dev/null 2>&1 || { echo "codex CLI not found in PATH" >&2; exit 1; }
if ! codex login status >/dev/null 2>&1; then
  echo "codex is not logged in. run: codex login" >&2
  exit 1
fi

# --- 입력 파싱 -----------------------------------------------------------
PROMPTS=()
OUTPUTS=()
for spec in "$@"; do
  case "$spec" in
    *"::"*) : ;;
    *) echo "bad spec (missing '::'): $spec" >&2; exit 1 ;;
  esac
  PROMPTS+=( "${spec%::*}" )
  OUTPUTS+=( "${spec##*::}" )
done

TOTAL="${#OUTPUTS[@]}"

# 출력 파일명 중복은 마지막 작업만 살아남게 만든다 — 생성 전에 막는다.
dupes="$(printf '%s\n' "${OUTPUTS[@]}" | sort | uniq -d)"
if [ -n "$dupes" ]; then
  echo "duplicate output filenames would overwrite each other:" >&2
  echo "$dupes" >&2
  exit 1
fi

echo "==> generating $TOTAL illustration(s) into $WORK_DIR (batch size $BATCH_SIZE)"

# --- 배치 실행 -----------------------------------------------------------
i=0
while [ "$i" -lt "$TOTAL" ]; do
  pids=()
  batch_end=$(( i + BATCH_SIZE ))
  [ "$batch_end" -gt "$TOTAL" ] && batch_end="$TOTAL"
  echo "--> batch $(( i / BATCH_SIZE + 1 )): items $(( i + 1 ))..$batch_end"

  j="$i"
  while [ "$j" -lt "$batch_end" ]; do
    out="${OUTPUTS[$j]}"
    prompt="${PROMPTS[$j]}"
    log="$LOG_DIR/${out%.png}.md"

    # --ask-for-approval 은 codex exec 에서 에러다. --skip-git-repo-check 없으면 워크스페이스 검증에서 멈춘다.
    codex exec \
      --sandbox workspace-write \
      --skip-git-repo-check \
      --cd "$WORK_DIR" \
      -o "$log" \
      "이미지 생성 도구로 다음 이미지를 생성하고 ./${out} 로 저장하라. 저장한 파일 경로만 한 줄로 보고하라. 프롬프트: ${prompt}" \
      >"$LOG_DIR/${out%.png}.stdout" 2>&1 &
    pids+=( "$!" )
    j=$(( j + 1 ))
  done

  for pid in "${pids[@]}"; do
    wait "$pid" || true   # 개별 실패는 아래 검수 단계에서 파일 기준으로 판정한다
  done

  i="$batch_end"
done

# --- 검수 ---------------------------------------------------------------
# codex 가 성공 메시지를 내고도 0바이트 파일을 남기는 경우가 있어 파일 기준으로 확인한다.
echo "==> verifying"
ok=0
fail=0
for out in "${OUTPUTS[@]}"; do
  path="$WORK_DIR/$out"

  # codex 가 작업 폴더로 복사하지 않고 자체 디렉토리에만 남긴 경우를 구제한다.
  if [ ! -s "$path" ]; then
    found="$(find "$HOME/.codex/generated_images" -name "$out" -type f 2>/dev/null | head -1)"
    if [ -n "$found" ]; then
      cp "$found" "$path" 2>/dev/null && echo "    recovered from ~/.codex/generated_images: $out"
    fi
  fi

  if [ ! -e "$path" ]; then
    echo "  FAIL  $out — file not created"
    fail=$(( fail + 1 )); continue
  fi
  if [ ! -s "$path" ]; then
    echo "  FAIL  $out — zero bytes"
    fail=$(( fail + 1 )); continue
  fi
  desc="$(file -b "$path" 2>/dev/null)"
  case "$desc" in
    PNG\ image\ data*)
      bytes="$(wc -c <"$path" | tr -d ' ')"
      echo "  ok    $out — $bytes bytes — $desc"
      ok=$(( ok + 1 ))
      ;;
    *)
      echo "  FAIL  $out — not a valid PNG ($desc)"
      fail=$(( fail + 1 ))
      ;;
  esac
done

echo "==> done: $ok ok, $fail failed (of $TOTAL)"
echo "    logs: $LOG_DIR"
if [ "$fail" -gt 0 ]; then
  echo "    failed items: check the log above for the codex message. Do not retry more than once —"
  echo "    repeated failure usually means the prompt itself is the problem (e.g. it asks for Korean text)."
  exit 2
fi
exit 0
