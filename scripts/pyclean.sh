#!/bin/bash

# This command cleans all the .pyc files into a directory tree.
# If you don't provide a directory path, the command will remove all the .pyc
# files in the current directory.

if [ $# -eq 1 ]
    then
    DIRECTORY=$1
else
    DIRECTORY=.
fi
find $DIRECTORY -name *.pyc -delete
