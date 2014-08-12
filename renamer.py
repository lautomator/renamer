#!/usr/bin/python

import os
import sys
import re


def validate_args(args):
    '''
        Check to ensure all there is at least one
        argument and that the arguments are valid
        files. Returns the valid targets only.
    '''
    errors = [
        'error: need to enter at least 1 argument.',
        'error: file does not exist.',
    ]

    usage = 'usage: python [this-script] <args>'

    valid_targets = []

    if len(args) == 0:
        return errors[0]

    else:
        for arg in args:
            if os.path.isfile(arg):
                valid_targets.append(arg)
            else:
                return errors[1]

        return valid_targets


def validate_targets(args):
    '''
        Check to ensure all targets arguments
        are files. Returns the valid targets only.
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
        Takes any string and renames output so
        that the new string is 16 chars or less,
        does not contain non-word chars except for '_',
        removes spaces, and converts to lowercase.
        Returns the renamed label.
    '''
    renamed = []
    # Maximum length of the renamed label.
    new_length = 16

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
    if len(sans_spaces) > new_length:
        reduced = sans_spaces[0:new_length]
    else:
        reduced = sans_spaces

    # If there is an extension, append it.
    final_name = reduced + extension

    # Add the label to the work list.
    renamed.insert(0, final_name)

    return str(renamed[0])


def renamer(targets, target_files, target_paths):
    ''' Perform the renaming of the actual files '''
    # Process the files for renaming.
    renamed_file = []
    index = 0
    for target in target_files:
        renamed_file.append(rename_label(target))

    for new_name in renamed_file:
        os.rename(targets[index], target_paths[index] + '/' + new_name)
        index += 1

    return renamed_file


def main():
    try:
        # Get the command line arguments.
        # Ignore the name of the script.
        args = sys.argv[1:]
        # Ensure that args are valid files.
        targets = validate_targets(args)
        # Get the file names.
        target_files = remove_paths(targets)
        # Reserve the file paths
        target_paths = preserve_paths(targets)
        # Rename the actual files.
        renamer(targets, target_files, target_paths)
    except Exception, e:
        raise e


if __name__ == '__main__':
    main()
