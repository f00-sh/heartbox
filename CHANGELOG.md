## [0.3.1] - 2026-04-10

### Changed

- Photo-locked palette to organic poppy-xray hero (`hb-hero-xray-r8`): sky `#1E78C8`, poppy `#D44A18`.
- Restored translucent xray field drama (std ~97); pure-channel clip on photo ends only.
- Favicons / brand marks recolored to match; all ports regenerated; f00 `theme-33`.

## [0.3.0] - 2026-04-10

### Changed

- Dye-transfer Technicolor pass: warm cobalt sky `#2A7EB0`, Oz poppy scarlet `#B82E18`.
- Cool silver chrome ladder (`#D0D5DB` / `#E4E8ED` / `#B8BEC2`); pure white banned.
- Hospital cream paper UI (`#E8DFD4`) with poppy type; ANSI brights desaturated.
- Regenerated all app ports; f00 shared CSS `f00-theme-32.css` + hero `hb-hero-dye-r7`.

## [0.2.1] - 2026-07-29

### Changed

- Palette vision-locked from Heart-Shaped Box video frames (pure verse sky `#2096EE`, chorus blood `#C50A1B`, hospital charcoal `#090909`).
- All app ports regenerated; f00 shared CSS tracks this version.

## [0.2.0] - 2026-07-29

### Changed

- Palette resampled from Heart-Shaped Box video frames (verse sky `#0888ED`, poppy `#E5141A`, hospital-night `#191413`, silver metal).
- Regenerated all application ports from `palette/heartbox.json`.
- Shared f00 brand CSS tracks this palette at `https://f00.sh/theme/f00-theme.css`.

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Noctalia port (`themes/noctalia/`) — custom palette JSON for Noctalia v5 shell

## Unreleased

### Note

Released as 0.2.0 below.

### Changed

- Palette resampled from Heart-Shaped Box video frames (verse sky `#0888ED`, poppy `#E5141A`, hospital-night `#191413`, silver metal).
- Regenerated all application ports from `palette/heartbox.json`.
- Shared f00 brand CSS tracks this palette at `https://f00.sh/theme/f00-theme.css`.



### Changed

- Declared as **f00 default brand theme**; product site loads `f00-theme-13.css` from the hub.

## [0.1.0] — 2026-07-29

### Added

- Canonical Heartbox palette (`palette/heartbox.json` + CSS/TOML/YAML/SCSS)
- Silver metal token (`#B8C0C8`) for cursor/chrome/punctuation
- Generator `scripts/generate-themes.py`
- Ports for 45+ apps (terminals, editors, shells, bars, CLIs)
- Product site `site/` for https://heartbox.f00.sh
- Man page, scene card, docs seed, Cloudflare Pages workflow

[0.1.0]: https://github.com/f00-sh/heartbox/releases/tag/v0.1.0
