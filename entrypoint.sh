#!/bin/sh

echo "##################################"
echo "hard-fail checks: ${1}"
echo "path: ${2}"
echo "skip-checks: ${3}"
echo "##################################"
echo "running checkov:"
echo "##################################"
python3 /main.py --hard-fail-on ${1} --path ${2} --skip-checks ${3}
