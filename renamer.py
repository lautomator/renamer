#!/usr/bin/python

import os
import sys
import re
# import fileinput


def remove_paths(args):
    '''
        Gather the file names from the
        command line arguments.
    '''
    target_files = []

    # Remove the file paths from the args.
    for index in args:
        split_path = os.path.split(index)
        target_files.append(split_path[1])

    return target_files


def validate_target(target):
    ''' Check to ensure the target is a file. '''
    for filename in target:
        if os.path.isfile(target[filename]):
            return True


def rename_label(target):
    '''
        This takes any string and renames
        output so that the new string is 16
        chars or less, does not contain non-word
        chars except for '_' and '-', removes
        spaces, and converts to lowercase.
    '''
    renamed = []

    # Convert to lowercase.
    renamed.insert(0, target.lower())

    # Check for a file extension.
    if re.findall(r'[\.]{1}[a-zA-Z]+', renamed[0]):
        # Find the file extension.
        ext = re.findall(r'[\.]{1}[a-zA-Z]+', renamed[0])
        extension = ext[-1]
        # Anything longer than 5 chars is probably
        # not an extension; this can be adjusted.
        if len(extension) > 5:
            extension = ''
    else:
        extension = ''

    # Split the target to exclude the extension.
    sans_ext = renamed[0].replace(extension, '')
    renamed.insert(0, sans_ext)

    # Remove non-word chars and convert to lowercase.
    sans_bad_chars = re.sub(r'[^a-zA-Z 0-9_-]', '', renamed[0])
    renamed.insert(0, sans_bad_chars.lower())

    # Remove spaces.
    sans_spaces = re.sub(r'[ -]', '_', renamed[0])

    # Reduce to 16 chars, if necessary.
    if len(sans_spaces) > 16:
        reduced = sans_spaces[0:16]
    else:
        reduced = sans_spaces

    # If there is an extension, append it.
    final_name = reduced + extension

    # Add the label to the work list.
    renamed.insert(0, final_name)

    # Cleanup.
    del renamed[1:]

    return str(renamed[0])


def main():
    # IN
    # Get the command line arguments.
    # Ignore the name of the script.
    args = sys.argv[1:]

    # OUT
    print remove_paths(args)


if __name__ == '__main__':
    main()
