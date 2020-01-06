#!/bin/bash
#send reuqest to url then show size of body
curl -sI $1 | grep Content-Length | cut -d" " -f2
