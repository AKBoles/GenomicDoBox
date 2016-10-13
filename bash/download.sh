#!/bin/bash

echo "starting"
#echo `./createopenrc.sh`
source /tmp/openrc
echo `swift download test_restore test.txt`
