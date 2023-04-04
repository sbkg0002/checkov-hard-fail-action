#!/bin/sh

echo "Installing ${1}"

echo "CURRENT DIRECTORY:"
ls -l /github/workspace/
echo "BARE RUN:"
checkov -d /github/workspace/
echo "RUNNING:"
python3 /main.py
