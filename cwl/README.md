CWL Code
=============

### Folder Contents ###

The following is an updated list of the python folder contents. The script is marked as "working", "in-progress, working", or "in-progress, not working".

1. bwa_index.cwl : in-progress

    > This script runs the command "bwa index" and accepts one user-input: a sorted reference genome. 
    > 
    > Currently, the script indexes the reference genome in the "/tmp/" directory. This is being worked on.
    >
    > To run, input the following from a command line:

    ~~~
    $ cwl-runner bwa_index.cwl --genome genome_sorted.fa
    ~~~

2. bwa_mem.cwl : in-progress

    > This script runs the command "bwa mem" and accepts five user-inputs:
    >
    >    * Number of threads
    >
    >    * reference genome
    >
    >    * FASTQ file one
    >
    >    * FASTQ file two
    >
    >    * Output file name
    > 
    > Currently, the script indexes the reference genome in the "/tmp/" directory. This is being worked on.
    >
    > To run, input the following from a command line:

    ~~~
    $ cwl-runner bwa_mem.cwl --numthreads \# --genome genome_sorted.fa --fastq_one input_R1.fastq --fastq_two inpute_R2.fastq --outfile     out.sam
~~~

### Common Workflow Language Description ###

Link: http://www.commonwl.org/
