#!/bin/bash

# Requires a positional argument with the IP of the EVE-NG/PNETLAB server
# Creates a tmux session with a window per device specified in the 
# devices.csv file read as input
# Format of the csv has to be name,port

tmux new -s lab -d
#tmux rename-window -t lab "localhost"
tmux send-keys -t lab C-m

while IFS="," read -r name port
do
  tmux new-window -t lab -n "$name"
  tmux select-window -t "$name"
  tmux send-keys -t lab "telnet ${1} ${port}" C-m
  tmux send-keys -t lab C-m
done < <(tail -n +2 devices.csv)
