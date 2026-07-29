# Heartbox

**One theme. Many surfaces.** Hand-tinted Technicolor dark colors —
poppy red, verse-sky blue, hospital gloom, anatomical pink, bruise purple,
and a cool **silver** metal accent.

- **Site:** https://heartbox.f00.sh
- **Repo:** https://github.com/f00-sh/heartbox
- **Hub:** https://f00.sh
- **License:** MIT

## Palette

| Token | Hex | Role |
|-------|-----|------|
| background | `#1A1214` | Hospital-night underpaint |
| current_line | `#2C1F22` | Surface / line highlight |
| selection | `#3A2428` | Selection |
| foreground | `#F4EBE0` | Hand-tinted cream |
| comment | `#8A6E78` | Dusty mauve |
| sky | `#5EC8E8` | Verse technicolor blue |
| green | `#5FBF4A` | Field / stem green |
| orange | `#E8924A` | Amber warmth |
| pink | `#E86A9A` | Heart / anatomical pink |
| purple | `#7A5A9E` | Bruise purple |
| red | `#E02030` | Poppy red (hero) |
| yellow | `#E8D45A` | Hand-tint yellow |
| **silver** | `#B8C0C8` | **Cool metal jacket** |

Canonical files: [`palette/heartbox.json`](palette/heartbox.json) · CSS · TOML · YAML · SCSS.

Aesthetic inspiration: the hand-painted Technicolor look of a famous 1993 poppy-field music video (sky/box blue↔red shifts, hyper-real reds, warm blacks). Heartbox is original work and is **not** affiliated with any band, label, or rights holder.

## Install

```bash
git clone https://github.com/f00-sh/heartbox.git
cd heartbox
ls themes/
```

Copy the port for your app from `themes/<app>/`. Examples:

```bash
# Kitty
cp themes/kitty/heartbox.conf ~/.config/kitty/themes/
# then: include themes/heartbox.conf  (or kitten themes)

# Alacritty
cp themes/alacritty/heartbox.toml ~/.config/alacritty/themes/

# Neovim
mkdir -p ~/.config/nvim/colors
cp themes/neovim/heartbox.lua ~/.config/nvim/colors/
# :colorscheme heartbox  (or require the file)

# VS Code / Cursor — use themes/vscode/heartbox-color-theme.json
# as a custom color theme or extension base

# fzf
source themes/fzf/heartbox.sh
```

Full port list and rules: [`themes/TEMPLATE.md`](themes/TEMPLATE.md).

### Curl helper (man page)

```text
curl -fsSL https://github.com/f00-sh/heartbox/releases/latest/download/install.sh | sh
```

Installs man page(s) when present on the release; theme files live in the repo tree.

## Ports (shipped)

alacritty · kitty · wezterm · ghostty · foot · windows-terminal · iterm · xresources · tmux · warp · hyper · vim · neovim · helix · emacs · sublime · vscode · zed · jetbrains · nano · kakoune · bat · fzf · rofi · dunst · slack · starship · btop · lsd · delta · lazygit · gitui · yazi · k9s · waybar · hyprland · i3 · polybar · zellij · fish · zsh-syntax · obsidian · base16 · cava · css · json · yaml · toml

Want another app? Open a PR with a folder under `themes/` following the template. Prefer regenerating shared formats via:

```bash
python3 scripts/generate-themes.py
```

## Documentation

| Surface | Location |
|---------|----------|
| This README | [README.md](README.md) |
| Man page | [man/heartbox.1.md](man/heartbox.1.md) |
| Product site | https://heartbox.f00.sh · [site/](site/) |
| Changelog | [CHANGELOG.md](CHANGELOG.md) |
| Scene card | [file_id.diz](file_id.diz) |
| Spec / SOP | [docs/](docs/) |

## Scene card

```text
╔══════════════════════════════════════════════════╗
║▓▓▓▓░░░░  HEARTBOX  ░░░░▓▓▓▓                      ║
║████████████████████████████████████████████████  ║
║  ▄█▀  SCENE CARD  ▀█▄   theme identity           ║
║████████████████████████████████████████████████  ║
║  v0.1.0  ·  MIT  ·  2026                         ║
║  hand-tinted technicolor dark · poppy · silver   ║
║  github:f00-sh/heartbox                          ║
╚══════════════════════════════════════════════════╝
```

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md).

1. Edit `palette/heartbox.json` only for color changes.
2. Run `python3 scripts/generate-themes.py`.
3. Hand-tune app-specific ports only when the generator cannot express them.
4. Keep silver on cursor/border/punctuation tokens.

## Versioning

[Semantic Versioning](https://semver.org/). See [CHANGELOG.md](CHANGELOG.md).

## Security

See [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE) © f00 / William Theesfeld
