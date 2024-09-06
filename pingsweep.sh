#!/bin/bash

for ip in $(seq 1 254);do

ping -c 1 $1.$ip -w 1 | grep "64 bytes" | cut -d " " -f 4 | sed "s/.$//g"

done
