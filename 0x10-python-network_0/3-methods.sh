#!/bin/bash
# show all options
curl -s -I -X OPTIONS "$1" | grep Allow: | awk 'sub($1 FS, "")'
