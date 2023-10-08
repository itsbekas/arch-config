# Check if zsh is installed

import os
import sys
import subprocess
import argparse

from packages import *
from util import *

#import cfg

PACKAGES = [] # TODO: Package graph

FLAGS = parse_args()

def install():
    for pkg in PACKAGES:
        if not pkg.exists and not FLAGS.install:
            install = confirm_prompt(f"{pkg} is not installed, do you wish to install?")
            if install:
                log(f"Installing {pkg.name}...")
                pkg.install()
            else:
                log(f"Skipping {pkg.name}...")
        else:
            log(f"{pkg} is installed. Skipping...")


def check_packages():
    for pkg in PACKAGES:
        if not pkg.exists:
            log(f"Package {pkg.name} is not installed, but is not implemented. Please implement it and try again.", "ERROR")
            sys.exit(1)


if __name__ == "__main__":
    pass
