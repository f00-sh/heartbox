-- Heartbox — Neovim (Lua colorscheme)
-- place as colors/heartbox.lua or require and apply
local c = {
  bg = "#090909",
  bg_alt = "#1C1617",
  sel = "#56180A",
  fg = "#EDE6DE",
  comment = "#8A7874",
  sky = "#2096EE",
  green = "#5A8A3A",
  orange = "#C45A20",
  pink = "#C47A72",
  purple = "#454B93",
  red = "#C50A1B",
  yellow = "#D4A83A",
  silver = "#B8BEC2",
  dim = "#3A3232",
}

vim.cmd("hi clear")
if vim.fn.exists("syntax_on") then vim.cmd("syntax reset") end
vim.o.background = "dark"
vim.g.colors_name = "heartbox"

local function hi(group, opts)
  vim.api.nvim_set_hl(0, group, opts)
end

hi("Normal", { fg = c.fg, bg = c.bg })
hi("Comment", { fg = c.comment, italic = true })
hi("Constant", { fg = c.purple })
hi("String", { fg = c.yellow })
hi("Number", { fg = c.orange })
hi("Identifier", { fg = c.fg })
hi("Function", { fg = c.sky })
hi("Statement", { fg = c.pink })
hi("Keyword", { fg = c.pink })
hi("Type", { fg = c.sky })
hi("Special", { fg = c.orange })
hi("Error", { fg = c.fg, bg = c.red })
hi("Todo", { fg = c.bg, bg = c.yellow, bold = true })
hi("LineNr", { fg = c.dim })
hi("CursorLine", { bg = c.bg_alt })
hi("CursorLineNr", { fg = c.silver, bold = true })
hi("Visual", { bg = c.sel })
hi("Search", { fg = c.bg, bg = c.yellow })
hi("IncSearch", { fg = c.bg, bg = c.orange })
hi("MatchParen", { fg = c.red, bg = c.sel, bold = true })
hi("StatusLine", { fg = c.fg, bg = c.bg_alt })
hi("Pmenu", { fg = c.fg, bg = c.bg_alt })
hi("PmenuSel", { fg = c.bg, bg = c.red })
hi("DiagnosticError", { fg = c.red })
hi("DiagnosticWarn", { fg = c.orange })
hi("DiagnosticInfo", { fg = c.sky })
hi("DiagnosticHint", { fg = c.silver })
hi("@punctuation", { fg = c.silver })
hi("@keyword", { fg = c.pink })
hi("@function", { fg = c.sky })
hi("@string", { fg = c.yellow })
hi("@variable", { fg = c.fg })
hi("@type", { fg = c.sky })
hi("@constant", { fg = c.purple })
hi("@tag", { fg = c.red })
hi("@attribute", { fg = c.green })

return c
