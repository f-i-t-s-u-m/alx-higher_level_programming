#!/bin/bash
# curl json file
curl -s --data @$2 $1 --header "Content-Type: application/json" 
