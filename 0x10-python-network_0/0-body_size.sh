#!/bin/bash
# Bash script that takes in a URL, sends a request and display the body in byte.
curl -sI "$1" | grep 'Content-Length' | cut -d ' ' -f2
