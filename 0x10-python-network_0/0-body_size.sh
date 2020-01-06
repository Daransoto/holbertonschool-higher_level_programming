#!/bin/bash
# This script shows the size in bytes of the content.
if [ $# -ne 1 ]
then
	exit 1
fi
curl -so /dev/null "$1" -w "%{size_download}"
echo
