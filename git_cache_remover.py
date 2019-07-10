#!/usr/bin/env python
import os


def ask():
    """This function removes a file if it was already staged before"""
    print("---\nNote: The directory inserted must be at the same level of this file")
    print("Press Ctrl+C to exit\n---")
    git_status = os.popen('git status')
    line = git_status.readline()
    while line:
        cnt = 1
        # print(line)
        if ('__pycache__' in line) or ('.pyc' in line):
            line = line.split("     ")
            directory = line[1]
            decition = input("Remove from cache {0}? (y/n):".format(directory))
            if decition=='y':
                output = os.popen('git rm --cached {0}'.format(directory)).read()
                print("------(removed)------")
            else:
                continue
        line = git_status.readline()
        cnt += 1
    print("(-finished-)")
    return

# Function call
ask()
