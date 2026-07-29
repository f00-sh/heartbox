#!/usr/bin/env sh
# Heartbox install helper — man page + theme location hint
set -eu

REPO="${HEARTBOX_REPO:-f00-sh/heartbox}"
PREFIX="${PREFIX:-${HOME}/.local}"
MAN_DIR="${PREFIX}/share/man/man1"
mkdir -p "${MAN_DIR}"

tmp="$(mktemp -d)"
trap 'rm -rf "${tmp}"' EXIT

echo "Heartbox: theme pack (no binary)."
echo "Clone or download themes from: https://github.com/${REPO}"
echo ""
echo "  git clone https://github.com/${REPO}.git"
echo "  ls heartbox/themes/"
echo ""

# Prefer release asset man page if present; else skip quietly
asset="https://github.com/${REPO}/releases/latest/download/heartbox.1"
if command -v curl >/dev/null 2>&1; then
  if curl -fsSL "${asset}" -o "${tmp}/heartbox.1" 2>/dev/null; then
    install -m 0644 "${tmp}/heartbox.1" "${MAN_DIR}/heartbox.1"
    echo "Installed man page → ${MAN_DIR}/heartbox.1"
  else
    echo "No man page asset on latest release yet; see man/heartbox.1.md in the repo."
  fi
fi

echo "Done. Site: https://heartbox.f00.sh"
