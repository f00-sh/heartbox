" Heartbox — Vim
" set colorscheme after placing in ~/.vim/colors/heartbox.vim
hi clear
if exists('syntax_on') | syntax reset | endif
let g:colors_name = 'heartbox'
set background=dark

hi Normal       guifg=#F4EBE0 guibg=#1A1214 ctermfg=15 ctermbg=0
hi Comment      guifg=#8A6E78 gui=italic ctermfg=8
hi Constant     guifg=#7A5A9E ctermfg=13
hi String       guifg=#E8D45A ctermfg=11
hi Character    guifg=#E8D45A
hi Number       guifg=#E8924A ctermfg=3
hi Boolean      guifg=#7A5A9E
hi Identifier   guifg=#F4EBE0 ctermfg=15
hi Function     guifg=#5EC8E8 ctermfg=14
hi Statement    guifg=#E86A9A ctermfg=5
hi Keyword      guifg=#E86A9A ctermfg=5
hi PreProc      guifg=#E86A9A
hi Type         guifg=#5EC8E8 ctermfg=12
hi Special      guifg=#E8924A
hi Underlined   guifg=#5EC8E8 gui=underline
hi Error        guifg=#F4EBE0 guibg=#E02030
hi Todo         guifg=#1A1214 guibg=#E8D45A
hi LineNr       guifg=#4A3A3E guibg=#1A1214
hi CursorLine   guibg=#2C1F22 cterm=NONE
hi CursorLineNr guifg=#B8C0C8 gui=bold
hi Visual       guibg=#3A2428
hi Search       guifg=#1A1214 guibg=#E8D45A
hi IncSearch    guifg=#1A1214 guibg=#E8924A
hi MatchParen   guifg=#E02030 guibg=#3A2428 gui=bold
hi StatusLine   guifg=#F4EBE0 guibg=#2C1F22
hi StatusLineNC guifg=#8A6E78 guibg=#2C1F22
hi VertSplit    guifg=#4A3A3E guibg=#1A1214
hi Pmenu        guifg=#F4EBE0 guibg=#2C1F22
hi PmenuSel     guifg=#1A1214 guibg=#E02030
hi DiffAdd      guibg=#1e2e1a guifg=#5FBF4A
hi DiffDelete   guibg=#2e1a1c guifg=#E02030
hi DiffChange   guibg=#2e2a1a guifg=#E8D45A
hi DiffText     guibg=#3a3420 guifg=#E8D45A gui=bold
hi Title        guifg=#E02030
hi Directory    guifg=#5EC8E8
hi NonText      guifg=#4A3A3E
hi SpecialKey   guifg=#B8C0C8
