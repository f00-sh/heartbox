# Port template — Heartbox

Copy this checklist when adding an app under `themes/<app>/`.

## Palette (always use these hex values)

| Token | Hex | Use |
|---|---|---|
| background | `#090909` | app chrome, editor bg |
| current_line | `#1C1617` | line highlight, panels |
| selection | `#56180A` | selection |
| foreground | `#EDE6DE` | primary text |
| comment | `#8A7874` | comments, muted |
| sky | `#2A7EB0` | functions, types, links (verse blue) |
| green | `#5A7A42` | strings alt, classes, success |
| orange | `#C45A20` | numbers, warnings |
| pink | `#C47A72` | keywords |
| purple | `#454B93` | constants, builtins |
| red | `#B82E18` | poppy accent, errors, tags |
| yellow | `#C49A3C` | strings |
| **silver** | `#B8BEC2` | **cursor, chrome, punctuation — Kurt jacket metal** |

## Feel rules

1. Dark, warm-black base — never cool pure navy like default IDE themes.
2. Poppy red is the hero accent (active tab, focus ring, mode indicator).
3. Silver is subtle: cursor and borders, not loud fills.
4. Sky blue for “verse” calm tokens (functions/links); red for “chorus” emphasis.
5. Prefer cream foreground `#EDE6DE` over pure white.

## Files

- Prefer a single theme file + short install note in the app folder README if needed.
- Regenerate machine ports: `python3 scripts/generate-themes.py` (do not hand-edit generated files).
