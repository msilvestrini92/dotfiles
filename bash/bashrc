#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Set to superior editing mode
set -o vi

# keybinds
bind -x '"\C-l":clear'

# ~~~~~~~~~~~~~~~ Environment Variables ~~~~~~~~~~~~~~~~~~~~~~~~

export VISUAL=vim
export EDITOR=vim

# directories
export REPOS="$HOME/repos"
export GITUSER="msilvestrini92"
export DOTFILES="$HOME/.dotfiles"

# okta-aws-cli env variables
export OKTA_AWSCLI_ORG_DOMAIN=okta.booking.com
export OKTA_AWSCLI_OIDC_CLIENT_ID=0oa69l79n9U8sx5if417
export OKTA_AWSCLI_AWS_ACCOUNT_FEDERATION_APP_ID=0oa1t1ub0fkS0kbyp416
export OKTA_AWSCLI_FORMAT=aws-credentials=true
export OKTA_AWSCLI_WRITE_AWS_CREDENTIALS=true
export OKTA_AWSCLI_OPEN_BROWSER=true

# aws-cli auto-completion
complete -C '/usr/local/bin/aws_completer' aws

# ~~~~~~~~~~~~~~~ Path configuration ~~~~~~~~~~~~~~~~~~~~~~~~

export PATH="/usr/local/bin/:$PATH"

# ~~~~~~~~~~~~~~~ History ~~~~~~~~~~~~~~~~~~~~~~~~

export HISTFILE=~/.histfile
export HISTSIZE=25000
export SAVEHIST=25000
export HISTCONTROL=ignorespace

# ~~~~~~~~~~~~~~~ Aliases ~~~~~~~~~~~~~~~~~~~~~~~~

# ls
alias ls='ls --color=auto'
alias ll='ls -la'
alias la='ls -lathr'

# finds all files recursively and sorts by last modification, ignore hidden files
alias lastmod='find . -type f -not -path "*/\.*" -exec ls -lrt {} +'

# BKNG netshell
alias netshell='ssh netshell.network.booking.com'
