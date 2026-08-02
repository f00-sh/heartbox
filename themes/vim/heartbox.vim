" Heartbox — Vim
" set colorscheme after placing in ~/.vim/colors/heartbox.vim
hi clear
if exists('syntax_on') | syntax reset | endif
let g:colors_name = 'heartbox'
set background=dark

hi Normal       guifg=#EDE6DE guibg=#0A1528 ctermfg=15 ctermbg=0
hi Comment      guifg=#6E7A8A gui=italic ctermfg=8
hi Constant     guifg=#5A4E9E ctermfg=13
hi String       guifg=#D4A838 ctermfg=11
hi Character    guifg=#D4A838
hi Number       guifg=#E06028 ctermfg=3
hi Boolean      guifg=#5A4E9E
hi Identifier   guifg=#EDE6DE ctermfg=15
hi Function     guifg=#1E8AE8 ctermfg=14
hi Statement    guifg=#D47A82 ctermfg=5
hi Keyword      guifg=#D47A82 ctermfg=5
hi PreProc      guifg=#D47A82
hi Type         guifg=#1E8AE8 ctermfg=12
hi Special      guifg=#E06028
hi Underlined   guifg=#1E8AE8 gui=underline
hi Error        guifg=#EDE6DE guibg=#E03818
hi Todo         guifg=#0A1528 guibg=#D4A838
hi LineNr       guifg=#2A3548 guibg=#0A1528
hi CursorLine   guibg=#142238 cterm=NONE
hi CursorLineNr guifg=#B8C0C8 gui=bold
hi Visual       guibg=#4E1A22
hi Search       guifg=#0A1528 guibg=#D4A838
hi IncSearch    guifg=#0A1528 guibg=#E06028
hi MatchParen   guifg=#E03818 guibg=#4E1A22 gui=bold
hi StatusLine   guifg=#EDE6DE guibg=#142238
hi StatusLineNC guifg=#6E7A8A guibg=#142238
hi VertSplit    guifg=#2A3548 guibg=#0A1528
hi Pmenu        guifg=#EDE6DE guibg=#142238
hi PmenuSel     guifg=#0A1528 guibg=#E03818
hi DiffAdd      guibg=#1e2e1a guifg=#3D9650
hi DiffDelete   guibg=#2e1a1c guifg=#E03818
hi DiffChange   guibg=#2e2a1a guifg=#D4A838
hi DiffText     guibg=#3a3420 guifg=#D4A838 gui=bold
hi Title        guifg=#E03818
hi Directory    guifg=#1E8AE8
hi NonText      guifg=#2A3548
hi SpecialKey   guifg=#B8C0C8
