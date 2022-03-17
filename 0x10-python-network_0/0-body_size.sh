#!/bin/bash
# get response content length	
(($#)) && curl -s -I $1 | grep Content-Length | awk '{print $2}'
