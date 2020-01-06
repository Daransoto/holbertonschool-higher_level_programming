#!/bin/bash
# This script sends a post request with data.
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
