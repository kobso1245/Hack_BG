#!/bin/sh
while inotifywait $1 || inotifywait panda_tester.py; do
    clear
    python3 panda_tester.py
done