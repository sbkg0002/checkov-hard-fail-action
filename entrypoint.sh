#!/bin/sh

echo "Installing ${1}"

echo "CURRENT DIRECTORY:"
ls -l /github/workspace/

# pip install -U checkov==${1}

echo "RUNNING:"
python3 /main.py
