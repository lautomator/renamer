#!/usr/bin/python

# import os
# import sys
import re

# get the args
# pass the args through the naming procedure
# assign the new name to the file


def renamer(file_args):
    # convert to lowercase
    print file_args.lower()
    
    # extract the file extension
    extension = re.match(r'[\.a-zA-Z]{1}', file_args)
    print dir(extension)
    ext = extension

    # get rid of nonword chars and whitespace
    sans_bad_chars = re.sub(r'[\W\s]', '', file_args)
    print sans_bad_chars

# test
file_name = "this\%\# is a Test-of the_PROCEDURE.txt"
renamer(file_name)
