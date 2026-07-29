" Heartbox — Vim
" set colorscheme after placing in ~/.vim/colors/heartbox.vim
hi clear
if exists('syntax_on') | syntax reset | endif
let g:colors_name = 'heartbox'
set background=dark

hi Normal       guifg=#E8E4DC guibg=#191413 ctermfg=15 ctermbg=0
hi Comment      guifg=#7A656A gui=italic ctermfg=8
hi Constant     guifg=#6B4A58 ctermfg=13
hi String       guifg=#D4B84A ctermfg=11
hi Character    guifg=#D4B84A
hi Number       guifg=#EA5638 ctermfg=3
hi Boolean      guifg=#6B4A58
hi Identifier   guifg=#E8E4DC ctermfg=15
hi Function     guifg=#0888ED ctermfg=14
hi Statement    guifg=#C97A86 ctermfg=5
hi Keyword      guifg=#C97A86 ctermfg=5
hi PreProc      guifg=#C97A86
hi Type         guifg=#0888ED ctermfg=12
hi Special      guifg=#EA5638
hi Underlined   guifg=#0888ED gui=underline
hi Error        guifg=#E8E4DC guibg=#E5141A
hi Todo         guifg=#191413 guibg=#D4B84A
hi LineNr       guifg=#3D2F2D guibg=#191413
hi CursorLine   guibg=#3D2F2D cterm=NONE
hi CursorLineNr guifg=#C2C8CC gui=bold
hi Visual       guibg=#4B1006
hi Search       guifg=#191413 guibg=#D4B84A
hi IncSearch    guifg=#191413 guibg=#EA5638
hi MatchParen   guifg=#E5141A guibg=#4B1006 gui=bold
hi StatusLine   guifg=#E8E4DC guibg=#3D2F2D
hi StatusLineNC guifg=#7A656A guibg=#3D2F2D
hi VertSplit    guifg=#3D2F2D guibg=#191413
hi Pmenu        guifg=#E8E4DC guibg=#3D2F2D
hi PmenuSel     guifg=#191413 guibg=#E5141A
hi DiffAdd      guibg=#1e2e1a guifg=#5A8A42
hi DiffDelete   guibg=#2e1a1c guifg=#E5141A
hi DiffChange   guibg=#2e2a1a guifg=#D4B84A
hi DiffText     guibg=#3a3420 guifg=#D4B84A gui=bold
hi Title        guifg=#E5141A
hi Directory    guifg=#0888ED
hi NonText      guifg=#3D2F2D
hi SpecialKey   guifg=#C2C8CC
