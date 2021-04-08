#!/bin/bash
# Sends a delete request to the URL passed as the first argument
curl -sL -X "DELETE" $1
