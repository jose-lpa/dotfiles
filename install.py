#!/usr/bin/env python

import os
import shutil
import argparse


parser = argparse.ArgumentParser(
    description='Install the configuration files for some system utilities.'
)
parser.add_argument(
    '-o', '--overwrite', dest='overwrite', action='store_true',
    help='Overwrite the existing dotfiles in home directory.'
)

args = parser.parse_args()


def main():
    home = os.path.expanduser('~')
    print('Set user home directory to: {0}'.format(home))

    files = os.path.join(os.path.abspath('.'), 'default')
    print('Copying configuration files from: {0}...\n'.format(files))

    for element in os.listdir(files):
        origin = os.path.join(files, element)
        link = os.path.join(home, '.' + element)

        # Create the symlink in home directory.
        try:
            os.symlink(origin, link)
            print('Linked configuration {0} to {1}'.format(origin, link))
        except OSError:
            if args.overwrite:
                print('Removing previous configuration {0}'.format(link))
                try:
                    os.remove(link)
                except OSError:
                    # Tried to remove a directory and failed. Go with `rmtree`.
                    shutil.rmtree(link)
                os.symlink(origin, link)
                print('\tLinked configuration {0} to {1}'.format(origin, link))
            else:
                print('{0} exists. Skipping...'.format(link))


if __name__ == '__main__':
    main()
