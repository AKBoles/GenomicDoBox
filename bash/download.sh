#!/bin/bash

echo "starting"
source /tmp/openrc
echo `swift download test_restore test.txt`
