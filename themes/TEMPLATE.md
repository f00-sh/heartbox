# Port template — Heartbox

Copy this checklist when adding an app under `themes/<app>/`.

## Palette (always use these hex values)

| Token | Hex | Use |
|---|---|---|
| background | `#1A1214` | app chrome, editor bg |
| current_line | `#2C1F22` | line highlight, panels |
| selection | `#3A2428` | selection |
| foreground | `#F4EBE0` | primary text |
| comment | `#8A6E78` | comments, muted |
| sky | `#5EC8E8` | functions, types, links (verse blue) |
| green | `#5FBF4A` | strings alt, classes, success |
| orange | `#E8924A` | numbers, warnings |
| pink | `#E86A9A` | keywords |
| purple | `#7A5A9E` | constants, builtins |
| red | `#E02030` | poppy accent, errors, tags |
| yellow | `#E8D45A` | strings |
| **silver** | `#B8C0C8` | **cursor, chrome, punctuation — Kurt jacket metal** |

## Feel rules

1. Dark, warm-black base — never cool pure navy like default IDE themes.
2. Poppy red is the hero accent (active tab, focus ring, mode indicator).
3. Silver is subtle: cursor and borders, not loud fills.
4. Sky blue for “verse” calm tokens (functions/links); red for “chorus” emphasis.
5. Prefer cream foreground `#F4EBE0` over pure white.

## Files

- Prefer a single theme file + short install note in the app folder README if needed.
- Regenerate machine ports: `python3 scripts/generate-themes.py` (do not hand-edit generated files).
