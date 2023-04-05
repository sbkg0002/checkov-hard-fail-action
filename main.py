"""Wrapper process to prevent skipping of hard enforced checks"""

import json
import subprocess
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-hf", "--hard-fail-on", dest='hard_fail_on', help="comma seperated list of hard-fail-on checks.")
parser.add_argument("-sc", "--skip-checks", dest='skip_checks',
                    help="comma seperated list of checks to skip.", default='')
parser.add_argument("-p", "--path", help="path to checks files in.")
args = parser.parse_args()


def checkov(code_path: str) -> None:
    """Main process that checks for skipped checks against the list of hard fails"""
    checkov_process = subprocess.run(
        ["checkov", "-o", "cli", "-o", "json", "-d", code_path,
         "--download-external-modules", "True", "--framework", "terraform", "--skip-check", args.skip_checks],
        universal_newlines=True,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    cli_output, json_output = checkov_process.stdout.split('--- OUTPUT DELIMITER ---')

    print(cli_output)
    checkov_results = json.loads(json_output)

    if not (hard_fail_ids := args.hard_fail_on):
        sys.exit(checkov_process.returncode)

    illegal_skip = False
    if checkov_results['summary'].get('skipped') > 0:
        for skipped_check in checkov_results['results'].get('skipped_checks'):
            if skipped_check['check_id'] not in hard_fail_ids.split(','):
                continue
            print(f"The following check cannot be skipped:\n"
                  f"\tCheck: {skipped_check['check_id']}: {skipped_check['check_name']}\n"
                  f"\tFile: {skipped_check['file_path']}")
            illegal_skip = True

        if illegal_skip:
            print("\n### MANDATORY CHECK(S) FAILED ###"
                  "\nThe terraform code that has been checked contains hard enforced checks,"
                  " it is not allowed to skip hard enforced checks. For more information see: "
                  "\n\thttps://devolksbank.atlassian.net/wiki/spaces/CEP/pages/49762271982/Terraform+code+analysis")
            sys.exit(1)


if __name__ == '__main__':
    CODE_PATH = f'/github/workspace/{args.path}'
    # CODE_PATH = f'/github/workspace/{args.path}'
    CODE_PATH = '.'
    checkov(code_path=CODE_PATH)
