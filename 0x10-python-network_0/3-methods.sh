#!/bin/bash
# This diplays all http methods that a server will accept
curl -s -I -X $1 | grep 'Allow:' | cut -d " " -f 2-
