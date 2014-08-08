#!/usr/bin/python

import os
import sys
import re

def renamer(filename):

    renamed = []

    # convert to lowercase
    renamed.insert(0, filename.lower())

    # find the file extension
    ext = re.findall(r'[\.]{1}[a-zA-Z]+', renamed[0])
    extension = ext[-1]

    # print the filename without the extension
    sans_ext = renamed[0].replace(extension, '')
    renamed.insert(0, sans_ext)

    # get rid of non-word chars and convert to lowercase
    sans_bad_chars = re.sub(r'[^a-zA-Z 0-9_-]', '', renamed[0])
    renamed.insert(0, sans_bad_chars.lower())

    # remove spaces
    sans_spaces = re.sub(r'[ -]', '_', renamed[0])

    # reduce to 16 chars
    if len(sans_spaces) > 16:
        reduced = sans_spaces[0:16]
    else:
        reduced = sans_spaces

    # add the file extension
    final_name = reduced + extension

    # add it into the list
    renamed.insert(0, final_name)

    # clean up
    del renamed[1:]

    return str(renamed[0])


def main(targets):

    for fin in targets:
        print renamer(fin)


targets = sys.argv[1:]

if __name__ == '__main__':
    main(targets)

'''
Traceback (most recent call last):
  File "../renamer.py", line 61, in <module>
    main(targets)
  File "../renamer.py", line 55, in main
    print renamer(fin)
  File "../renamer.py", line 21, in renamer
    extension = ext[-1]
IndexError: list index out of range
'''
