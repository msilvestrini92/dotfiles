#!/bin/sh

# Current timestamp
date=$(date +%Y-%m-%d)

# Kill any running tmux sessions
pkill -9 tmux

# Kill any running ssh-agent, restart and renew ssh keys
pkill -9 ssh-agent
ssh-agent
ssh -A ssh.booking.com

# Move old logs to the archived directory
mv ~/Documents/work/Logs/* ~/Documents/work/Logs/archived/ >/dev/null 2>&1 &

# Set up tmux, create new session, select first pane and cd into repos dir
tmux new -s work -d
tmux rename-window -t work "localhost_${date}"
tmux send-keys -t work C-m

# Connect to netshell
tmux new-window -t work -n "netshell"
tmux select-window -t "netshell"
tmux pipe-pane -t work "exec cat >>${HOME}/Documents/work/Logs/'#W-tmux.log'" \; display-message "Started logging to ${HOME}/Documents/work/Logs/#W-tmux.log"
tmux send-keys -t work "ssh netshell.network.booking.com" C-m
tmux send-keys -t work C-m

# Select the localhost window and attach to the tmux session
tmux select-window -t "localhost_${date}"
tmux attach -t work
