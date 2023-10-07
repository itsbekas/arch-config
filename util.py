import argparse
import subprocess

def parse_args():
    parser = argparse.ArgumentParser(
        prog="installer.py",
        description=f"""Install packages and configs for Arch Linux.
        By default, the following packages will be installed:
        {PACKAGES}"""
    )
    parser.add_argument("--server", help="include server specific configs", action="store_true", default=False)
    parser.add_argument("--install", help="install packages without prompting", action="store_true", default=False)
    parser.add_argument("--exclude", help="exclude packages", action="extend", default=[])

    args = parser.parse_args()
    return args


def confirm_prompt(prompt, options = ["y", "n"], default="y"):
    """Prompt user for input, return True if input is y, False if input is n"""

    options = [x.capitalize() if x == default else x.lower() for x in options]
    default = default.lower()

    while True:
        user_input = input(f"{prompt} [{'/'.join(options)}]:", end=" ").lower()
        if user_input == "":
            user_input = default
        if user_input in options or user_input == default: # Default is capitalized in options
            return user_input == "y"
        else:
            print("Invalid input")


def log(message, level="INFO"):
    print(f"[{level}] {message}")


def run_cmd(cmd):
    """Run a command and return the output"""
    return subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode("utf-8")