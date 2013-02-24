import os


def main():
    home = os.path.expanduser('~')
    print('Set user home directory to: {0}'.format(home))

    files = os.path.join(os.path.abspath('.'), 'files')
    print('Copying configuration files from: {0}'.format(files))

    for element in os.listdir(files):
        origin = os.path.join(files, element)
        link = os.path.join(home, '.' + element)

        # Create the symlink in home directory.
        try:
            os.symlink(origin, link)
            print('Created configuration file {0}'.format(link))
        except OSError:
            pass


if __name__ == '__main__':
    main()
