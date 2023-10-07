# Check if zsh is installed

import os
import sys
import subprocess
import argparse

import packages
from util import *

#import cfg

PACKAGES = [getattr(packages, package_name)() for package_name in package_names]



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
        

if __name__ == "__main__":
    install()
