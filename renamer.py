#!/usr/bin/python

import os
import sys
import re
import fileinput

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


def validate_target(target):

    if os.path.isfile(targets[0]):
        valid_targets = targets
        return valid_targets
    else:
        return 'not a file'


def main(target):
    
    pass


# ignore the name of the script
path_to_file = sys.argv[1]
split_path = os.path.split(path_to_file)
target = split_path[1]

#if __name__ == '__main__':
#    main(target)

print renamer(target)
