#!/bin/bash
# This script shows the size in bytes of the content.
curl -so /dev/null "$1" -w "%{size_download}"
