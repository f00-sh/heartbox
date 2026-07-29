#!/usr/bin/env python3
"""Generate Heartbox theme ports from palette/heartbox.json."""
from __future__ import annotations

import json
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTE = json.loads((ROOT / "palette" / "heartbox.json").read_text())
C = PALETTE["colors"]
A = PALETTE["ansi"]
U = PALETTE["ui"]
S = PALETTE["syntax"]


def hx(key: str) -> str:
    if key in C:
        return C[key]["hex"]
    if key in A:
        return A[key]
    if key in U:
        return U[key]
    raise KeyError(key)


def rgb(key: str) -> tuple[int, int, int]:
    return tuple(C[key]["rgb"])  # type: ignore[return-value]


def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n")
    print("wrote", rel)


def gen_canonical() -> None:
    # CSS variables
    write(
        "palette/heartbox.css",
        textwrap.dedent(
            f"""\
            /* Heartbox Theme — canonical CSS custom properties */
            :root {{
              --hb-bg: {hx('background')};
              --hb-bg-alt: {hx('current_line')};
              --hb-selection: {hx('selection')};
              --hb-fg: {hx('foreground')};
              --hb-comment: {hx('comment')};
              --hb-sky: {hx('sky')};
              --hb-green: {hx('green')};
              --hb-orange: {hx('orange')};
              --hb-pink: {hx('pink')};
              --hb-purple: {hx('purple')};
              --hb-red: {hx('red')};
              --hb-yellow: {hx('yellow')};
              --hb-silver: {hx('silver')};
              --hb-bright-black: {hx('bright_black')};
              --hb-bright-white: {hx('bright_white')};
              --hb-panel: {U['panel']};
              --hb-border: {U['border']};
              --hb-accent: {U['accent']};
              --hb-metal: {U['metal']};
            }}
            """
        ),
    )
    # TOML
    write(
        "palette/heartbox.toml",
        textwrap.dedent(
            f"""\
            # Heartbox Theme — canonical palette
            name = "Heartbox"
            version = "{PALETTE['version']}"

            [colors]
            background = "{hx('background')}"
            current_line = "{hx('current_line')}"
            selection = "{hx('selection')}"
            foreground = "{hx('foreground')}"
            comment = "{hx('comment')}"
            sky = "{hx('sky')}"
            green = "{hx('green')}"
            orange = "{hx('orange')}"
            pink = "{hx('pink')}"
            purple = "{hx('purple')}"
            red = "{hx('red')}"
            yellow = "{hx('yellow')}"
            silver = "{hx('silver')}"
            """
        ),
    )
    # YAML
    write(
        "palette/heartbox.yaml",
        textwrap.dedent(
            f"""\
            name: Heartbox
            version: "{PALETTE['version']}"
            colors:
              background: "{hx('background')}"
              current_line: "{hx('current_line')}"
              selection: "{hx('selection')}"
              foreground: "{hx('foreground')}"
              comment: "{hx('comment')}"
              sky: "{hx('sky')}"
              green: "{hx('green')}"
              orange: "{hx('orange')}"
              pink: "{hx('pink')}"
              purple: "{hx('purple')}"
              red: "{hx('red')}"
              yellow: "{hx('yellow')}"
              silver: "{hx('silver')}"
            """
        ),
    )
    # SCSS map
    write(
        "palette/heartbox.scss",
        textwrap.dedent(
            f"""\
            // Heartbox Theme
            $heartbox: (
              "background": {hx('background')},
              "current-line": {hx('current_line')},
              "selection": {hx('selection')},
              "foreground": {hx('foreground')},
              "comment": {hx('comment')},
              "sky": {hx('sky')},
              "green": {hx('green')},
              "orange": {hx('orange')},
              "pink": {hx('pink')},
              "purple": {hx('purple')},
              "red": {hx('red')},
              "yellow": {hx('yellow')},
              "silver": {hx('silver')},
            );
            """
        ),
    )
    # base16
    write(
        "themes/base16/base16-heartbox.yaml",
        textwrap.dedent(
            f"""\
            scheme: "Heartbox"
            author: "f00"
            base00: "{hx('background')[1:]}"
            base01: "{hx('current_line')[1:]}"
            base02: "{hx('selection')[1:]}"
            base03: "{hx('comment')[1:]}"
            base04: "{hx('silver')[1:]}"
            base05: "{hx('foreground')[1:]}"
            base06: "{hx('bright_white')[1:]}"
            base07: "{hx('bright_white')[1:]}"
            base08: "{hx('red')[1:]}"
            base09: "{hx('orange')[1:]}"
            base0A: "{hx('yellow')[1:]}"
            base0B: "{hx('green')[1:]}"
            base0C: "{hx('sky')[1:]}"
            base0D: "{hx('sky')[1:]}"
            base0E: "{hx('pink')[1:]}"
            base0F: "{hx('purple')[1:]}"
            """
        ),
    )


def gen_terminals() -> None:
    write(
        "themes/alacritty/heartbox.toml",
        textwrap.dedent(
            f"""\
            # Heartbox — Alacritty
            [colors.primary]
            background = "{hx('background')}"
            foreground = "{hx('foreground')}"

            [colors.cursor]
            text = "{hx('background')}"
            cursor = "{hx('silver')}"

            [colors.selection]
            text = "{hx('foreground')}"
            background = "{hx('selection')}"

            [colors.normal]
            black = "{A['black']}"
            red = "{A['red']}"
            green = "{A['green']}"
            yellow = "{A['yellow']}"
            blue = "{A['blue']}"
            magenta = "{A['magenta']}"
            cyan = "{A['cyan']}"
            white = "{A['white']}"

            [colors.bright]
            black = "{A['bright_black']}"
            red = "{A['bright_red']}"
            green = "{A['bright_green']}"
            yellow = "{A['bright_yellow']}"
            blue = "{A['bright_blue']}"
            magenta = "{A['bright_magenta']}"
            cyan = "{A['bright_cyan']}"
            white = "{A['bright_white']}"
            """
        ),
    )
    write(
        "themes/kitty/heartbox.conf",
        textwrap.dedent(
            f"""\
            # Heartbox — Kitty
            foreground {hx('foreground')}
            background {hx('background')}
            selection_foreground {hx('foreground')}
            selection_background {hx('selection')}
            cursor {hx('silver')}
            cursor_text_color {hx('background')}
            url_color {hx('sky')}
            active_border_color {hx('red')}
            inactive_border_color {hx('bright_black')}
            active_tab_foreground {hx('background')}
            active_tab_background {hx('red')}
            inactive_tab_foreground {hx('comment')}
            inactive_tab_background {hx('current_line')}

            color0  {A['black']}
            color1  {A['red']}
            color2  {A['green']}
            color3  {A['yellow']}
            color4  {A['blue']}
            color5  {A['magenta']}
            color6  {A['cyan']}
            color7  {A['white']}
            color8  {A['bright_black']}
            color9  {A['bright_red']}
            color10 {A['bright_green']}
            color11 {A['bright_yellow']}
            color12 {A['bright_blue']}
            color13 {A['bright_magenta']}
            color14 {A['bright_cyan']}
            color15 {A['bright_white']}
            """
        ),
    )
    write(
        "themes/wezterm/heartbox.toml",
        textwrap.dedent(
            f"""\
            # Heartbox — WezTerm (include via config)
            [colors]
            foreground = "{hx('foreground')}"
            background = "{hx('background')}"
            cursor_bg = "{hx('silver')}"
            cursor_fg = "{hx('background')}"
            cursor_border = "{hx('silver')}"
            selection_fg = "{hx('foreground')}"
            selection_bg = "{hx('selection')}"
            ansi = [
              "{A['black']}",
              "{A['red']}",
              "{A['green']}",
              "{A['yellow']}",
              "{A['blue']}",
              "{A['magenta']}",
              "{A['cyan']}",
              "{A['white']}",
            ]
            brights = [
              "{A['bright_black']}",
              "{A['bright_red']}",
              "{A['bright_green']}",
              "{A['bright_yellow']}",
              "{A['bright_blue']}",
              "{A['bright_magenta']}",
              "{A['bright_cyan']}",
              "{A['bright_white']}",
            ]
            """
        ),
    )
    write(
        "themes/ghostty/heartbox",
        textwrap.dedent(
            f"""\
            # Heartbox — Ghostty
            background = {hx('background')}
            foreground = {hx('foreground')}
            cursor-color = {hx('silver')}
            selection-background = {hx('selection')}
            selection-foreground = {hx('foreground')}
            palette = 0={A['black']}
            palette = 1={A['red']}
            palette = 2={A['green']}
            palette = 3={A['yellow']}
            palette = 4={A['blue']}
            palette = 5={A['magenta']}
            palette = 6={A['cyan']}
            palette = 7={A['white']}
            palette = 8={A['bright_black']}
            palette = 9={A['bright_red']}
            palette = 10={A['bright_green']}
            palette = 11={A['bright_yellow']}
            palette = 12={A['bright_blue']}
            palette = 13={A['bright_magenta']}
            palette = 14={A['bright_cyan']}
            palette = 15={A['bright_white']}
            """
        ),
    )
    write(
        "themes/foot/heartbox.ini",
        textwrap.dedent(
            f"""\
            # Heartbox — foot
            [colors]
            foreground={hx('foreground')[1:]}
            background={hx('background')[1:]}
            selection-foreground={hx('foreground')[1:]}
            selection-background={hx('selection')[1:]}
            regular0={A['black'][1:]}
            regular1={A['red'][1:]}
            regular2={A['green'][1:]}
            regular3={A['yellow'][1:]}
            regular4={A['blue'][1:]}
            regular5={A['magenta'][1:]}
            regular6={A['cyan'][1:]}
            regular7={A['white'][1:]}
            bright0={A['bright_black'][1:]}
            bright1={A['bright_red'][1:]}
            bright2={A['bright_green'][1:]}
            bright3={A['bright_yellow'][1:]}
            bright4={A['bright_blue'][1:]}
            bright5={A['bright_magenta'][1:]}
            bright6={A['bright_cyan'][1:]}
            bright7={A['bright_white'][1:]}
            """
        ),
    )
    write(
        "themes/windows-terminal/heartbox.json",
        json.dumps(
            {
                "name": "Heartbox",
                "background": hx("background"),
                "foreground": hx("foreground"),
                "cursorColor": hx("silver"),
                "selectionBackground": hx("selection"),
                "black": A["black"],
                "red": A["red"],
                "green": A["green"],
                "yellow": A["yellow"],
                "blue": A["blue"],
                "purple": A["magenta"],
                "cyan": A["cyan"],
                "white": A["white"],
                "brightBlack": A["bright_black"],
                "brightRed": A["bright_red"],
                "brightGreen": A["bright_green"],
                "brightYellow": A["bright_yellow"],
                "brightBlue": A["bright_blue"],
                "brightPurple": A["bright_magenta"],
                "brightCyan": A["bright_cyan"],
                "brightWhite": A["bright_white"],
            },
            indent=2,
        )
        + "\n",
    )
    write(
        "themes/iterm/Heartbox.itermcolors",
        textwrap.dedent(
            f"""\
            <?xml version="1.0" encoding="UTF-8"?>
            <!-- Heartbox for iTerm2 — import via Preferences → Profiles → Colors → Color Presets → Import -->
            <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
            <plist version="1.0">
            <dict>
              <key>Ansi 0 Color</key><dict><key>Red Component</key><real>{rgb('background')[0]/255}</real><key>Green Component</key><real>{rgb('background')[1]/255}</real><key>Blue Component</key><real>{rgb('background')[2]/255}</real></dict>
              <key>Ansi 1 Color</key><dict><key>Red Component</key><real>{rgb('red')[0]/255}</real><key>Green Component</key><real>{rgb('red')[1]/255}</real><key>Blue Component</key><real>{rgb('red')[2]/255}</real></dict>
              <key>Ansi 2 Color</key><dict><key>Red Component</key><real>{rgb('green')[0]/255}</real><key>Green Component</key><real>{rgb('green')[1]/255}</real><key>Blue Component</key><real>{rgb('green')[2]/255}</real></dict>
              <key>Ansi 3 Color</key><dict><key>Red Component</key><real>{rgb('yellow')[0]/255}</real><key>Green Component</key><real>{rgb('yellow')[1]/255}</real><key>Blue Component</key><real>{rgb('yellow')[2]/255}</real></dict>
              <key>Ansi 4 Color</key><dict><key>Red Component</key><real>{rgb('sky')[0]/255}</real><key>Green Component</key><real>{rgb('sky')[1]/255}</real><key>Blue Component</key><real>{rgb('sky')[2]/255}</real></dict>
              <key>Ansi 5 Color</key><dict><key>Red Component</key><real>{rgb('pink')[0]/255}</real><key>Green Component</key><real>{rgb('pink')[1]/255}</real><key>Blue Component</key><real>{rgb('pink')[2]/255}</real></dict>
              <key>Ansi 6 Color</key><dict><key>Red Component</key><real>{rgb('sky')[0]/255}</real><key>Green Component</key><real>{rgb('sky')[1]/255}</real><key>Blue Component</key><real>{rgb('sky')[2]/255}</real></dict>
              <key>Ansi 7 Color</key><dict><key>Red Component</key><real>{rgb('foreground')[0]/255}</real><key>Green Component</key><real>{rgb('foreground')[1]/255}</real><key>Blue Component</key><real>{rgb('foreground')[2]/255}</real></dict>
              <key>Background Color</key><dict><key>Red Component</key><real>{rgb('background')[0]/255}</real><key>Green Component</key><real>{rgb('background')[1]/255}</real><key>Blue Component</key><real>{rgb('background')[2]/255}</real></dict>
              <key>Foreground Color</key><dict><key>Red Component</key><real>{rgb('foreground')[0]/255}</real><key>Green Component</key><real>{rgb('foreground')[1]/255}</real><key>Blue Component</key><real>{rgb('foreground')[2]/255}</real></dict>
              <key>Cursor Color</key><dict><key>Red Component</key><real>{rgb('silver')[0]/255}</real><key>Green Component</key><real>{rgb('silver')[1]/255}</real><key>Blue Component</key><real>{rgb('silver')[2]/255}</real></dict>
              <key>Selection Color</key><dict><key>Red Component</key><real>{rgb('selection')[0]/255}</real><key>Green Component</key><real>{rgb('selection')[1]/255}</real><key>Blue Component</key><real>{rgb('selection')[2]/255}</real></dict>
            </dict>
            </plist>
            """
        ),
    )
    write(
        "themes/xresources/heartbox.Xresources",
        textwrap.dedent(
            f"""\
            ! Heartbox — Xresources
            *.foreground:  {hx('foreground')}
            *.background:  {hx('background')}
            *.cursorColor: {hx('silver')}
            *.color0:  {A['black']}
            *.color1:  {A['red']}
            *.color2:  {A['green']}
            *.color3:  {A['yellow']}
            *.color4:  {A['blue']}
            *.color5:  {A['magenta']}
            *.color6:  {A['cyan']}
            *.color7:  {A['white']}
            *.color8:  {A['bright_black']}
            *.color9:  {A['bright_red']}
            *.color10: {A['bright_green']}
            *.color11: {A['bright_yellow']}
            *.color12: {A['bright_blue']}
            *.color13: {A['bright_magenta']}
            *.color14: {A['bright_cyan']}
            *.color15: {A['bright_white']}
            """
        ),
    )
    write(
        "themes/tmux/heartbox.tmux",
        textwrap.dedent(
            f"""\
            # Heartbox — tmux
            set -g status-style "bg={hx('current_line')},fg={hx('foreground')}"
            set -g message-style "bg={hx('selection')},fg={hx('foreground')}"
            set -g pane-border-style "fg={hx('bright_black')}"
            set -g pane-active-border-style "fg={hx('red')}"
            set -g window-status-current-style "bg={hx('red')},fg={hx('background')},bold"
            set -g window-status-style "fg={hx('comment')}"
            set -g mode-style "bg={hx('selection')},fg={hx('foreground')}"
            set -g clock-mode-colour "{hx('silver')}"
            """
        ),
    )
    write(
        "themes/warp/heartbox.yaml",
        textwrap.dedent(
            f"""\
            name: Heartbox
            accent: "{hx('red')}"
            cursor: "{hx('silver')}"
            background: "{hx('background')}"
            foreground: "{hx('foreground')}"
            details: darker
            terminal_colors:
              normal:
                black: "{A['black']}"
                red: "{A['red']}"
                green: "{A['green']}"
                yellow: "{A['yellow']}"
                blue: "{A['blue']}"
                magenta: "{A['magenta']}"
                cyan: "{A['cyan']}"
                white: "{A['white']}"
              bright:
                black: "{A['bright_black']}"
                red: "{A['bright_red']}"
                green: "{A['bright_green']}"
                yellow: "{A['bright_yellow']}"
                blue: "{A['bright_blue']}"
                magenta: "{A['bright_magenta']}"
                cyan: "{A['bright_cyan']}"
                white: "{A['bright_white']}"
            """
        ),
    )
    write(
        "themes/hyper/heartbox.js",
        textwrap.dedent(
            f"""\
            // Heartbox — Hyper
            module.exports.decorateConfig = config => ({{
              ...config,
              backgroundColor: '{hx('background')}',
              foregroundColor: '{hx('foreground')}',
              borderColor: '{hx('bright_black')}',
              cursorColor: '{hx('silver')}',
              selectionColor: 'rgba(58, 36, 40, 0.6)',
              colors: {{
                black: '{A['black']}',
                red: '{A['red']}',
                green: '{A['green']}',
                yellow: '{A['yellow']}',
                blue: '{A['blue']}',
                magenta: '{A['magenta']}',
                cyan: '{A['cyan']}',
                white: '{A['white']}',
                lightBlack: '{A['bright_black']}',
                lightRed: '{A['bright_red']}',
                lightGreen: '{A['bright_green']}',
                lightYellow: '{A['bright_yellow']}',
                lightBlue: '{A['bright_blue']}',
                lightMagenta: '{A['bright_magenta']}',
                lightCyan: '{A['bright_cyan']}',
                lightWhite: '{A['bright_white']}',
              }},
            }});
            """
        ),
    )


def gen_editors() -> None:
    write(
        "themes/vim/heartbox.vim",
        textwrap.dedent(
            f"""\
            " Heartbox — Vim
            " set colorscheme after placing in ~/.vim/colors/heartbox.vim
            hi clear
            if exists('syntax_on') | syntax reset | endif
            let g:colors_name = 'heartbox'
            set background=dark

            hi Normal       guifg={hx('foreground')} guibg={hx('background')} ctermfg=15 ctermbg=0
            hi Comment      guifg={hx('comment')} gui=italic ctermfg=8
            hi Constant     guifg={hx('purple')} ctermfg=13
            hi String       guifg={hx('yellow')} ctermfg=11
            hi Character    guifg={hx('yellow')}
            hi Number       guifg={hx('orange')} ctermfg=3
            hi Boolean      guifg={hx('purple')}
            hi Identifier   guifg={hx('foreground')} ctermfg=15
            hi Function     guifg={hx('sky')} ctermfg=14
            hi Statement    guifg={hx('pink')} ctermfg=5
            hi Keyword      guifg={hx('pink')} ctermfg=5
            hi PreProc      guifg={hx('pink')}
            hi Type         guifg={hx('sky')} ctermfg=12
            hi Special      guifg={hx('orange')}
            hi Underlined   guifg={hx('sky')} gui=underline
            hi Error        guifg={hx('foreground')} guibg={hx('red')}
            hi Todo         guifg={hx('background')} guibg={hx('yellow')}
            hi LineNr       guifg={hx('bright_black')} guibg={hx('background')}
            hi CursorLine   guibg={hx('current_line')} cterm=NONE
            hi CursorLineNr guifg={hx('silver')} gui=bold
            hi Visual       guibg={hx('selection')}
            hi Search       guifg={hx('background')} guibg={hx('yellow')}
            hi IncSearch    guifg={hx('background')} guibg={hx('orange')}
            hi MatchParen   guifg={hx('red')} guibg={hx('selection')} gui=bold
            hi StatusLine   guifg={hx('foreground')} guibg={hx('current_line')}
            hi StatusLineNC guifg={hx('comment')} guibg={hx('current_line')}
            hi VertSplit    guifg={hx('bright_black')} guibg={hx('background')}
            hi Pmenu        guifg={hx('foreground')} guibg={hx('current_line')}
            hi PmenuSel     guifg={hx('background')} guibg={hx('red')}
            hi DiffAdd      guibg=#1e2e1a guifg={hx('green')}
            hi DiffDelete   guibg=#2e1a1c guifg={hx('red')}
            hi DiffChange   guibg=#2e2a1a guifg={hx('yellow')}
            hi DiffText     guibg=#3a3420 guifg={hx('yellow')} gui=bold
            hi Title        guifg={hx('red')}
            hi Directory    guifg={hx('sky')}
            hi NonText      guifg={hx('bright_black')}
            hi SpecialKey   guifg={hx('silver')}
            """
        ),
    )
    write(
        "themes/neovim/heartbox.lua",
        textwrap.dedent(
            f"""\
            -- Heartbox — Neovim (Lua colorscheme)
            -- place as colors/heartbox.lua or require and apply
            local c = {{
              bg = "{hx('background')}",
              bg_alt = "{hx('current_line')}",
              sel = "{hx('selection')}",
              fg = "{hx('foreground')}",
              comment = "{hx('comment')}",
              sky = "{hx('sky')}",
              green = "{hx('green')}",
              orange = "{hx('orange')}",
              pink = "{hx('pink')}",
              purple = "{hx('purple')}",
              red = "{hx('red')}",
              yellow = "{hx('yellow')}",
              silver = "{hx('silver')}",
              dim = "{hx('bright_black')}",
            }}

            vim.cmd("hi clear")
            if vim.fn.exists("syntax_on") then vim.cmd("syntax reset") end
            vim.o.background = "dark"
            vim.g.colors_name = "heartbox"

            local function hi(group, opts)
              vim.api.nvim_set_hl(0, group, opts)
            end

            hi("Normal", {{ fg = c.fg, bg = c.bg }})
            hi("Comment", {{ fg = c.comment, italic = true }})
            hi("Constant", {{ fg = c.purple }})
            hi("String", {{ fg = c.yellow }})
            hi("Number", {{ fg = c.orange }})
            hi("Identifier", {{ fg = c.fg }})
            hi("Function", {{ fg = c.sky }})
            hi("Statement", {{ fg = c.pink }})
            hi("Keyword", {{ fg = c.pink }})
            hi("Type", {{ fg = c.sky }})
            hi("Special", {{ fg = c.orange }})
            hi("Error", {{ fg = c.fg, bg = c.red }})
            hi("Todo", {{ fg = c.bg, bg = c.yellow, bold = true }})
            hi("LineNr", {{ fg = c.dim }})
            hi("CursorLine", {{ bg = c.bg_alt }})
            hi("CursorLineNr", {{ fg = c.silver, bold = true }})
            hi("Visual", {{ bg = c.sel }})
            hi("Search", {{ fg = c.bg, bg = c.yellow }})
            hi("IncSearch", {{ fg = c.bg, bg = c.orange }})
            hi("MatchParen", {{ fg = c.red, bg = c.sel, bold = true }})
            hi("StatusLine", {{ fg = c.fg, bg = c.bg_alt }})
            hi("Pmenu", {{ fg = c.fg, bg = c.bg_alt }})
            hi("PmenuSel", {{ fg = c.bg, bg = c.red }})
            hi("DiagnosticError", {{ fg = c.red }})
            hi("DiagnosticWarn", {{ fg = c.orange }})
            hi("DiagnosticInfo", {{ fg = c.sky }})
            hi("DiagnosticHint", {{ fg = c.silver }})
            hi("@punctuation", {{ fg = c.silver }})
            hi("@keyword", {{ fg = c.pink }})
            hi("@function", {{ fg = c.sky }})
            hi("@string", {{ fg = c.yellow }})
            hi("@variable", {{ fg = c.fg }})
            hi("@type", {{ fg = c.sky }})
            hi("@constant", {{ fg = c.purple }})
            hi("@tag", {{ fg = c.red }})
            hi("@attribute", {{ fg = c.green }})

            return c
            """
        ),
    )
    write(
        "themes/helix/heartbox.toml",
        textwrap.dedent(
            f"""\
            # Heartbox — Helix (~/.config/helix/themes/heartbox.toml)
            "ui.background" = {{ bg = "background" }}
            "ui.text" = "foreground"
            "ui.cursor" = {{ fg = "background", bg = "silver" }}
            "ui.selection" = {{ bg = "selection" }}
            "ui.linenr" = "bright_black"
            "ui.linenr.selected" = "silver"
            "ui.statusline" = {{ fg = "foreground", bg = "current_line" }}
            "ui.statusline.inactive" = {{ fg = "comment", bg = "current_line" }}
            "ui.menu" = {{ fg = "foreground", bg = "current_line" }}
            "ui.menu.selected" = {{ fg = "background", bg = "red" }}
            "comment" = {{ fg = "comment", modifiers = ["italic"] }}
            "keyword" = "pink"
            "function" = "sky"
            "string" = "yellow"
            "constant" = "purple"
            "type" = "sky"
            "variable" = "foreground"
            "number" = "orange"
            "punctuation" = "silver"
            "operator" = "pink"
            "error" = "red"
            "warning" = "orange"
            "info" = "sky"
            "hint" = "silver"
            "diff.plus" = "green"
            "diff.minus" = "red"
            "diff.delta" = "yellow"

            [palette]
            background = "{hx('background')}"
            current_line = "{hx('current_line')}"
            selection = "{hx('selection')}"
            foreground = "{hx('foreground')}"
            comment = "{hx('comment')}"
            sky = "{hx('sky')}"
            green = "{hx('green')}"
            orange = "{hx('orange')}"
            pink = "{hx('pink')}"
            purple = "{hx('purple')}"
            red = "{hx('red')}"
            yellow = "{hx('yellow')}"
            silver = "{hx('silver')}"
            bright_black = "{hx('bright_black')}"
            """
        ),
    )
    write(
        "themes/sublime/Heartbox.sublime-color-scheme",
        json.dumps(
            {
                "name": "Heartbox",
                "globals": {
                    "background": hx("background"),
                    "foreground": hx("foreground"),
                    "caret": hx("silver"),
                    "line_highlight": hx("current_line"),
                    "selection": hx("selection"),
                    "selection_border": hx("bright_black"),
                    "inactive_selection": hx("current_line"),
                    "find_highlight": hx("yellow"),
                    "find_highlight_foreground": hx("background"),
                    "brackets_options": "underline",
                    "brackets_foreground": hx("red"),
                    "tags_options": "stippled_underline",
                    "tags_foreground": hx("pink"),
                    "guide": hx("bright_black"),
                    "active_guide": hx("silver"),
                    "gutter": hx("background"),
                    "gutter_foreground": hx("bright_black"),
                },
                "rules": [
                    {"name": "Comment", "scope": "comment", "foreground": hx("comment"), "font_style": "italic"},
                    {"name": "String", "scope": "string", "foreground": hx("yellow")},
                    {"name": "Number", "scope": "constant.numeric", "foreground": hx("orange")},
                    {"name": "Keyword", "scope": "keyword", "foreground": hx("pink")},
                    {"name": "Storage", "scope": "storage", "foreground": hx("pink")},
                    {"name": "Function", "scope": "entity.name.function, support.function", "foreground": hx("sky")},
                    {"name": "Class", "scope": "entity.name.class, entity.name.type", "foreground": hx("green")},
                    {"name": "Constant", "scope": "constant", "foreground": hx("purple")},
                    {"name": "Variable", "scope": "variable", "foreground": hx("foreground")},
                    {"name": "Tag", "scope": "entity.name.tag", "foreground": hx("red")},
                    {"name": "Attribute", "scope": "entity.other.attribute-name", "foreground": hx("green")},
                    {"name": "Punctuation", "scope": "punctuation", "foreground": hx("silver")},
                    {"name": "Invalid", "scope": "invalid", "foreground": hx("foreground"), "background": hx("red")},
                ],
            },
            indent=2,
        )
        + "\n",
    )
    # VS Code / Cursor / VSCodium
    write(
        "themes/vscode/heartbox-color-theme.json",
        json.dumps(
            {
                "name": "Heartbox",
                "type": "dark",
                "colors": {
                    "editor.background": hx("background"),
                    "editor.foreground": hx("foreground"),
                    "editor.lineHighlightBackground": hx("current_line"),
                    "editor.selectionBackground": hx("selection"),
                    "editorCursor.foreground": hx("silver"),
                    "editorLineNumber.foreground": hx("bright_black"),
                    "editorLineNumber.activeForeground": hx("silver"),
                    "sideBar.background": U["panel"],
                    "sideBar.foreground": hx("foreground"),
                    "activityBar.background": hx("background"),
                    "activityBar.foreground": hx("silver"),
                    "statusBar.background": hx("current_line"),
                    "statusBar.foreground": hx("foreground"),
                    "statusBar.debuggingBackground": hx("red"),
                    "tab.activeBackground": hx("current_line"),
                    "tab.inactiveBackground": hx("background"),
                    "tab.activeForeground": hx("foreground"),
                    "tab.inactiveForeground": hx("comment"),
                    "tab.activeBorderTop": hx("red"),
                    "titleBar.activeBackground": hx("background"),
                    "titleBar.activeForeground": hx("foreground"),
                    "panel.background": U["panel"],
                    "panel.border": U["border"],
                    "focusBorder": hx("red"),
                    "button.background": hx("red"),
                    "button.foreground": hx("foreground"),
                    "list.activeSelectionBackground": hx("selection"),
                    "list.hoverBackground": hx("current_line"),
                    "list.highlightForeground": hx("sky"),
                    "terminal.background": hx("background"),
                    "terminal.foreground": hx("foreground"),
                    "terminal.ansiBlack": A["black"],
                    "terminal.ansiRed": A["red"],
                    "terminal.ansiGreen": A["green"],
                    "terminal.ansiYellow": A["yellow"],
                    "terminal.ansiBlue": A["blue"],
                    "terminal.ansiMagenta": A["magenta"],
                    "terminal.ansiCyan": A["cyan"],
                    "terminal.ansiWhite": A["white"],
                    "terminal.ansiBrightBlack": A["bright_black"],
                    "terminal.ansiBrightRed": A["bright_red"],
                    "terminal.ansiBrightGreen": A["bright_green"],
                    "terminal.ansiBrightYellow": A["bright_yellow"],
                    "terminal.ansiBrightBlue": A["bright_blue"],
                    "terminal.ansiBrightMagenta": A["bright_magenta"],
                    "terminal.ansiBrightCyan": A["bright_cyan"],
                    "terminal.ansiBrightWhite": A["bright_white"],
                    "gitDecoration.addedResourceForeground": hx("green"),
                    "gitDecoration.deletedResourceForeground": hx("red"),
                    "gitDecoration.modifiedResourceForeground": hx("yellow"),
                },
                "tokenColors": [
                    {"scope": ["comment"], "settings": {"foreground": hx("comment"), "fontStyle": "italic"}},
                    {"scope": ["string"], "settings": {"foreground": hx("yellow")}},
                    {"scope": ["constant.numeric"], "settings": {"foreground": hx("orange")}},
                    {"scope": ["keyword", "storage"], "settings": {"foreground": hx("pink")}},
                    {"scope": ["entity.name.function", "support.function"], "settings": {"foreground": hx("sky")}},
                    {"scope": ["entity.name.class", "entity.name.type", "support.type"], "settings": {"foreground": hx("green")}},
                    {"scope": ["variable"], "settings": {"foreground": hx("foreground")}},
                    {"scope": ["constant"], "settings": {"foreground": hx("purple")}},
                    {"scope": ["entity.name.tag"], "settings": {"foreground": hx("red")}},
                    {"scope": ["entity.other.attribute-name"], "settings": {"foreground": hx("green")}},
                    {"scope": ["punctuation"], "settings": {"foreground": hx("silver")}},
                    {"scope": ["invalid"], "settings": {"foreground": hx("red")}},
                ],
            },
            indent=2,
        )
        + "\n",
    )
    write(
        "themes/emacs/heartbox-theme.el",
        textwrap.dedent(
            f"""\
            ;;; heartbox-theme.el --- Heartbox color theme -*- lexical-binding: t; -*-
            (deftheme heartbox "Hand-tinted Technicolor dark theme.")
            (let ((bg "{hx('background')}")
                  (fg "{hx('foreground')}")
                  (cur "{hx('current_line')}")
                  (sel "{hx('selection')}")
                  (com "{hx('comment')}")
                  (sky "{hx('sky')}")
                  (grn "{hx('green')}")
                  (org "{hx('orange')}")
                  (pnk "{hx('pink')}")
                  (prp "{hx('purple')}")
                  (red "{hx('red')}")
                  (ylw "{hx('yellow')}")
                  (slv "{hx('silver')}")
                  (dim "{hx('bright_black')}"))
              (custom-theme-set-faces
               'heartbox
               `(default ((t (:background ,bg :foreground ,fg))))
               `(cursor ((t (:background ,slv))))
               `(region ((t (:background ,sel))))
               `(hl-line ((t (:background ,cur))))
               `(font-lock-comment-face ((t (:foreground ,com :slant italic))))
               `(font-lock-string-face ((t (:foreground ,ylw))))
               `(font-lock-keyword-face ((t (:foreground ,pnk))))
               `(font-lock-function-name-face ((t (:foreground ,sky))))
               `(font-lock-type-face ((t (:foreground ,sky))))
               `(font-lock-constant-face ((t (:foreground ,prp))))
               `(font-lock-variable-name-face ((t (:foreground ,fg))))
               `(font-lock-builtin-face ((t (:foreground ,prp))))
               `(font-lock-warning-face ((t (:foreground ,red :weight bold))))
               `(mode-line ((t (:background ,cur :foreground ,fg))))
               `(mode-line-inactive ((t (:background ,cur :foreground ,com))))
               `(line-number ((t (:foreground ,dim))))
               `(line-number-current-line ((t (:foreground ,slv :weight bold))))
               `(show-paren-match ((t (:foreground ,red :background ,sel :weight bold))))
               `(link ((t (:foreground ,sky :underline t))))
               `(error ((t (:foreground ,red))))
               `(warning ((t (:foreground ,org))))
               `(success ((t (:foreground ,grn))))))
            (provide-theme 'heartbox)
            ;;; heartbox-theme.el ends here
            """
        ),
    )
    write(
        "themes/zed/heartbox.json",
        json.dumps(
            {
                "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
                "name": "Heartbox",
                "author": "f00",
                "themes": [
                    {
                        "name": "Heartbox",
                        "appearance": "dark",
                        "style": {
                            "background": hx("background"),
                            "editor.background": hx("background"),
                            "editor.foreground": hx("foreground"),
                            "editor.gutter.background": hx("background"),
                            "editor.line_number": hx("bright_black"),
                            "editor.active_line_number": hx("silver"),
                            "editor.active_line.background": hx("current_line"),
                            "terminal.background": hx("background"),
                            "terminal.foreground": hx("foreground"),
                            "terminal.ansi.black": A["black"],
                            "terminal.ansi.red": A["red"],
                            "terminal.ansi.green": A["green"],
                            "terminal.ansi.yellow": A["yellow"],
                            "terminal.ansi.blue": A["blue"],
                            "terminal.ansi.magenta": A["magenta"],
                            "terminal.ansi.cyan": A["cyan"],
                            "terminal.ansi.white": A["white"],
                            "terminal.ansi.bright_black": A["bright_black"],
                            "terminal.ansi.bright_red": A["bright_red"],
                            "terminal.ansi.bright_green": A["bright_green"],
                            "terminal.ansi.bright_yellow": A["bright_yellow"],
                            "terminal.ansi.bright_blue": A["bright_blue"],
                            "terminal.ansi.bright_magenta": A["bright_magenta"],
                            "terminal.ansi.bright_cyan": A["bright_cyan"],
                            "terminal.ansi.bright_white": A["bright_white"],
                            "text": hx("foreground"),
                            "text.muted": hx("comment"),
                            "text.accent": hx("red"),
                            "border": U["border"],
                            "border.focused": hx("red"),
                            "element.background": U["panel"],
                            "element.hover": hx("current_line"),
                            "element.selected": hx("selection"),
                            "elevated_surface.background": U["panel"],
                            "surface.background": hx("background"),
                            "panel.background": U["panel"],
                            "status_bar.background": hx("current_line"),
                            "title_bar.background": hx("background"),
                            "tab_bar.background": hx("background"),
                            "tab.active_background": hx("current_line"),
                            "tab.inactive_background": hx("background"),
                            "players": [{"cursor": hx("silver"), "background": hx("silver"), "selection": hx("selection")}],
                            "syntax": {
                                "comment": {"color": hx("comment"), "font_style": "italic"},
                                "string": {"color": hx("yellow")},
                                "number": {"color": hx("orange")},
                                "keyword": {"color": hx("pink")},
                                "function": {"color": hx("sky")},
                                "type": {"color": hx("sky")},
                                "variable": {"color": hx("foreground")},
                                "constant": {"color": hx("purple")},
                                "punctuation": {"color": hx("silver")},
                                "tag": {"color": hx("red")},
                                "attribute": {"color": hx("green")},
                                "operator": {"color": hx("pink")},
                            },
                        },
                    }
                ],
            },
            indent=2,
        )
        + "\n",
    )
    write(
        "themes/nano/heartbox.nanorc",
        textwrap.dedent(
            f"""\
            ## Heartbox — nano
            set titlecolor bold,{hx('foreground')},{hx('current_line')}
            set statuscolor bold,{hx('foreground')},{hx('current_line')}
            set selectedcolor bold,{hx('foreground')},{hx('selection')}
            set numbercolor {hx('bright_black')},{hx('background')}
            set keycolor {hx('sky')},{hx('background')}
            set functioncolor {hx('pink')},{hx('background')}
            set scrollercolor {hx('silver')},{hx('background')}
            """
        ),
    )
    write(
        "themes/kakoune/heartbox.kak",
        textwrap.dedent(
            f"""\
            # Heartbox — Kakoune
            face global Default {hx('foreground')},{hx('background')}
            face global PrimarySelection {hx('foreground')},{hx('selection')}
            face global SecondarySelection {hx('foreground')},{hx('current_line')}
            face global PrimaryCursor {hx('background')},{hx('silver')}
            face global SecondaryCursor {hx('background')},{hx('comment')}
            face global LineNumbers {hx('bright_black')},{hx('background')}
            face global LineNumberCursor {hx('silver')},{hx('background')}+b
            face global MenuForeground {hx('background')},{hx('red')}
            face global MenuBackground {hx('foreground')},{hx('current_line')}
            face global Information {hx('foreground')},{hx('current_line')}
            face global Error {hx('foreground')},{hx('red')}
            face global StatusLine {hx('foreground')},{hx('current_line')}
            face global StatusLineMode {hx('background')},{hx('red')}
            face global MatchingChar {hx('red')},{hx('selection')}+b
            face global BufferPadding {hx('bright_black')},{hx('background')}
            face global comment {hx('comment')}+i
            face global string {hx('yellow')}
            face global keyword {hx('pink')}
            face global function {hx('sky')}
            face global type {hx('sky')}
            face global value {hx('orange')}
            face global meta {hx('purple')}
            face global operator {hx('pink')}
            face global attribute {hx('green')}
            """
        ),
    )


def gen_tools() -> None:
    write(
        "themes/bat/heartbox.tmTheme",
        textwrap.dedent(
            f"""\
            <?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
            <plist version="1.0">
            <dict>
              <key>name</key><string>Heartbox</string>
              <key>settings</key>
              <array>
                <dict>
                  <key>settings</key>
                  <dict>
                    <key>background</key><string>{hx('background')}</string>
                    <key>foreground</key><string>{hx('foreground')}</string>
                    <key>caret</key><string>{hx('silver')}</string>
                    <key>lineHighlight</key><string>{hx('current_line')}</string>
                    <key>selection</key><string>{hx('selection')}</string>
                  </dict>
                </dict>
                <dict><key>name</key><string>Comment</string><key>scope</key><string>comment</string><key>settings</key><dict><key>foreground</key><string>{hx('comment')}</string><key>fontStyle</key><string>italic</string></dict></dict>
                <dict><key>name</key><string>String</string><key>scope</key><string>string</string><key>settings</key><dict><key>foreground</key><string>{hx('yellow')}</string></dict></dict>
                <dict><key>name</key><string>Number</string><key>scope</key><string>constant.numeric</string><key>settings</key><dict><key>foreground</key><string>{hx('orange')}</string></dict></dict>
                <dict><key>name</key><string>Keyword</string><key>scope</key><string>keyword</string><key>settings</key><dict><key>foreground</key><string>{hx('pink')}</string></dict></dict>
                <dict><key>name</key><string>Function</string><key>scope</key><string>entity.name.function</string><key>settings</key><dict><key>foreground</key><string>{hx('sky')}</string></dict></dict>
                <dict><key>name</key><string>Type</string><key>scope</key><string>entity.name.type</string><key>settings</key><dict><key>foreground</key><string>{hx('green')}</string></dict></dict>
                <dict><key>name</key><string>Constant</string><key>scope</key><string>constant</string><key>settings</key><dict><key>foreground</key><string>{hx('purple')}</string></dict></dict>
                <dict><key>name</key><string>Punctuation</string><key>scope</key><string>punctuation</string><key>settings</key><dict><key>foreground</key><string>{hx('silver')}</string></dict></dict>
              </array>
              <key>uuid</key><string>a1b2c3d4-e5f6-7890-abcd-ef1234567890</string>
            </dict>
            </plist>
            """
        ),
    )
    write(
        "themes/fzf/heartbox.sh",
        textwrap.dedent(
            f"""\
            # Heartbox — fzf
            export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS \\
              --color=bg+:{hx('current_line')},bg:{hx('background')},spinner:{hx('sky')},hl:{hx('red')} \\
              --color=fg:{hx('foreground')},header:{hx('red')},info:{hx('silver')},pointer:{hx('pink')} \\
              --color=marker:{hx('green')},fg+:{hx('foreground')},prompt:{hx('pink')},hl+:{hx('yellow')} \\
              --color=border:{hx('bright_black')}"
            """
        ),
    )
    write(
        "themes/rofi/heartbox.rasi",
        textwrap.dedent(
            f"""\
            /* Heartbox — rofi */
            * {{
              background: {hx('background')};
              background-alt: {hx('current_line')};
              foreground: {hx('foreground')};
              selected: {hx('red')};
              active: {hx('sky')};
              urgent: {hx('orange')};
              silver: {hx('silver')};
            }}
            window {{
              background-color: @background;
              border: 2px;
              border-color: @silver;
            }}
            mainbox {{ background-color: @background; }}
            inputbar {{
              background-color: @background-alt;
              text-color: @foreground;
              padding: 8px;
            }}
            listview {{ background-color: @background; }}
            element {{
              background-color: @background;
              text-color: @foreground;
              padding: 6px;
            }}
            element selected {{
              background-color: @selected;
              text-color: @background;
            }}
            """
        ),
    )
    write(
        "themes/dunst/heartbox.dunstrc",
        textwrap.dedent(
            f"""\
            # Heartbox — dunst (fragment; merge into dunstrc)
            [global]
                frame_color = "{hx('silver')}"
                separator_color = frame

            [urgency_low]
                background = "{hx('background')}"
                foreground = "{hx('foreground')}"
                frame_color = "{hx('bright_black')}"

            [urgency_normal]
                background = "{hx('background')}"
                foreground = "{hx('foreground')}"
                frame_color = "{hx('silver')}"

            [urgency_critical]
                background = "{hx('background')}"
                foreground = "{hx('foreground')}"
                frame_color = "{hx('red')}"
            """
        ),
    )
    write(
        "themes/slack/heartbox.txt",
        f"{hx('background')},#22181B,{hx('selection')},{hx('red')},{hx('current_line')},{hx('foreground')},{hx('sky')},{hx('red')},{hx('background')},{hx('foreground')}\n",
    )
    write(
        "themes/starship/heartbox.toml",
        textwrap.dedent(
            f"""\
            # Heartbox — Starship palette fragment
            palette = "heartbox"

            [palettes.heartbox]
            bg = "{hx('background')}"
            fg = "{hx('foreground')}"
            red = "{hx('red')}"
            green = "{hx('green')}"
            yellow = "{hx('yellow')}"
            sky = "{hx('sky')}"
            pink = "{hx('pink')}"
            purple = "{hx('purple')}"
            orange = "{hx('orange')}"
            silver = "{hx('silver')}"
            comment = "{hx('comment')}"
            """
        ),
    )
    write(
        "themes/btop/heartbox.theme",
        textwrap.dedent(
            f"""\
            # Heartbox — btop
            theme[main_bg]="{hx('background')}"
            theme[main_fg]="{hx('foreground')}"
            theme[title]="{hx('red')}"
            theme[hi_fg]="{hx('sky')}"
            theme[selected_bg]="{hx('selection')}"
            theme[selected_fg]="{hx('foreground')}"
            theme[inactive_fg]="{hx('comment')}"
            theme[graph_text]="{hx('silver')}"
            theme[meter_bg]="{hx('current_line')}"
            theme[proc_misc]="{hx('orange')}"
            theme[cpu_box]="{hx('red')}"
            theme[mem_box]="{hx('sky')}"
            theme[net_box]="{hx('green')}"
            theme[proc_box]="{hx('pink')}"
            theme[div_line]="{hx('bright_black')}"
            theme[temp_start]="{hx('green')}"
            theme[temp_mid]="{hx('yellow')}"
            theme[temp_end]="{hx('red')}"
            theme[cpu_start]="{hx('green')}"
            theme[cpu_mid]="{hx('yellow')}"
            theme[cpu_end]="{hx('red')}"
            theme[free_start]="{hx('green')}"
            theme[free_mid]="{hx('sky')}"
            theme[free_end]="{hx('pink')}"
            theme[cached_start]="{hx('sky')}"
            theme[cached_mid]="{hx('purple')}"
            theme[cached_end]="{hx('pink')}"
            theme[available_start]="{hx('green')}"
            theme[available_mid]="{hx('yellow')}"
            theme[available_end]="{hx('orange')}"
            theme[used_start]="{hx('orange')}"
            theme[used_mid]="{hx('red')}"
            theme[used_end]="{hx('pink')}"
            theme[download_start]="{hx('sky')}"
            theme[download_mid]="{hx('green')}"
            theme[download_end]="{hx('yellow')}"
            theme[upload_start]="{hx('pink')}"
            theme[upload_mid]="{hx('purple')}"
            theme[upload_end]="{hx('red')}"
            theme[process_start]="{hx('sky')}"
            theme[process_mid]="{hx('pink')}"
            theme[process_end]="{hx('red')}"
            """
        ),
    )
    write(
        "themes/lsd/heartbox.yaml",
        textwrap.dedent(
            f"""\
            # Heartbox — lsd colors
            user: {hx('sky')[1:]}
            group: {hx('purple')[1:]}
            permission:
              read: {hx('green')[1:]}
              write: {hx('yellow')[1:]}
              exec: {hx('red')[1:]}
              exec-sticky: {hx('pink')[1:]}
              no-access: {hx('bright_black')[1:]}
            date:
              hour-old: {hx('silver')[1:]}
              day-old: {hx('comment')[1:]}
              older: {hx('bright_black')[1:]}
            size:
              none: {hx('bright_black')[1:]}
              small: {hx('green')[1:]}
              medium: {hx('yellow')[1:]}
              large: {hx('orange')[1:]}
            inode:
              valid: {hx('foreground')[1:]}
              invalid: {hx('red')[1:]}
            links:
              valid: {hx('sky')[1:]}
              invalid: {hx('red')[1:]}
            tree-edge: {hx('bright_black')[1:]}
            """
        ),
    )
    write(
        "themes/delta/heartbox.gitconfig",
        textwrap.dedent(
            f"""\
            # Heartbox — git-delta (include in ~/.gitconfig)
            [delta]
                syntax-theme = Heartbox
                plus-style = syntax "{hx('green')}"
                minus-style = syntax "{hx('red')}"
                plus-emph-style = syntax bold "{hx('green')}"
                minus-emph-style = syntax bold "{hx('red')}"
                line-numbers-left-style = "{hx('bright_black')}"
                line-numbers-right-style = "{hx('bright_black')}"
                line-numbers-minus-style = "{hx('red')}"
                line-numbers-plus-style = "{hx('green')}"
                line-numbers-zero-style = "{hx('comment')}"
                map-styles = bold purple => syntax "{hx('purple')}", bold blue => syntax "{hx('sky')}", bold cyan => syntax "{hx('sky')}", bold yellow => syntax "{hx('yellow')}"
            """
        ),
    )
    write(
        "themes/lazygit/heartbox.yml",
        textwrap.dedent(
            f"""\
            # Heartbox — lazygit
            gui:
              theme:
                activeBorderColor:
                  - "{hx('red')}"
                  - bold
                inactiveBorderColor:
                  - "{hx('bright_black')}"
                searchingActiveBorderColor:
                  - "{hx('yellow')}"
                  - bold
                optionsTextColor:
                  - "{hx('sky')}"
                selectedLineBgColor:
                  - "{hx('selection')}"
                inactiveViewSelectedLineBgColor:
                  - "{hx('current_line')}"
                cherryPickedCommitBgColor:
                  - "{hx('purple')}"
                cherryPickedCommitFgColor:
                  - "{hx('foreground')}"
                unstagedChangesColor:
                  - "{hx('red')}"
                defaultFgColor:
                  - "{hx('foreground')}"
            """
        ),
    )
    write(
        "themes/yazi/heartbox.toml",
        textwrap.dedent(
            f"""\
            # Heartbox — yazi (flavor fragment)
            [mgr]
            cwd = {{ fg = "{hx('sky')}" }}
            hovered = {{ fg = "{hx('foreground')}", bg = "{hx('selection')}" }}
            preview_hovered = {{ underline = true }}
            find_keyword = {{ fg = "{hx('yellow')}", bold = true }}
            find_position = {{ fg = "{hx('pink')}", bg = "reset", bold = true }}
            marker_copied = {{ fg = "{hx('green')}", bg = "{hx('green')}" }}
            marker_cut = {{ fg = "{hx('red')}", bg = "{hx('red')}" }}
            marker_selected = {{ fg = "{hx('yellow')}", bg = "{hx('yellow')}" }}
            count_copied = {{ fg = "{hx('background')}", bg = "{hx('green')}" }}
            count_cut = {{ fg = "{hx('background')}", bg = "{hx('red')}" }}
            count_selected = {{ fg = "{hx('background')}", bg = "{hx('yellow')}" }}
            border_symbol = "│"
            border_style = {{ fg = "{hx('silver')}" }}

            [status]
            separator_open = ""
            separator_close = ""
            separator_style = {{ fg = "{hx('current_line')}", bg = "{hx('current_line')}" }}
            mode_normal = {{ fg = "{hx('background')}", bg = "{hx('red')}", bold = true }}
            mode_select = {{ fg = "{hx('background')}", bg = "{hx('yellow')}", bold = true }}
            mode_unset = {{ fg = "{hx('background')}", bg = "{hx('pink')}", bold = true }}
            progress_label = {{ bold = true }}
            progress_normal = {{ fg = "{hx('sky')}", bg = "{hx('background')}" }}
            progress_error = {{ fg = "{hx('red')}", bg = "{hx('background')}" }}
            permissions_t = {{ fg = "{hx('green')}" }}
            permissions_r = {{ fg = "{hx('yellow')}" }}
            permissions_w = {{ fg = "{hx('red')}" }}
            permissions_x = {{ fg = "{hx('sky')}" }}
            permissions_s = {{ fg = "{hx('silver')}" }}
            """
        ),
    )
    write(
        "themes/k9s/heartbox.yaml",
        textwrap.dedent(
            f"""\
            # Heartbox — k9s skin
            k9s:
              body:
                fgColor: "{hx('foreground')}"
                bgColor: "{hx('background')}"
                logoColor: "{hx('red')}"
              prompt:
                fgColor: "{hx('foreground')}"
                bgColor: "{hx('background')}"
                suggestColor: "{hx('sky')}"
              info:
                fgColor: "{hx('pink')}"
                sectionColor: "{hx('foreground')}"
              dialog:
                fgColor: "{hx('foreground')}"
                bgColor: "{hx('background')}"
                buttonFgColor: "{hx('background')}"
                buttonBgColor: "{hx('red')}"
                buttonFocusFgColor: "{hx('background')}"
                buttonFocusBgColor: "{hx('sky')}"
                labelFgColor: "{hx('yellow')}"
                fieldFgColor: "{hx('foreground')}"
              frame:
                border:
                  fgColor: "{hx('silver')}"
                  focusColor: "{hx('red')}"
                menu:
                  fgColor: "{hx('foreground')}"
                  keyColor: "{hx('pink')}"
                  numKeyColor: "{hx('orange')}"
                crumbs:
                  fgColor: "{hx('background')}"
                  bgColor: "{hx('purple')}"
                  activeColor: "{hx('red')}"
                status:
                  newColor: "{hx('sky')}"
                  modifyColor: "{hx('yellow')}"
                  addColor: "{hx('green')}"
                  errorColor: "{hx('red')}"
                  highlightColor: "{hx('orange')}"
                  killColor: "{hx('pink')}"
                  completedColor: "{hx('comment')}"
                title:
                  fgColor: "{hx('foreground')}"
                  bgColor: "{hx('background')}"
                  highlightColor: "{hx('silver')}"
                  counterColor: "{hx('sky')}"
                  filterColor: "{hx('pink')}"
              views:
                table:
                  fgColor: "{hx('foreground')}"
                  bgColor: "{hx('background')}"
                  cursorFgColor: "{hx('background')}"
                  cursorBgColor: "{hx('selection')}"
                  header:
                    fgColor: "{hx('foreground')}"
                    bgColor: "{hx('background')}"
                    sorterColor: "{hx('silver')}"
                logs:
                  fgColor: "{hx('foreground')}"
                  bgColor: "{hx('background')}"
                  indicator:
                    fgColor: "{hx('foreground')}"
                    bgColor: "{hx('red')}"
            """
        ),
    )
    write(
        "themes/waybar/heartbox.css",
        textwrap.dedent(
            f"""\
            /* Heartbox — waybar */
            * {{
              border: none;
              font-family: monospace;
              font-size: 13px;
            }}
            window#waybar {{
              background: {hx('background')};
              color: {hx('foreground')};
              border-bottom: 2px solid {hx('silver')};
            }}
            #workspaces button {{
              padding: 0 8px;
              color: {hx('comment')};
              background: transparent;
            }}
            #workspaces button.active {{
              color: {hx('background')};
              background: {hx('red')};
            }}
            #clock, #battery, #cpu, #memory, #network, #pulseaudio, #tray {{
              padding: 0 10px;
              color: {hx('foreground')};
            }}
            #battery.warning {{ color: {hx('orange')}; }}
            #battery.critical {{ color: {hx('red')}; }}
            #network.disconnected {{ color: {hx('red')}; }}
            """
        ),
    )
    write(
        "themes/noctalia/heartbox.json",
        json.dumps(
            {
                "dark": {
                    "mPrimary": hx("red"),
                    "mOnPrimary": hx("foreground"),
                    "mSecondary": hx("sky"),
                    "mOnSecondary": hx("background"),
                    "mTertiary": hx("pink"),
                    "mOnTertiary": hx("background"),
                    "mError": hx("red"),
                    "mOnError": hx("foreground"),
                    "mSurface": hx("background"),
                    "mOnSurface": hx("foreground"),
                    "mSurfaceVariant": hx("current_line"),
                    "mOnSurfaceVariant": hx("comment"),
                    "mOutline": hx("silver"),
                    "mShadow": hx("background"),
                    "mHover": hx("selection"),
                    "mOnHover": hx("foreground"),
                    "terminal": {
                        "background": hx("background"),
                        "foreground": hx("foreground"),
                        "cursor": hx("silver"),
                        "cursorText": hx("background"),
                        "selectionBg": hx("selection"),
                        "selectionFg": hx("foreground"),
                        "normal": {
                            "black": A["black"],
                            "red": A["red"],
                            "green": A["green"],
                            "yellow": A["yellow"],
                            "blue": A["blue"],
                            "magenta": A["magenta"],
                            "cyan": A["cyan"],
                            "white": A["white"],
                        },
                        "bright": {
                            "black": A["bright_black"],
                            "red": A["bright_red"],
                            "green": A["bright_green"],
                            "yellow": A["bright_yellow"],
                            "blue": A["bright_blue"],
                            "magenta": A["bright_magenta"],
                            "cyan": A["bright_cyan"],
                            "white": A["bright_white"],
                        },
                    },
                },
                "light": {
                    "mPrimary": hx("red"),
                    "mOnPrimary": hx("bright_white"),
                    "mSecondary": hx("sky"),
                    "mOnSecondary": hx("background"),
                    "mTertiary": hx("pink"),
                    "mOnTertiary": hx("background"),
                    "mError": hx("red"),
                    "mOnError": hx("bright_white"),
                    "mSurface": hx("bright_white"),
                    "mOnSurface": hx("background"),
                    "mSurfaceVariant": hx("foreground"),
                    "mOnSurfaceVariant": hx("bright_black"),
                    "mOutline": hx("silver"),
                    "mShadow": hx("background"),
                    "mHover": hx("red"),
                    "mOnHover": hx("bright_white"),
                    "terminal": {
                        "background": hx("bright_white"),
                        "foreground": hx("background"),
                        "cursor": hx("silver"),
                        "cursorText": hx("bright_white"),
                        "selectionBg": hx("selection"),
                        "selectionFg": hx("foreground"),
                        "normal": {
                            "black": A["black"],
                            "red": A["red"],
                            "green": A["green"],
                            "yellow": A["yellow"],
                            "blue": A["blue"],
                            "magenta": A["magenta"],
                            "cyan": A["cyan"],
                            "white": A["white"],
                        },
                        "bright": {
                            "black": A["bright_black"],
                            "red": A["bright_red"],
                            "green": A["bright_green"],
                            "yellow": A["bright_yellow"],
                            "blue": A["bright_blue"],
                            "magenta": A["bright_magenta"],
                            "cyan": A["bright_cyan"],
                            "white": A["bright_white"],
                        },
                    },
                },
            },
            indent=2,
        )
        + "\n",
    )
    write(
        "themes/noctalia/README.md",
        textwrap.dedent(
            """\
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
            """
        ),
    )
    write(
        "themes/hyprland/heartbox.conf",
        textwrap.dedent(
            f"""\
            # Heartbox — Hyprland colors fragment
            general {{
                col.active_border = rgba({hx('red')[1:]}ee) rgba({hx('silver')[1:]}aa) 45deg
                col.inactive_border = rgba({hx('bright_black')[1:]}aa)
            }}
            decoration {{
                col.shadow = rgba({hx('background')[1:]}ee)
            }}
            misc {{
                background_color = rgb({hx('background')[1:]})
            }}
            """
        ),
    )
    write(
        "themes/i3/heartbox.i3",
        textwrap.dedent(
            f"""\
            # Heartbox — i3/sway colors
            # class                 border              bground             text                indicator           child_border
            client.focused          {hx('red')}     {hx('current_line')} {hx('foreground')} {hx('silver')}   {hx('red')}
            client.focused_inactive {hx('bright_black')} {hx('background')} {hx('comment')} {hx('bright_black')} {hx('bright_black')}
            client.unfocused        {hx('background')} {hx('background')} {hx('comment')} {hx('background')} {hx('background')}
            client.urgent           {hx('orange')}  {hx('orange')}     {hx('background')} {hx('orange')}  {hx('orange')}
            client.placeholder      {hx('background')} {hx('background')} {hx('foreground')} {hx('background')} {hx('background')}
            client.background       {hx('background')}

            bar {{
                colors {{
                    background {hx('background')}
                    statusline {hx('foreground')}
                    separator  {hx('bright_black')}
                    focused_workspace  {hx('red')} {hx('red')} {hx('background')}
                    active_workspace   {hx('selection')} {hx('current_line')} {hx('foreground')}
                    inactive_workspace {hx('background')} {hx('background')} {hx('comment')}
                    urgent_workspace   {hx('orange')} {hx('orange')} {hx('background')}
                }}
            }}
            """
        ),
    )
    write(
        "themes/polybar/heartbox.ini",
        textwrap.dedent(
            f"""\
            ; Heartbox — polybar
            [colors]
            background = {hx('background')}
            background-alt = {hx('current_line')}
            foreground = {hx('foreground')}
            primary = {hx('red')}
            secondary = {hx('sky')}
            alert = {hx('orange')}
            disabled = {hx('comment')}
            silver = {hx('silver')}
            """
        ),
    )
    write(
        "themes/zellij/heartbox.kdl",
        textwrap.dedent(
            f"""\
            // Heartbox — Zellij
            themes {{
                heartbox {{
                    fg "{hx('foreground')}"
                    bg "{hx('background')}"
                    black "{A['black']}"
                    red "{A['red']}"
                    green "{A['green']}"
                    yellow "{A['yellow']}"
                    blue "{A['blue']}"
                    magenta "{A['magenta']}"
                    cyan "{A['cyan']}"
                    white "{A['white']}"
                    orange "{hx('orange')}"
                }}
            }}
            """
        ),
    )
    write(
        "themes/fish/heartbox.fish",
        textwrap.dedent(
            f"""\
            # Heartbox — fish syntax
            set -U fish_color_normal {hx('foreground')[1:]}
            set -U fish_color_command {hx('sky')[1:]}
            set -U fish_color_keyword {hx('pink')[1:]}
            set -U fish_color_quote {hx('yellow')[1:]}
            set -U fish_color_redirection {hx('orange')[1:]}
            set -U fish_color_end {hx('pink')[1:]}
            set -U fish_color_error {hx('red')[1:]}
            set -U fish_color_param {hx('foreground')[1:]}
            set -U fish_color_comment {hx('comment')[1:]}
            set -U fish_color_selection --background={hx('selection')[1:]}
            set -U fish_color_operator {hx('pink')[1:]}
            set -U fish_color_escape {hx('orange')[1:]}
            set -U fish_color_autosuggestion {hx('bright_black')[1:]}
            set -U fish_color_cwd {hx('green')[1:]}
            set -U fish_color_cwd_root {hx('red')[1:]}
            set -U fish_color_user {hx('silver')[1:]}
            set -U fish_color_host {hx('sky')[1:]}
            set -U fish_pager_color_progress {hx('comment')[1:]}
            set -U fish_pager_color_prefix {hx('sky')[1:]}
            set -U fish_pager_color_completion {hx('foreground')[1:]}
            set -U fish_pager_color_description {hx('comment')[1:]}
            """
        ),
    )
    write(
        "themes/zsh-syntax/heartbox.zsh",
        textwrap.dedent(
            f"""\
            # Heartbox — zsh-syntax-highlighting
            typeset -A ZSH_HIGHLIGHT_STYLES
            ZSH_HIGHLIGHT_STYLES[default]='fg={hx('foreground')}'
            ZSH_HIGHLIGHT_STYLES[unknown-token]='fg={hx('red')}'
            ZSH_HIGHLIGHT_STYLES[reserved-word]='fg={hx('pink')}'
            ZSH_HIGHLIGHT_STYLES[alias]='fg={hx('sky')}'
            ZSH_HIGHLIGHT_STYLES[builtin]='fg={hx('sky')}'
            ZSH_HIGHLIGHT_STYLES[function]='fg={hx('sky')}'
            ZSH_HIGHLIGHT_STYLES[command]='fg={hx('green')}'
            ZSH_HIGHLIGHT_STYLES[precommand]='fg={hx('green')},underline'
            ZSH_HIGHLIGHT_STYLES[commandseparator]='fg={hx('pink')}'
            ZSH_HIGHLIGHT_STYLES[hashed-command]='fg={hx('green')}'
            ZSH_HIGHLIGHT_STYLES[path]='fg={hx('yellow')}'
            ZSH_HIGHLIGHT_STYLES[globbing]='fg={hx('orange')}'
            ZSH_HIGHLIGHT_STYLES[history-expansion]='fg={hx('purple')}'
            ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg={hx('orange')}'
            ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg={hx('orange')}'
            ZSH_HIGHLIGHT_STYLES[back-quoted-argument]='fg={hx('purple')}'
            ZSH_HIGHLIGHT_STYLES[single-quoted-argument]='fg={hx('yellow')}'
            ZSH_HIGHLIGHT_STYLES[double-quoted-argument]='fg={hx('yellow')}'
            ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]='fg={hx('orange')}'
            ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]='fg={hx('orange')}'
            ZSH_HIGHLIGHT_STYLES[assign]='fg={hx('foreground')}'
            ZSH_HIGHLIGHT_STYLES[redirection]='fg={hx('pink')}'
            ZSH_HIGHLIGHT_STYLES[comment]='fg={hx('comment')}'
            ZSH_HIGHLIGHT_STYLES[arg0]='fg={hx('green')}'
            """
        ),
    )
    write(
        "themes/bbcode/heartbox.txt",
        textwrap.dedent(
            f"""\
            Heartbox BBCode / forum swatches
            Background: {hx('background')}
            Foreground: {hx('foreground')}
            Red/Poppy:  {hx('red')}
            Sky:        {hx('sky')}
            Green:      {hx('green')}
            Yellow:     {hx('yellow')}
            Pink:       {hx('pink')}
            Purple:     {hx('purple')}
            Orange:     {hx('orange')}
            Silver:     {hx('silver')}
            Comment:    {hx('comment')}
            """
        ),
    )
    write(
        "themes/obsidian/heartbox.css",
        textwrap.dedent(
            f"""\
            /* Heartbox — Obsidian CSS snippet */
            .theme-dark {{
              --background-primary: {hx('background')};
              --background-secondary: {U['panel']};
              --background-modifier-border: {U['border']};
              --text-normal: {hx('foreground')};
              --text-muted: {hx('comment')};
              --text-faint: {hx('bright_black')};
              --text-accent: {hx('red')};
              --text-accent-hover: {hx('pink')};
              --interactive-accent: {hx('red')};
              --interactive-accent-hover: {hx('pink')};
              --code-normal: {hx('sky')};
              --code-comment: {hx('comment')};
              --code-function: {hx('sky')};
              --code-keyword: {hx('pink')};
              --code-string: {hx('yellow')};
              --code-value: {hx('orange')};
              --code-property: {hx('green')};
              --code-operator: {hx('pink')};
              --code-punctuation: {hx('silver')};
              --text-highlight-bg: {hx('selection')};
              --titlebar-background: {hx('background')};
              --tab-container-background: {hx('background')};
            }}
            """
        ),
    )
    write(
        "themes/chrome-devtools/heartbox.json",
        json.dumps(
            {
                "name": "Heartbox",
                "colors": {
                    "background": hx("background"),
                    "foreground": hx("foreground"),
                    "accent": hx("red"),
                    "secondary": hx("sky"),
                    "metal": hx("silver"),
                },
            },
            indent=2,
        )
        + "\n",
    )
    # JetBrains .icls is complex; provide scheme XML-ish simple + colors
    write(
        "themes/jetbrains/Heartbox.theme.json",
        json.dumps(
            {
                "name": "Heartbox",
                "dark": True,
                "author": "f00",
                "editorScheme": "Heartbox",
                "colors": {
                    "bg": hx("background"),
                    "fg": hx("foreground"),
                    "accent": hx("red"),
                    "metal": hx("silver"),
                    "sky": hx("sky"),
                    "poppy": hx("red"),
                },
                "ui": {
                    "*": {
                        "background": hx("background"),
                        "foreground": hx("foreground"),
                        "selectionBackground": hx("selection"),
                        "selectionForeground": hx("foreground"),
                        "borderColor": U["border"],
                        "disabledForeground": hx("comment"),
                    }
                },
            },
            indent=2,
        )
        + "\n",
    )
    write(
        "themes/gitui/heartbox.ron",
        textwrap.dedent(
            f"""\
            // Heartbox — gitui theme.ron
            (
              selected_tab: Some("{hx('red')}"),
              command_fg: Some("{hx('foreground')}"),
              selection_bg: Some("{hx('selection')}"),
              selection_fg: Some("{hx('foreground')}"),
              cmdbar_bg: Some("{hx('current_line')}"),
              cmdbar_extra_lines_bg: Some("{hx('current_line')}"),
              disabled_fg: Some("{hx('comment')}"),
              diff_line_add: Some("{hx('green')}"),
              diff_line_delete: Some("{hx('red')}"),
              diff_file_added: Some("{hx('green')}"),
              diff_file_removed: Some("{hx('red')}"),
              diff_file_moved: Some("{hx('purple')}"),
              diff_file_modified: Some("{hx('yellow')}"),
              commit_hash: Some("{hx('sky')}"),
              commit_time: Some("{hx('silver')}"),
              commit_author: Some("{hx('pink')}"),
              danger_fg: Some("{hx('red')}"),
              push_gauge_bg: Some("{hx('red')}"),
              push_gauge_fg: Some("{hx('background')}"),
              tag_fg: Some("{hx('yellow')}"),
              branch_fg: Some("{hx('sky')}"),
            )
            """
        ),
    )
    write(
        "themes/cava/heartbox",
        textwrap.dedent(
            f"""\
            ; Heartbox — cava
            [color]
            background = '{hx('background')}'
            foreground = '{hx('red')}'
            gradient = 1
            gradient_count = 4
            gradient_color_1 = '{hx('purple')}'
            gradient_color_2 = '{hx('pink')}'
            gradient_color_3 = '{hx('red')}'
            gradient_color_4 = '{hx('orange')}'
            """
        ),
    )


def gen_template() -> None:
    write(
        "themes/TEMPLATE.md",
        textwrap.dedent(
            f"""\
            # Port template — Heartbox

            Copy this checklist when adding an app under `themes/<app>/`.

            ## Palette (always use these hex values)

            | Token | Hex | Use |
            |---|---|---|
            | background | `{hx('background')}` | app chrome, editor bg |
            | current_line | `{hx('current_line')}` | line highlight, panels |
            | selection | `{hx('selection')}` | selection |
            | foreground | `{hx('foreground')}` | primary text |
            | comment | `{hx('comment')}` | comments, muted |
            | sky | `{hx('sky')}` | functions, types, links (verse blue) |
            | green | `{hx('green')}` | strings alt, classes, success |
            | orange | `{hx('orange')}` | numbers, warnings |
            | pink | `{hx('pink')}` | keywords |
            | purple | `{hx('purple')}` | constants, builtins |
            | red | `{hx('red')}` | poppy accent, errors, tags |
            | yellow | `{hx('yellow')}` | strings |
            | **silver** | `{hx('silver')}` | **cursor, chrome, punctuation — Kurt jacket metal** |

            ## Feel rules

            1. Dark, warm-black base — never cool pure navy like default IDE themes.
            2. Poppy red is the hero accent (active tab, focus ring, mode indicator).
            3. Silver is subtle: cursor and borders, not loud fills.
            4. Sky blue for “verse” calm tokens (functions/links); red for “chorus” emphasis.
            5. Prefer cream foreground `{hx('foreground')}` over pure white.

            ## Files

            - Prefer a single theme file + short install note in the app folder README if needed.
            - Regenerate machine ports: `python3 scripts/generate-themes.py` (do not hand-edit generated files).
            """
        ),
    )


def main() -> None:
    gen_canonical()
    gen_terminals()
    gen_editors()
    gen_tools()
    gen_template()
    # also dump palette copies under themes for discoverability
    write("themes/css/heartbox.css", (ROOT / "palette" / "heartbox.css").read_text())
    write("themes/json/heartbox.json", (ROOT / "palette" / "heartbox.json").read_text())
    write("themes/yaml/heartbox.yaml", (ROOT / "palette" / "heartbox.yaml").read_text())
    write("themes/toml/heartbox.toml", (ROOT / "palette" / "heartbox.toml").read_text())
    print("ok")


if __name__ == "__main__":
    main()
