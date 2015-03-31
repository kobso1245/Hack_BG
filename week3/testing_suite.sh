#!/bin/sh
while inotifywait $1; do
    clear
    python3 tester.py
done