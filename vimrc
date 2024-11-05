syntax on

if has("autocmd")
  filetype plugin indent on

  autocmd BufReadPost *
   \ if line("'\"") > 0 && line("'\"") <= line("$") |
   \  exe "normal g`\"" |
   \ endif

endif

set cindent
set autoindent
set copyindent
set number
set smartindent
set expandtab
set tabstop=2
set shiftwidth=2
set bs=2
set hidden
set showmatch
set nocompatible
set laststatus=2
set encoding=utf-8
set t_Co=256

set ignorecase    " ignore case when searching
set smartcase     " ignore case if search pattern is all lowercase,
                  "    case-sensitive otherwise
set hlsearch
set incsearch
set title

set mouse=n

" change the mapleader from \ to ,
let mapleader=","
nmap <silent> ,/ :nohlsearch<CR>

let g:netrw_liststyle=3

colorscheme default

" use ,F to jump to tag in a vertical split
nnoremap ,F :let word=expand(""):vsp:wincmd w:exec("tag ". word)<CR>

" " use ,gf to go to file in a vertical split
nnoremap ,gf :vertical botright wincmd f<CR>

nmap <Leader>s :set spell!<CR>

let g:Powerline_symbols = "fancy"

nmap <Leader>b :FufBuffer<CR>
nmap <Leader>t :FufTag<CR>

if $VIM_CRONTAB == "true"
  set nobackup
  set nowritebackup
endif
