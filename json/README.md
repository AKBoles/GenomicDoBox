JSON Code
=============

### Folder Contents ###

The following is an updated list of the python folder contents. The script is marked as "working", "in-progress, working", or "in-progress, not working".

1. prepareref.json : working

    > This script prepares the Reference Genome (placed in /home/cc/ref_genome/ - change location if needed) for use in DNA processing.

2. sample.json :  working

    > This script is a sample JSON pipeline file. It performs two calls on input paired-end read FASTQ files:
    >
    >    * bwa mem
    >
    >    * samtools view
