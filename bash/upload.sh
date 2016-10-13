#!/bin/bash
source /home/cc/openstack_docs/CH-818165-openrc.sh
echo `swift upload Genomics/post_processing $output1`
echo `swift upload Genomics/file_archive $input1`
echo `swift upload Genomics/file_archive $input2`
echo `swift delete Genomics/currently_processing $input1`
echo `swift delete Genomics/currently_processing $input2`
echo `rm exomecapstp* demo_*`
