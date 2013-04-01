#!/bin/bash

# This command simply adds a new user to an `htpasswd` file for nginx server.
# It uses openssl to generate the password hash which will be read by nginx
# to grant access to the user in basic authentication.
#
# This command is tested under Debian GNU/Linux systems, so maybe some changes
# will be need to operate in other OS.
#
# Usage: htpasswd-gen [USER] [PASSWORD]

if [ $# -lt 3 ]
then
    echo "No file specified. Defaulting to /etc/nginx/htpasswd"
    HTPASSWD_FILE=/etc/nginx/htpasswd
else
    HTPASSWD_FILE=$3
fi
printf "$1:$(openssl passwd -1 $2)\n" >> $HTPASSWD_FILE
