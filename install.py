import os
import argparse


parser = argparse.ArgumentParser(description='Install the configuration files '
                                             'for some system utilities.')
parser.add_argument('-o', '--overwrite', dest='overwrite', action='store_true',
                    help='Overwrite the existing dotfiles in home directory.')

args = parser.parse_args()


def main():
    home = os.path.expanduser('~')
    print('Set user home directory to: {0}'.format(home))

    files = os.path.join(os.path.abspath('.'), 'default')
    print('Copying configuration files from: {0}'.format(files))

    for element in os.listdir(files):
        origin = os.path.join(files, element)
        link = os.path.join(home, '.' + element)

        # Create the symlink in home directory.
        try:
            os.symlink(origin, link)
            print('Created configuration file {0}'.format(link))
        except OSError:
            if args.overwrite:
                print('Removing symlink {0}'.format(link))
                os.remove(link)
                os.symlink(origin, link)
                print('\tCreated new configuration file {0}'.format(link))
            else:
                print('{0} exists. Skipping...'.format(link))


if __name__ == '__main__':
    main()
