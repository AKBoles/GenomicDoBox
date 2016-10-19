#!/bin/bash

echo "starting"
source /tmp/openrc
echo `nova boot --flavor baremetal --image uthsc-computation --key-name akb-public-key --hint reservation=7356fdba-450e-4377-9980-22c3b5a88685 --nic net-id=915853fe-10c5-4dac-a402-ef1ebc53e427 --security-groups default test2`
