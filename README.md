My dotfiles setup
=================

Configuration files for some system stuff I often use.


Automated installation
----------------------
There is a Python script to automate the creation of symlinks. Just run it to
get done. If you want to overwrite the existing files in your home directory,
pass the option `-o` or `--overwrite`.

Attached submodules
-------------------

To install the attached submodules, just run this after cloning repository:

    git submodule init
    git submodule update
