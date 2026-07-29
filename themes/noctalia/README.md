# Heartbox — Noctalia

Custom palette for [Noctalia](https://noctalia.dev) (v5 palette JSON).

## Install

```bash
mkdir -p ~/.config/noctalia/palettes
cp themes/noctalia/heartbox.json ~/.config/noctalia/palettes/Heartbox.json
```

Then in Noctalia config (`~/.config/noctalia/*.toml`):

```toml
[theme]
mode           = "dark"
source         = "custom"
custom_palette = "Heartbox"
```

Or pick **custom → Heartbox** in Settings → Theme / Color scheme.

Dark mode is the canonical hospital-night Heartbox look (poppy red primary,
verse-sky secondary, silver outline/cursor). Light mode inverts surfaces onto
cream/peak-white while keeping the same accents.

Regenerated from `palette/heartbox.json` via `python3 scripts/generate-themes.py`.
