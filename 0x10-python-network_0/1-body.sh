#!/bin/bash
#get body if status code is 200

(($#)) && RES=$(curl  -s -I $1 | grep HTTP |  awk '{print $2}')
(($RES == 200)) && curl -s $1
