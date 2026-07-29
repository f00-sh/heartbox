# Port template — Heartbox

Copy this checklist when adding an app under `themes/<app>/`.

## Palette (always use these hex values)

| Token | Hex | Use |
|---|---|---|
| background | `#191413` | app chrome, editor bg |
| current_line | `#3D2F2D` | line highlight, panels |
| selection | `#4B1006` | selection |
| foreground | `#E8E4DC` | primary text |
| comment | `#7A656A` | comments, muted |
| sky | `#0888ED` | functions, types, links (verse blue) |
| green | `#5A8A42` | strings alt, classes, success |
| orange | `#EA5638` | numbers, warnings |
| pink | `#C97A86` | keywords |
| purple | `#6B4A58` | constants, builtins |
| red | `#E5141A` | poppy accent, errors, tags |
| yellow | `#D4B84A` | strings |
| **silver** | `#C2C8CC` | **cursor, chrome, punctuation — Kurt jacket metal** |

## Feel rules

1. Dark, warm-black base — never cool pure navy like default IDE themes.
2. Poppy red is the hero accent (active tab, focus ring, mode indicator).
3. Silver is subtle: cursor and borders, not loud fills.
4. Sky blue for “verse” calm tokens (functions/links); red for “chorus” emphasis.
5. Prefer cream foreground `#E8E4DC` over pure white.

## Files

- Prefer a single theme file + short install note in the app folder README if needed.
- Regenerate machine ports: `python3 scripts/generate-themes.py` (do not hand-edit generated files).
