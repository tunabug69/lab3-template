#!/usr/bin/env python3
# Author ID: rsrrajapaksha@mysenenca.ca

import subprocess

def free_space():
    result = subprocess.run(
        ["df", "-h", "/"],
        capture_output=True,
        text=True
    )

    free_space_value = result.stdout.splitlines()[1].split()[3]
    

    return free_space_value.strip()

if __name__ == '__main__':
    print(free_space())
