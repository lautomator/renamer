#!/usr/bin/python

# import os
# import sys
# import re

# get the args
# pass the args through the naming procedure
# assign the new name to the file


def renamer(file_args):
    print file_args.lower()
    print file_args.rstrip('')

# test
file_name = "this\%\# is a Test-of the_PROCEDURE.txt"
renamer(file_name)
