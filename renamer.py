#!/usr/bin/python

import os
import sys
import re


def validate_targets(args):
    '''
        Check to ensure all targets arguments
        are files. Returns Boolean.
    '''
    valid_targets = []
    for arg in args:
        if os.path.isfile(arg):
            valid_targets.append(arg)

    return valid_targets


def remove_paths(targets):
    '''
        Gather the file name(s) from the
        command line argument(s) Returns
        a list with the file name(s).
    '''
    target_files = []

    # Remove the file paths from the targets.
    for index in targets:
        split_path = os.path.split(index)
        target_files.append(split_path[-1])

    return target_files


def preserve_paths(targets):
    '''
        Gather the file path(s) from the
        command line argument(s) Returns
        a list with the file path(s).
    '''
    target_paths = []

    # Remove the file names from the targets.
    for index in targets:
        split_path = os.path.split(index)
        target_paths.append(split_path[0])

    return target_paths


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

    return str(renamed[0])


def main():
    # IN
    # Get the command line arguments.
    # Ignore the name of the script.
    args = sys.argv[1:]
    # Ensure that args are valid files.
    targets = validate_targets(args)
    # Get the file names.
    target_files = remove_paths(targets)
    # Reserve the file paths
    target_paths = preserve_paths(targets)

    # OUT
    # Rename the target file labels
    renamed = []
    for target in target_files:
        renamed.append(rename_label(target))

    # Rename the actual files
    index = 0
    for new_name in renamed:
        os.rename(targets[index], target_paths[index] + '/' + new_name)
        index += 1


if __name__ == '__main__':
    main()
