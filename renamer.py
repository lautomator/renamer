#!/usr/bin/python

# import os
# import sys
import re

# get the args
# pass the args through the naming procedure
# assign the new name to the file


def renamer(file_name):

    renamed = []

    # convert to lowercase
    renamed.insert(0, file_name.lower())

    # find the file extension
    ext = re.findall(r'[\.]{1}[a-zA-Z]+', renamed[0])
    extension = ext[-1]

    print extension

    # get rid of nonword chars
    sans_bad_chars = re.sub(r'[^a-zA-Z 0-9_-]', '', file_name)
    print sans_bad_chars.lower()


# test
file_name = "this\%\# is a Test-of the_PROCEDURE.yomama.txt"
renamer(file_name)
