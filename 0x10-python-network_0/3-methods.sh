#!/bin/bash
# This diplays all http methods that a server will accept
curl -s -I $1 -X OPTIONS | grep 'Allow:' | cut -d " " -f 2-
