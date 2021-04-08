#!/bin/bash
# Takes in URL and sends request to that URL and gets the size of the response in bytes
curl -s $1 | wc -c
