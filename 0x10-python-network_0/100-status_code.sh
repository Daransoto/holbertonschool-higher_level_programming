#!/bin/bash
# This script shows the status code of the response.
curl -so /dev/null "$1" -w "%{http_code}"
