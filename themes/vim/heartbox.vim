" Heartbox — Vim
" set colorscheme after placing in ~/.vim/colors/heartbox.vim
hi clear
if exists('syntax_on') | syntax reset | endif
let g:colors_name = 'heartbox'
set background=dark

hi Normal       guifg=#EDE6DE guibg=#090909 ctermfg=15 ctermbg=0
hi Comment      guifg=#8A7874 gui=italic ctermfg=8
hi Constant     guifg=#454B93 ctermfg=13
hi String       guifg=#C49A3C ctermfg=11
hi Character    guifg=#C49A3C
hi Number       guifg=#C45A20 ctermfg=3
hi Boolean      guifg=#454B93
hi Identifier   guifg=#EDE6DE ctermfg=15
hi Function     guifg=#1E78C8 ctermfg=14
hi Statement    guifg=#C47A72 ctermfg=5
hi Keyword      guifg=#C47A72 ctermfg=5
hi PreProc      guifg=#C47A72
hi Type         guifg=#1E78C8 ctermfg=12
hi Special      guifg=#C45A20
hi Underlined   guifg=#1E78C8 gui=underline
hi Error        guifg=#EDE6DE guibg=#D44A18
hi Todo         guifg=#090909 guibg=#C49A3C
hi LineNr       guifg=#3A3232 guibg=#090909
hi CursorLine   guibg=#1C1617 cterm=NONE
hi CursorLineNr guifg=#B8BEC2 gui=bold
hi Visual       guibg=#56180A
hi Search       guifg=#090909 guibg=#C49A3C
hi IncSearch    guifg=#090909 guibg=#C45A20
hi MatchParen   guifg=#D44A18 guibg=#56180A gui=bold
hi StatusLine   guifg=#EDE6DE guibg=#1C1617
hi StatusLineNC guifg=#8A7874 guibg=#1C1617
hi VertSplit    guifg=#3A3232 guibg=#090909
hi Pmenu        guifg=#EDE6DE guibg=#1C1617
hi PmenuSel     guifg=#090909 guibg=#D44A18
hi DiffAdd      guibg=#1e2e1a guifg=#3D8A48
hi DiffDelete   guibg=#2e1a1c guifg=#D44A18
hi DiffChange   guibg=#2e2a1a guifg=#C49A3C
hi DiffText     guibg=#3a3420 guifg=#C49A3C gui=bold
hi Title        guifg=#D44A18
hi Directory    guifg=#1E78C8
hi NonText      guifg=#3A3232
hi SpecialKey   guifg=#B8BEC2
