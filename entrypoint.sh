#!/bin/sh

echo "Hard-fail checks: ${1}"

echo "RUNNING:"
python3 /main.py ${1}
