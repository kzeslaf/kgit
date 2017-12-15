#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
kgit.py

Decorator for git command allowing for simultaneous operations on many repos.

Commands outside repository directory:
    - pull
    - status
"""


import os
import sys


#
# Constats
#


RES_OK = 0
RES_ERROR = 1


#
# Utils Functions
#


def list_git_repos(path):
    """..."""
    result = []
    join = os.path.join

    for i in os.listdir(path):
        if os.path.exists(join(join(path, i), '.git')):
            result.append(i)

    return result


def is_git_repo(path):
    """..."""
    abspath = os.path.abspath
    exists = os.path.exists
    join = os.path.join

    while path != '' and path != '/' and path[1:] != ":\\":
        if exists(join(path, '.git')):
            return True
        path = abspath(join(path, '..'))
    return False


#
# Command Functions
#


def git_pull(paths):
    """..."""
    for i in paths:
        res = os.system(
            '( echo Directory: [{0}]; cd {0}; git pull )'.format(i))
        if res != 0:
            return res
    return 0


def git_status(paths):
    """..."""
    for i in paths:
        res = os.system(
            '( echo Directory: [{0}]; cd {0}; git status )'.format(i))
        if res != 0:
            return res
    return 0


#
#
#


def main():
    """..."""
    cwd = os.getcwd()

    functions = [
        (['pull'], git_pull),
        (['status', 'stat'], git_status),
    ]

    if is_git_repo(cwd):
        return os.system('git ' + ' '.join(sys.argv[1:]))

    else:
        for i in functions:
            if sys.argv[1] in i[0]:
                return i[1](sorted(list_git_repos(cwd)))

    raise Exception('Unknown command: {}'.format(sys.argv[1:]))


#
# Main
#


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print exc
        sys.exit(RES_ERROR)
