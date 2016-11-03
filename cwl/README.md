CWL Code
=============

### Folder Contents ###

The following is an updated list of the python folder contents. The script is marked as "working", "in-progress, working", or "in-progress, not working".

1. bwa_index.cwl : in-progress, not working

    > This script runs the command `bwa index` and accepts one user-input: a sorted reference genome. 
    > 
    > Currently, the script indexes the reference genome in the `/tmp/` directory. This is being worked on.
    >
    > To run, input the following from a command line:

    ~~~
    $ cwl-runner bwa_index.cwl --genome genome_sorted.fa
    ~~~

2. bwa_mem.cwl : in-progress, not working

    > This script runs the command `bwa mem` and accepts five user-inputs:
    >
    >    * Number of threads
    >
    >    * Reference genome
    >
    >    * FASTQ file one
    >
    >    * FASTQ file two
    >
    >    * Output file name
    > 
    > Currently, the script indexes the reference genome in the `/tmp/` directory. This is being worked on.
    >
    > To run, input the following from a command line:

    ~~~
    $ cwl-runner bwa_mem.cwl --numthreads \# --genome genome_sorted.fa --fastq_one input_R1.fastq --fastq_two inpute_R2.fastq --outfile out.sam
    ~~~

### Common Workflow Language Description ###

Link: http://www.commonwl.org/

Github Link: https://github.com/common-workflow-language/common-workflow-language

The Common Workflow Language (CWL) was created to be used to describe analysis workflows and make them portable across various envronments. CWL can work alongside JSON or YAML scripts to be even more powerful.

CWL was made to connect command line tools to create workflows, which is why it is a good choice for this application.

    Note that a few things are required in every CWL script:
       
        *cwlVersion: version of CWL to use
        *class: the class of the command to be called
        *baseCommand: the command to be called
        *inputs: any number of inputs; can be specified in JSON/YAML script or via command line arguments
        *outputs: if any outputs, they are listed here; if no output, outputs = []

The most basic of CWL scripts is as follows.

~~~
cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo
inputs:
  - id: message
    type: string
    inputBinding:
      position: 1
outputs: []
~~~

If the script was titled `helloworld.cwl`, it would be run using the following command line command:

~~~
cwl-runner helloworld.cwl --message "Hello World"
~~~

The output is: 

~~~
$ cwl-runner helloworld.cwl --message "Hello World!"
/usr/local/bin/cwl-runner 1.0.20161007181528
[job helloworld.cwl] /tmp/tmpr5e7V4$ echo \
    'Hello World!'
Hello World!
Final process status is success
{}
~~~

For further examples and a good introduction to CWL, please visit: http://www.commonwl.org/v1.0/UserGuide.html
