"""Wrapper process to prevent skipping of hard enforced checks"""

import json
import subprocess
import sys


def checkov(code_path: str) -> None:
    """Main process that checks for skipped checks against the list of hard fails"""
    checkov_process = subprocess.run(
        ["checkov", "-o", "cli", "-o", "json", "-d", code_path],
        universal_newlines=True,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    print(checkov_process.stdout)
    cli_output, json_output = checkov_process.stdout.split('--- OUTPUT DELIMITER ---')

    print(cli_output)
    checkov_results = json.loads(json_output)[0]

    if not (hard_fail_ids := sys.argv[1]):
        sys.exit(checkov_process.returncode)

    illegal_skip = False
    for skipped_check in checkov_results['results']['skipped_checks']:
        if skipped_check['check_id'] not in hard_fail_ids.split(','):
            continue
        print(f"The following check cannot be skipped:\n"
              f"\tCheck: {skipped_check['check_id']}: {skipped_check['check_name']}\n"
              f"\tFile: {skipped_check['file_path']}")
        illegal_skip = True

    if illegal_skip:
        print("\nThe terraform code that has been checked contains hard enforced checks,"
              " it is not allowed to skip hard enforced check: see: http://someniceconfluence doc")
        sys.exit(1)


if __name__ == '__main__':
    CODE_PATH = '/github/workspace/'
    if len(sys.argv) > 2:
        CODE_PATH += sys.argv[2]
    checkov(code_path=CODE_PATH)
