#!/bin/bash
#get status code
curl  -sI "$1" | grep HTTP |  awk '{print $2}'
