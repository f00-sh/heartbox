#!/usr/bin/env bash
# Install / re-sync Heartbox theme ports onto this machine for every
# detected application that has a themes/<app> port.
#
# Usage:
#   ./scripts/install-local-themes.sh           # copy + enable where safe
#   ./scripts/install-local-themes.sh --copy-only
#   HEARTBOX_ROOT=~/src/heartbox ./scripts/install-local-themes.sh
set -euo pipefail

ROOT="${HEARTBOX_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
THEMES="${ROOT}/themes"
COPY_ONLY=0
[[ "${1:-}" == "--copy-only" ]] && COPY_ONLY=1

have() { command -v "$1" >/dev/null 2>&1; }
ok() { printf '  \033[32mok\033[0m  %s\n' "$*"; }
skip() { printf '  \033[33mskip\033[0m %s\n' "$*"; }
note() { printf '  \033[36m→\033[0m  %s\n' "$*"; }

# Rewrite KEY=VALUE style lines (drop old KEY, append one)
set_line() {
  local file="$1" pattern="$2" line="$3"
  mkdir -p "$(dirname "$file")"
  local tmp; tmp="$(mktemp)"
  if [[ -f "$file" ]]; then
    grep -v -E "$pattern" "$file" >"$tmp" || true
  else
    : >"$tmp"
  fi
  printf '%s\n' "$line" >>"$tmp"
  mv "$tmp" "$file"
}

install_file() {
  local src="$1" dest="$2"
  mkdir -p "$(dirname "$dest")"
  install -m 0644 "$src" "$dest"
}

echo "Heartbox local install"
echo "  source: $THEMES"
echo

# ── always: hub under ~/.config/heartbox (shell helpers) ──
mkdir -p "${HOME}/.config/heartbox"
install_file "${THEMES}/fzf/heartbox.sh" "${HOME}/.config/heartbox/fzf.sh"
install_file "${THEMES}/zsh-syntax/heartbox.zsh" "${HOME}/.config/heartbox/zsh-syntax.zsh"
# keep existing dircolors if present (hand-tuned)
if [[ ! -f "${HOME}/.config/heartbox/dircolors" ]]; then
  note "no dircolors yet (optional)"
fi
ok "hub helpers → ~/.config/heartbox/{fzf,zsh-syntax}.sh"

# ── ghostty ──
if have ghostty || [[ -d "${HOME}/.config/ghostty" ]]; then
  install_file "${THEMES}/ghostty/heartbox" "${HOME}/.config/ghostty/themes/heartbox"
  if [[ "$COPY_ONLY" -eq 0 ]]; then
    set_line "${HOME}/.config/ghostty/config.ghostty"       '^[[:space:]]*theme[[:space:]]*=' 'theme = heartbox'
    ok "ghostty theme=heartbox"
  else
    ok "ghostty theme file copied"
  fi
else
  skip "ghostty not present"
fi

# ── bat ──
if have bat || [[ -d "${HOME}/.config/bat" ]]; then
  install_file "${THEMES}/bat/heartbox.tmTheme" "${HOME}/.config/bat/themes/heartbox.tmTheme"
  if have bat; then
    bat cache --build >/dev/null 2>&1 || true
  fi
  if [[ "$COPY_ONLY" -eq 0 ]]; then
    set_line "${HOME}/.config/bat/config"       '^[[:space:]]*--theme=' '--theme=heartbox'
    ok "bat --theme=heartbox"
  else
    ok "bat theme file copied"
  fi
else
  skip "bat not present"
fi

# ── btop ──
if have btop || [[ -d "${HOME}/.config/btop" ]]; then
  install_file "${THEMES}/btop/heartbox.theme" "${HOME}/.config/btop/themes/heartbox.theme"
  if [[ "$COPY_ONLY" -eq 0 && -f "${HOME}/.config/btop/btop.conf" ]]; then
    sed -i 's/^color_theme = .*/color_theme = "heartbox"/' "${HOME}/.config/btop/btop.conf"
    ok "btop color_theme=heartbox"
  else
    ok "btop theme file copied"
  fi
else
  skip "btop not present"
fi

# ── lazygit ──
if have lazygit || [[ -d "${HOME}/.config/lazygit" ]]; then
  install_file "${THEMES}/lazygit/heartbox.yml" "${HOME}/.config/lazygit/themes/heartbox.yml"
  if [[ "$COPY_ONLY" -eq 0 ]]; then
    conf="${HOME}/.config/lazygit/config.yml"
    mkdir -p "$(dirname "$conf")"
    # Prefer full theme file content as config when config is only theme block
    # or merge: write guitheme from port if no gui.theme section
    if [[ ! -f "$conf" ]] || ! grep -q 'activeBorderColor' "$conf" 2>/dev/null; then
      cp "${THEMES}/lazygit/heartbox.yml" "$conf"
    else
      # refresh colors from port file (overwrite config with port — it's pure theme)
      cp "${THEMES}/lazygit/heartbox.yml" "$conf"
    fi
    ok "lazygit config ← themes/lazygit/heartbox.yml"
  else
    ok "lazygit theme file copied"
  fi
else
  skip "lazygit not present"
fi

# ── starship ──
if have starship || [[ -f "${HOME}/.config/starship.toml" ]]; then
  install_file "${THEMES}/starship/heartbox.toml" "${HOME}/.config/starship-heartbox.toml"
  # Do not clobber a full custom starship.toml — only ensure palette fragment exists
  if [[ "$COPY_ONLY" -eq 0 && -f "${HOME}/.config/starship.toml" ]]; then
    if grep -q 'palette = "heartbox"' "${HOME}/.config/starship.toml" 2>/dev/null; then
      ok "starship already palette=heartbox (left full config intact)"
    else
      note "starship.toml present without heartbox palette — not overwriting; see starship-heartbox.toml"
    fi
  else
    ok "starship heartbox.toml copied"
  fi
else
  skip "starship not present"
fi

# ── yazi ──
if have yazi || [[ -d "${HOME}/.config/yazi" ]]; then
  mkdir -p "${HOME}/.config/yazi/flavors/heartbox.yazi"
  # yazi flavors are directories; port is a single toml — install both ways
  install_file "${THEMES}/yazi/heartbox.toml" "${HOME}/.config/yazi/heartbox.toml"
  install_file "${THEMES}/yazi/heartbox.toml" "${HOME}/.config/yazi/flavors/heartbox.yazi/flavor.toml"
  if [[ "$COPY_ONLY" -eq 0 ]]; then
    conf="${HOME}/.config/yazi/theme.toml"
    mkdir -p "$(dirname "$conf")"
    cat >"$conf" <<'EOF'
[flavor]
dark = "heartbox"
light = "heartbox"
EOF
    ok "yazi flavor=heartbox"
  else
    ok "yazi theme files copied"
  fi
else
  skip "yazi not present"
fi

# ── zed ──
if have zed || have zed-editor || [[ -d "${HOME}/.config/zed" ]]; then
  install_file "${THEMES}/zed/heartbox.json" "${HOME}/.config/zed/themes/heartbox.json"
  install_file "${THEMES}/zed/heartbox.json" "${HOME}/.config/zed/themes/Heartbox.json"
  if [[ "$COPY_ONLY" -eq 0 && -f "${HOME}/.config/zed/settings.json" ]]; then
    if grep -q '"Heartbox"' "${HOME}/.config/zed/settings.json" 2>/dev/null; then
      ok "zed dark theme already Heartbox"
    else
      note "zed: set theme.dark to Heartbox in settings if needed (file installed)"
    fi
  else
    ok "zed theme files copied"
  fi
else
  skip "zed not present"
fi

# ── vim ──
if have vim || [[ -d "${HOME}/.vim" ]]; then
  install_file "${THEMES}/vim/heartbox.vim" "${HOME}/.vim/colors/heartbox.vim"
  if [[ "$COPY_ONLY" -eq 0 ]]; then
    if [[ -f "${HOME}/.vimrc" ]] && grep -q 'colorscheme heartbox' "${HOME}/.vimrc" 2>/dev/null; then
      ok "vim colorscheme heartbox"
    elif [[ -f "${HOME}/.vimrc" ]]; then
      echo 'colorscheme heartbox' >>"${HOME}/.vimrc"
      ok "vim: appended colorscheme heartbox"
    else
      printf 'colorscheme heartbox\n' >"${HOME}/.vimrc"
      ok "vim: created ~/.vimrc with heartbox"
    fi
  else
    ok "vim colorscheme file copied"
  fi
else
  skip "vim not present"
fi

# ── nano ──
if have nano || [[ -d "${HOME}/.config/nano" ]]; then
  install_file "${THEMES}/nano/heartbox.nanorc" "${HOME}/.config/nano/heartbox.nanorc"
  if [[ "$COPY_ONLY" -eq 0 ]]; then
    if [[ -f "${HOME}/.nanorc" ]] && grep -q 'heartbox.nanorc' "${HOME}/.nanorc" 2>/dev/null; then
      ok "nano includes heartbox.nanorc"
    else
      echo "include \"${HOME}/.config/nano/heartbox.nanorc\"" >>"${HOME}/.nanorc"
      ok "nano: include heartbox.nanorc"
    fi
  else
    ok "nano nanorc copied"
  fi
else
  skip "nano not present"
fi

# ── fzf ──
if have fzf || [[ -d "${HOME}/.config/fzf" ]]; then
  install_file "${THEMES}/fzf/heartbox.sh" "${HOME}/.config/fzf/heartbox.sh"
  install_file "${THEMES}/fzf/heartbox.sh" "${HOME}/.config/heartbox/fzf.sh"
  if [[ "$COPY_ONLY" -eq 0 ]]; then
    if grep -q 'heartbox/fzf\|fzf/heartbox' "${HOME}/.zshrc" 2>/dev/null; then
      ok "fzf heartbox sourced from zshrc"
    else
      note "add: source ~/.config/heartbox/fzf.sh  (already in many f00 shells)"
    fi
  else
    ok "fzf heartbox.sh copied"
  fi
else
  skip "fzf not present"
fi

# ── zsh-syntax ──
if have zsh; then
  install_file "${THEMES}/zsh-syntax/heartbox.zsh" "${HOME}/.config/heartbox/zsh-syntax.zsh"
  if grep -q 'zsh-syntax.zsh' "${HOME}/.zshrc" 2>/dev/null; then
    ok "zsh-syntax heartbox already wired"
  else
    note "ensure zsh-syntax-highlighting loads, then source ~/.config/heartbox/zsh-syntax.zsh last"
  fi
else
  skip "zsh not present"
fi

# ── noctalia palette ──
if [[ -d "${HOME}/.config/noctalia" ]] || have noctalia; then
  mkdir -p "${HOME}/.config/noctalia/palettes"
  install_file "${THEMES}/noctalia/heartbox.json" "${HOME}/.config/noctalia/palettes/Heartbox.json"
  ok "noctalia palette Heartbox.json (select as custom_palette in Noctalia if not active)"
else
  skip "noctalia config dir not present"
fi

# ── delta (git) ──
if have delta; then
  install_file "${THEMES}/delta/heartbox.gitconfig" "${HOME}/.config/heartbox/delta.gitconfig"
  if [[ "$COPY_ONLY" -eq 0 ]]; then
    git config --global include.path "${HOME}/.config/heartbox/delta.gitconfig" || true
    ok "delta git include.path → heartbox"
  else
    ok "delta gitconfig copied"
  fi
else
  skip "delta not installed (port ready under themes/delta/)"
fi

# ── optional tools if binary exists ──
if have helix || [[ -d "${HOME}/.config/helix" ]]; then
  install_file "${THEMES}/helix/heartbox.toml" "${HOME}/.config/helix/themes/heartbox.toml"
  ok "helix theme file (set theme = \"heartbox\" in config.toml)"
fi
if have foot || [[ -d "${HOME}/.config/foot" ]]; then
  install_file "${THEMES}/foot/heartbox.ini" "${HOME}/.config/foot/heartbox.ini"
  ok "foot theme file"
fi
if have kitty || [[ -d "${HOME}/.config/kitty" ]]; then
  mkdir -p "${HOME}/.config/kitty/themes"
  install_file "${THEMES}/kitty/heartbox.conf" "${HOME}/.config/kitty/themes/heartbox.conf"
  ok "kitty theme file"
fi
if have alacritty || [[ -d "${HOME}/.config/alacritty" ]]; then
  mkdir -p "${HOME}/.config/alacritty/themes"
  install_file "${THEMES}/alacritty/heartbox.toml" "${HOME}/.config/alacritty/themes/heartbox.toml"
  ok "alacritty theme file"
fi
if have wezterm || [[ -d "${HOME}/.config/wezterm" ]]; then
  install_file "${THEMES}/wezterm/heartbox.toml" "${HOME}/.config/wezterm/heartbox.toml"
  ok "wezterm theme file"
fi
if have tmux || [[ -d "${HOME}/.config/tmux" ]]; then
  install_file "${THEMES}/tmux/heartbox.tmux" "${HOME}/.config/tmux/heartbox.tmux"
  ok "tmux theme file"
fi
if have rofi || [[ -d "${HOME}/.config/rofi" ]]; then
  install_file "${THEMES}/rofi/heartbox.rasi" "${HOME}/.config/rofi/heartbox.rasi"
  ok "rofi theme file"
fi
if have dunst || [[ -d "${HOME}/.config/dunst" ]]; then
  install_file "${THEMES}/dunst/heartbox.dunstrc" "${HOME}/.config/dunst/heartbox.dunstrc"
  ok "dunst theme file"
fi
if have waybar || [[ -d "${HOME}/.config/waybar" ]]; then
  mkdir -p "${HOME}/.config/waybar"
  install_file "${THEMES}/waybar/heartbox.css" "${HOME}/.config/waybar/heartbox.css"
  ok "waybar heartbox.css (import from style.css if used)"
fi
if have gitui || [[ -d "${HOME}/.config/gitui" ]]; then
  install_file "${THEMES}/gitui/heartbox.ron" "${HOME}/.config/gitui/heartbox.ron"
  ok "gitui theme file"
fi
if have zellij || [[ -d "${HOME}/.config/zellij" ]]; then
  mkdir -p "${HOME}/.config/zellij/themes"
  install_file "${THEMES}/zellij/heartbox.kdl" "${HOME}/.config/zellij/themes/heartbox.kdl"
  ok "zellij theme file"
fi
if have fish || [[ -d "${HOME}/.config/fish" ]]; then
  mkdir -p "${HOME}/.config/fish/themes"
  install_file "${THEMES}/fish/heartbox.fish" "${HOME}/.config/fish/themes/heartbox.fish" 2>/dev/null \
    || install_file "${THEMES}/fish/heartbox.fish" "${HOME}/.config/fish/heartbox.fish"
  ok "fish theme file"
fi
if have nvim || [[ -d "${HOME}/.config/nvim" ]]; then
  mkdir -p "${HOME}/.config/nvim/colors"
  install_file "${THEMES}/neovim/heartbox.lua" "${HOME}/.config/nvim/colors/heartbox.lua"
  ok "neovim colors/heartbox.lua"
fi

# ── VS Code / Cursor if present ──
for ed in code cursor codium; do
  if have "$ed"; then
    ext_dir="${HOME}/.config/${ed}/User"
    # Cursor uses ~/.config/Cursor sometimes
    [[ "$ed" == cursor ]] && ext_dir="${HOME}/.config/Cursor/User"
    mkdir -p "${HOME}/.local/share/heartbox-vscode"
    install_file "${THEMES}/vscode/heartbox-color-theme.json" \
      "${HOME}/.local/share/heartbox-vscode/heartbox-color-theme.json"
    note "$ed: theme JSON at ~/.local/share/heartbox-vscode/ (install as custom color theme)"
  fi
done

echo
echo "Done. Active switches applied for: ghostty, bat, yazi, btop, lazygit, vim, nano (when present)."
echo "Restart terminals / reload shell for full effect."
echo "Noctalia: palette installed — pick custom palette Heartbox in Noctalia UI if apps still follow Noctalia templates."
