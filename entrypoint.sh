#!/bin/sh

echo "##################################"
echo "hard-fail checks: ${1}"
echo "path: ${2}"
echo "##################################"
echo "running checkov:"
echo "##################################"
python3 /main.py ${1} ${2}
