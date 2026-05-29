#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCS_DIR="$ROOT_DIR/docs"
OBSERVE_DOCS_DIR="$DOCS_DIR/observations"
REFLECT_DOCS_DIR="$DOCS_DIR/reflections"
CSS_PATH="assets/site.css"
SCRIPT_INCLUDE_PATH="assets/site-after-body.html"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "error: pandoc is required to publish docs" >&2
  exit 1
fi

mkdir -p "$OBSERVE_DOCS_DIR" "$REFLECT_DOCS_DIR"

shopt -s nullglob
OBSERVE_SOURCES=("$ROOT_DIR"/observe/*.md)
REFLECT_SOURCES=("$ROOT_DIR"/reflect/*.md)
shopt -u nullglob

eligible_sources() {
  local source
  for source in "$@"; do
    if [[ "$(basename "$source")" != "README.md" ]]; then
      printf '%s\n' "$source"
    fi
  done
}

title_from_stem() {
  local stem="$1"
  local words=()
  local word

  stem="${stem//_/ }"
  stem="${stem//-/ }"
  read -r -a words <<< "$stem"

  for word in "${words[@]}"; do
    printf '%s%s ' "${word:0:1}" "${word:1}"
  done | sed 's/[[:space:]]$//'
}

publish_sources() {
  local target_dir="$1"
  shift

  local source stem title output
  for source in "$@"; do
    stem="$(basename "$source" .md)"
    title="$(title_from_stem "$stem")"
    output="$target_dir/$stem.html"

    pandoc "$source" \
      --standalone \
      --css "../$CSS_PATH" \
      --include-after-body "$DOCS_DIR/$SCRIPT_INCLUDE_PATH" \
      --metadata "title=$title" \
      -o "$output"
  done
}

append_links() {
  local category_dir="$1"
  shift
  local heading

  heading="$(title_from_stem "$category_dir")"
  {
    printf '## %s\n\n' "$heading"
    if (($# == 0)); then
      printf '_No %s published._\n\n' "$category_dir"
      return
    fi

    local source stem output
    for source in "$@"; do
      stem="$(basename "$source" .md)"
      output="$stem.html"
      printf -- '- [%s](./%s/%s)\n' "$output" "$category_dir" "$output"
    done
    printf '\n'
  } >> "$DOCS_DIR/index.md"
}

mapfile -t OBSERVE_PUBLISH < <(eligible_sources "${OBSERVE_SOURCES[@]}" | sort)
mapfile -t REFLECT_PUBLISH < <(eligible_sources "${REFLECT_SOURCES[@]}" | sort)

publish_sources "$OBSERVE_DOCS_DIR" "${OBSERVE_PUBLISH[@]}"
publish_sources "$REFLECT_DOCS_DIR" "${REFLECT_PUBLISH[@]}"

{
  printf -- '---\n'
  printf 'layout: default\n'
  printf 'title: UDT Platforms Map\n'
  printf -- '---\n\n'
  printf '# Urban Digital Twin Platforms Map\n\n'
} > "$DOCS_DIR/index.md"

append_links "observations" "${OBSERVE_PUBLISH[@]}"
append_links "reflections" "${REFLECT_PUBLISH[@]}"

pandoc "$DOCS_DIR/index.md" \
  --standalone \
  --css "$CSS_PATH" \
  --metadata title="UDT Platforms Map" \
  -o "$DOCS_DIR/index.html"

echo "Published ${#OBSERVE_PUBLISH[@]} observation page(s) and ${#REFLECT_PUBLISH[@]} reflection page(s)."
