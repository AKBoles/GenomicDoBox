#!/bin/bash
source /home/cc/openstack_docs/CH-818165-openrc.sh
echo `swift delete Genomics logfile.txt`
echo `swift upload Genomics logfile.txt`
