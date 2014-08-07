#!/usr/bin/python

# import os
# import sys
import re

# get the args
# pass the args through the naming procedure
# assign the new name to the file


def renamer(file_name):

    # convert to lowercase
    print file_name.lower()
    
    # extract the file extension
    extension = re.findall(r'[\.]{1}[a-zA-Z]+', file_name)
    ext = extension[-1]
    print ext

    # get rid of nonword chars and whitespace
    sans_bad_chars = re.sub(r'[\W\s]', '', file_name)
    print sans_bad_chars

# test
file_name = "this\%\# is a Test-of the_PROCEDURE.yomama.txt"
renamer(file_name)
