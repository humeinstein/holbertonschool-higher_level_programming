#!/bin/bash
#Bash script that takes in URL and shows all methods that will be accepted
curl -sI "$1" | grep Allow | cut -d " " -f 2-
