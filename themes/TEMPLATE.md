# Port template — Heartbox

Copy this checklist when adding an app under `themes/<app>/`.

## Palette (always use these hex values)

| Token | Hex | Use |
|---|---|---|
| background | `#0A1528` | app chrome, editor bg |
| current_line | `#142238` | line highlight, panels |
| selection | `#4E1A22` | selection |
| foreground | `#EDE6DE` | primary text |
| comment | `#6E7A8A` | comments, muted |
| sky | `#1E8AE8` | functions, types, links (verse blue) |
| green | `#3D9650` | strings alt, classes, success |
| orange | `#E06028` | numbers, warnings |
| pink | `#D47A82` | keywords |
| purple | `#5A4E9E` | constants, builtins |
| red | `#E03818` | poppy accent, errors, tags |
| yellow | `#D4A838` | strings |
| **silver** | `#B8C0C8` | **cursor, chrome, punctuation — Kurt jacket metal** |

## Feel rules

1. Dark, warm-black base — never cool pure navy like default IDE themes.
2. Poppy red is the hero accent (active tab, focus ring, mode indicator).
3. Silver is subtle: cursor and borders, not loud fills.
4. Sky blue for “verse” calm tokens (functions/links); red for “chorus” emphasis.
5. Prefer cream foreground `#EDE6DE` over pure white.

## Files

- Prefer a single theme file + short install note in the app folder README if needed.
- Regenerate machine ports: `python3 scripts/generate-themes.py` (do not hand-edit generated files).
