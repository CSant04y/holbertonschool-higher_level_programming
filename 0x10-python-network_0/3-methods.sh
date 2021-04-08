#!/bin/bash
# This diplays all http methods that a server will accept
curl -s -I -X OPTIONS 0.0.0.0:5000/route_4 | grep 'Allow:' | cut -d " " -f 2-
