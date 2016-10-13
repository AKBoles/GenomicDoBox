#!/bin/bash
source /home/cc/openstack_docs/CH-818165-openrc.sh
echo `swift download Genomics/to_be_processed $input1`
echo `swift download Genomics/to_be_processed $input2`
echo `swift upload Genomics/currently_processing $input1`
echo `swift upload Genomics/currently_processing $input2`
echo `swift delete Genomics/to_be_processed $input1`
echo `swift delete Genomics/to_be_processed $input2`
