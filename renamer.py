#!/usr/bin/python

import os
import sys
import re
# import fileinput


def validate_targets(args):
    '''
        Check to ensure all targets arguments
        are files. Returns Boolean.
    '''
    index = 0
    while index < len(args) && os.path.isfile(args[index]):
        


def remove_paths(args):
    '''
        Gather the file name(s) from the
        command line argument(s) Returns
        a list with the file name(s).
    '''
    target_files = []

    # Remove the file paths from the args.
    for index in args:
        split_path = os.path.split(index)
        target_files.append(split_path[-1])

    return target_files


def rename_label(target):
    '''
        This takes any string and renames
        output so that the new string is 16
        chars or less, does not contain non-word
        chars except for '_', removes spaces,
        and converts to lowercase. Returns the
        renamed label.
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

    # Ensure the targets are all files


    # OUT
    print validate_target(args[0])


if __name__ == '__main__':
    main()
