#!/bin/bash
#get body if status code is 200
(($(curl  -sI "$1" | grep HTTP |  awk '{print $2}') == "200")) && curl -s "$1"
