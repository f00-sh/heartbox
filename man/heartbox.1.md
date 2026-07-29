# heartbox(1) — Heartbox theme pack

## Name

heartbox — hand-tinted Technicolor dark theme for terminals, editors, and tools

## Synopsis

```text
git clone https://github.com/f00-sh/heartbox.git
cp themes/<app>/…  # per-app install
python3 scripts/generate-themes.py   # maintainers
```

## Description

**Heartbox** is a dark color theme defined by a single canonical palette and
many application ports. Colors favor warm hospital-night blacks, poppy red as
the hero accent, verse-sky cyan/blue for calm tokens, cream foreground text,
and a cool **silver** metal accent for cursors and chrome.

Canonical palette path: `palette/heartbox.json`.

Product site: https://heartbox.f00.sh

## Palette tokens

| Token | Hex |
|-------|-----|
| background | #1A1214 |
| current_line | #2C1F22 |
| selection | #3A2428 |
| foreground | #F4EBE0 |
| comment | #8A6E78 |
| sky | #5EC8E8 |
| green | #5FBF4A |
| orange | #E8924A |
| pink | #E86A9A |
| purple | #7A5A9E |
| red | #E02030 |
| yellow | #E8D45A |
| silver | #B8C0C8 |

## Files

| Path | Purpose |
|------|---------|
| `palette/heartbox.json` | Source of truth |
| `palette/heartbox.{css,toml,yaml,scss}` | Interchange formats |
| `themes/<app>/` | Application ports |
| `themes/TEMPLATE.md` | How to add a port |
| `scripts/generate-themes.py` | Regenerate ports |
| `site/` | Product website sources |

## Environment

None required. Optional: source `themes/fzf/heartbox.sh` for fzf colors.

## Exit status

Generator exits 0 on success.

## See also

- https://heartbox.f00.sh
- https://github.com/f00-sh/heartbox
- https://f00.sh

## Bugs

Report issues at https://github.com/f00-sh/heartbox/issues

## License

MIT
