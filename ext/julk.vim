" julk.vim - Julk language plugin with filetype detection and syntax

" Auto-detect .jlk files
augroup julk_ftdetect
    autocmd!
    autocmd BufRead,BufNewFile *.jlk set filetype=julk
  augroup END
  
  " Define syntax only if filetype is julk
  augroup julk_syntax
    autocmd!
    autocmd FileType julk call s:define_julk_syntax()
  augroup END
  
  function! s:define_julk_syntax()
    " Clear any existing syntax
    syntax clear
  
    " Keywords
    syntax keyword julkKeyword def defmacro definex let eval alias claaf sync if else return use
  
    " Types
    syntax keyword julkType Result Module State
  
    " Constants
    syntax keyword julkConstant True False null
  
    " Operators
    syntax match julkOperator /\v(\+|\-|\*|\/|=|===|==|!=|<|>)/
  
    " Strings
    syntax region julkString start=/"/ skip=/\\"/ end=/"/
    syntax region julkString start=/'/ skip=/\\'/ end=/'/
  
    " Comments (C-style or C++-style)
    syntax match julkComment /\/\/.*/
  
    " Function & macro definitions
    syntax match julkFunction /\vdef\s+\zs\w+/
    syntax match julkMacro /\vdefmacro\s+\zs\w+/
  
    " Claaf blocks
    syntax match julkClaaf /\vclaaf\s+\w+/
  
    " Highlight groups
    hi def link julkKeyword Keyword
    hi def link julkType Type
    hi def link julkConstant Constant
    hi def link julkOperator Operator
    hi def link julkString String
    hi def link julkComment Comment
    hi def link julkFunction Function
    hi def link julkMacro Macro
    hi def link julkClaaf Structure
  endfunction
  