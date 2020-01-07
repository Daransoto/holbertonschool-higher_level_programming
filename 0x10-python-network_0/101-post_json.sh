#!/bin/bash
# This script uses json data on the request.
curl -sH "Content-Type:Application/json" "$1" -d @"$2"
