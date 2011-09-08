import argparse
import subprocess
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def failed(message):
    return bcolors.FAIL + message + bcolors.ENDC 


def passed(message):
    return bcolors.OKGREEN + message + bcolors.ENDC


class Response(object):
    """A command's response"""

    def __init__(self, command=None, std_err=None, std_out=None, code=None):
        self.command = command
        self.std_err = std_err
        self.std_out = std_out
        self.returncode = code


def run(command):
    process = subprocess.Popen(command.split(" "),
        universal_newlines=True,
        env=os.environ,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=0,
    )

    out, err = process.communicate()
    code = process.returncode

    return Response(command=command, std_err=err, std_out=out, code=code)


def dry_run(command):
    print bcolors.HEADER + "Running {}...".format(command) + bcolors.ENDC


def attempt(command):
    """Try to run the command. Stop and print out the error if it fails"""
    print bcolors.HEADER + "Running {}...".format(command) + bcolors.ENDC
    resp = run(command)

    if not resp.returncode == 0:
        raise Exception(resp.std_err)


def main():
    usage = "Close pull requests in a git-svn friendly manner"
    parser = argparse.ArgumentParser(description=usage)
    parser.add_argument("command", type=str, choices=["merge"])
    parser.add_argument("branch", type=str, help="Branch to merge to master")
    parser.add_argument("-dr", "--dryrun", default=False, action="store_true")
    args = parser.parse_args()

    if args.dryrun:
        execute = dry_run
    else:
        execute = attempt
    
    commands = [
        "git fetch origin",
        "git checkout -b {0} origin/{0}".format(args.branch),
        "git rebase master",
        "git checkout master",
        "git merge {}".format(args.branch),
        "git push origin master",
        ]
    
    for command in commands:
        try:
            execute(command)
        except Exception as e:
            print failed(str(e))
            exit(1)
    
    print passed("Successfully merged {} into master".format(args.branch))
