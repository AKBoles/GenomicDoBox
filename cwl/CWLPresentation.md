
Common Workflow Language (CWL)
==============================

![CWL](http://www.commonwl.org/CWL-Logo-Header.png)

In bioinformatics, a majority of the data processing procedures are defined in Command Line based Pipelines. Historically, users would either have to input each command on the terminal by hand or use something similar to Matlab or JSON scripts to perform a pre-defined list of commands.

Problems with this include human error in typing the (sometimes) long, complicated commands into the terminal. Pre-defined pipelines fix this slightly but it is not a trivial task to change certain parameters in a large pipeline - simply finding the correct command in a large list can be time consuming.

Benefits of CWL:
----------------

The Common Workflow Language (CWL) uses JSON and YAML scripts, described below, to simplify the workflow description process. Primarily, CWL separates the tool description with the specific user-input arguments. In this way, describing a pipeline is simplified and altering it at a later time is also simplified. This will be seen in the implementation below.

JSON / YAML Introduction:
-------------------------

    JSON (JavaScript Object Notation) is a format that uses human-readable text to transmit objects via attribute-value pairs.
  
    Language-independent format, derives from JavaScript
  
    Example script shown below:
  
~~~json
  {
    "firstName":  "Andrew",
    "lastName":  "Boles",
    "age":  25,
    },
    "phoneNumbers": [
      {
        "type":  "cell",
        "number":  "867-5309"
      }
    ],
  }
~~~
    
    As can be seen, this is a simple key-value pair list.
   
    Similarly, YAML is a human-readable data serialization language. JSON and YAML are similar because YAML is a superset of JSON.
   
    Main difference being that JSON uses brackets and YAML uses indentation. The same script can be seen below in YAML:
   
   ~~~yaml
     firstName: "Andrew"
     lastName: "Boles"
     age: 25
     phoneNumbers:
       - type: "cell"
       - number: "867-5309"
   ~~~

    So both are used to transmit data and defining values - both of which are desired in a data processing workflow!
   
CWL in Action
-------------

    To first see the power of CWL before moving on to bioinformatics applications, the following is how the HelloWorld script in CWL would be written, two different ways.
   
    Method Number 1: using the command line to define the user-input arguments
   
~~~yaml
cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo
inputs:
  -id: message
    type: string
    inputBinding:
      position: 1
outputs: []
~~~
    
    This would be run in the command line by using the following:


```python
%%bash

cwl-runner HelloWorld.cwl --message "Hello World!"
```

    {}


    /usr/local/bin/cwl-runner 1.0.20161107145355
    [job HelloWorld.cwl] /tmp/tmphOJaSq$ echo \
        'Hello World!'
    Hello World!
    Final process status is success


    Method Number 1: using a YAML script to define the user-input arguments. First, there is a slight change to the CWL script as seen below. Then the `message` is given by the YAML script below the CWL script.
   
~~~yaml
cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo
inputs:
  message:
    type: string
    inputBinding:
      position: 1
outputs: []
~~~

~~~yaml
message: Hello World!
~~~
    
    This would be run in the command line by using the following:


```python
%%bash

cwl-runner hello.cwl hello-job.yml
```

    {}


    /usr/local/bin/cwl-runner 1.0.20161107145355
    [job hello.cwl] /tmp/tmpQdzlRT$ echo \
        'Hello World!'
    Hello World!
    Final process status is success


CWL for Bioinformatics
----------------------

![DNA](http://cdn.theatlantic.com/static/mt/assets/science/shutterstock_34693498%20copy.jpg)

### Preparing Reference Genome ###

##### A first example #####

    A first example of implementing a bioinformatics workflow in CWL would be a pipeline defined to prepare (index, etc) a reference genome for use in a DNA processing pipeline.
    
    Typically indexing a genome starts with the Burrows-Wheeler Aligner algorithm (BWA) command line tool: bwa index. This can be implemented in CWL / YAML as follows:

bwa-index.cwl

~~~yaml
cwlVersion: v1.0
class: CommandLineTool
baseCommand: [bwa, index]
inputs:
  genome:
    type: File
    inputBinding:
      position: 1
outputs: []
~~~

bwa-index-job.yml

~~~yaml
genome: 
  class: File
  path: /home/cc/RefData/genome_sorted.fa
~~~

    This takes a while to run so it will not be shown. The command to run would be:
    
   > cwl-runner bwa-index.cwl index-argu.yml
   
##### A second example #####

    
    A second example of preparing the reference genome is the Picard command: Picard CreateSequenceDictionary. Picard is a Java-based code, run by calling java -jar from the command line. It is illuminating to see more of CWL's capabilities by observing the Picard CreateSequenceDictionary code.
    
picard-CreateSequenceDictionary.cwl

~~~yaml
cwlVersion: v1.0
class: CommandLineTool
baseCommand: java
arguments:
  - valueFrom: -Xmx64g
    position: 1
  - valueFrom: /usr/local/lib/picard/picard.jar
    position: 2
    prefix: -jar
  - valueFrom: CreateSequenceDictionary
    position: 3
inputs:
  reference:
    type: File
    inputBinding:
      position: 4
      prefix: R=
      separate: false
  outfile:
    type: string
    inputBinding:
      position: 5
      prefix: O=
      separate: false
outputs:
  result:
    type: File
    outputBinding:
      glob: $(inputs.outfile)
~~~

And the corresponding picard-CreateSequenceDictionary-job.yml:

~~~yaml
reference:
  class: File
  path: /home/cc/RefData/genome_sorted.fa
outfile: genome_sorted.dict
~~~

    The output is shown below:


```python
%%bash

cwl-runner picard-CreateSequenceDictionary.cwl picard-CreateSequenceDictionary-job.yml
```

    {
        "result": {
            "checksum": "sha1$c18d9908f7edfbb2ee07841f35f1448351820cd7", 
            "basename": "genome_sorted.dict", 
            "location": "file:///home/cc/Presentation/genome_sorted.dict", 
            "path": "/home/cc/Presentation/genome_sorted.dict", 
            "class": "File", 
            "size": 3549
        }
    }


    /usr/local/bin/cwl-runner 1.0.20161107145355
    [job picard-CreateSequenceDictionary.cwl] /tmp/tmpSt2dL8$ java \
        -Xmx64g \
        -jar \
        /usr/local/lib/picard/picard.jar \
        CreateSequenceDictionary \
        R=/tmp/tmp2Ai2pJ/stg75839cfb-70f7-48d7-9f40-b8086ce20834/genome_sorted.fa \
        O=genome_sorted.dict
    [Wed Nov 16 01:22:56 UTC 2016] picard.sam.CreateSequenceDictionary REFERENCE=/tmp/tmp2Ai2pJ/stg75839cfb-70f7-48d7-9f40-b8086ce20834/genome_sorted.fa OUTPUT=genome_sorted.dict    TRUNCATE_NAMES_AT_WHITESPACE=true NUM_SEQUENCES=2147483647 VERBOSITY=INFO QUIET=false VALIDATION_STRINGENCY=STRICT COMPRESSION_LEVEL=5 MAX_RECORDS_IN_RAM=500000 CREATE_INDEX=false CREATE_MD5_FILE=false GA4GH_CLIENT_SECRETS=client_secrets.json
    [Wed Nov 16 01:23:16 UTC 2016] picard.sam.CreateSequenceDictionary done. Elapsed time: 0.33 minutes.
    Runtime.totalMemory()=4800905216
    Final process status is success


##### Putting entire preparation pipeline together #####

While doing each call separately is fine sometimes, having to do it each and every time that a reference genome needs to be prepared would get annoying rather quickly. That is why CWL scripts can be made to be complete Workflows. A Workflow is just one CWL script that calls multiple Command Line tools sequentially.

By definition, the class "Workflow" will perform the steps as defined either: sequentially if later steps depend on the output of earlier steps or in parallel if the steps are independent of one another.
    
    The most generic preparation pipeline using in bioinformatics uses the following three commands:
    
     1. bwa index
     2. samtools faidx
     3. picard CreateSequenceDictionary
     
    The following PrepareRef.cwl script defines the workflow using three separate CWL scripts:
    
~~~yaml
cwlVersion: v1.0
class: Workflow
inputs:
  ref: File
  out1: string
outputs:
  dictout:
    type: File
    outputSource: csd/dictionary
steps:
  index:
    run: bwa-index.cwl
    in:
      genome: ref
    out: []
  csd:
    run: picard-CreateSequenceDictionary.cwl
    in:
      reference: ref
      outfile: out1
    out: [dictionary]
  fai:
    run: samtools-faidx.cwl
    in:
      genome: ref
    out: []
~~~

    The associated PrepareRef-job.yml script:
    
~~~yaml
ref:
  class: File
  path: /home/cc/RefData/genome_sorted.fa
out1: genome_sorted.dict
~~~

To run this, simply type `cwl-runner PrepareRef.cwl PrepareRef-job.yml` into the command line. Note that all of the individual cwl scripts must be in the same directory (there is probably a way around this but am not sure at this time). As the `bwa index` step takes over 30 minutes to run, the file will be run below with the `index` step commented out:


```python
%%bash

cwl-runner PrepareRef.cwl PrepareRef-job.yml
```

    {
        "dictout": {
            "checksum": "sha1$527dff3e26c8a39e0af9e19f00ac6c8a4e1af9cb", 
            "basename": "genome_sorted.dict", 
            "location": "file:///home/cc/Presentation/genome_sorted.dict", 
            "path": "/home/cc/Presentation/genome_sorted.dict", 
            "class": "File", 
            "size": 3549
        }
    }


    /usr/local/bin/cwl-runner 1.0.20161107145355
    [job fai] /tmp/tmpj6IWMI$ samtools \
        faidx \
        /tmp/tmpXerm1s/stg5be6e3a6-25e8-4025-99b9-9fa60c029798/genome_sorted.fa
    [step fai] completion status is success
    [job csd] /tmp/tmpa9GXvU$ java \
        -Xmx64g \
        -jar \
        /usr/local/lib/picard/picard.jar \
        CreateSequenceDictionary \
        R=/tmp/tmpkYFlWA/stgf9a5822b-f4b9-4029-8d55-81fb21bda289/genome_sorted.fa \
        O=genome_sorted.dict
    [Wed Nov 16 01:26:11 UTC 2016] picard.sam.CreateSequenceDictionary REFERENCE=/tmp/tmpkYFlWA/stgf9a5822b-f4b9-4029-8d55-81fb21bda289/genome_sorted.fa OUTPUT=genome_sorted.dict    TRUNCATE_NAMES_AT_WHITESPACE=true NUM_SEQUENCES=2147483647 VERBOSITY=INFO QUIET=false VALIDATION_STRINGENCY=STRICT COMPRESSION_LEVEL=5 MAX_RECORDS_IN_RAM=500000 CREATE_INDEX=false CREATE_MD5_FILE=false GA4GH_CLIENT_SECRETS=client_secrets.json
    [Wed Nov 16 01:26:31 UTC 2016] picard.sam.CreateSequenceDictionary done. Elapsed time: 0.33 minutes.
    Runtime.totalMemory()=3770679296
    [step csd] completion status is success
    [workflow PrepareRef.cwl] outdir is /tmp/tmps1sV0y
    Final process status is success


Notice that the `step fai` was finished before `step csd`. This shows that, regardless of their defined order, because the two steps were not dependant on one another, the process was finished in parallel. 

ExomeCap Pipeline
=================

#### Well, a section of it at least! ####

![Lego DNA](https://dp1eoqdp1qht7.cloudfront.net/community/projects/5a5/1fb/103829/1924837-o_19m7tf1dnq7m1oedc7m12ui1l12h-full.png "Lego DNA")

CWL Scripts can act like `building blocks` to build up different pipelines. As seen in the example above, `PrepareRef.cwl` simply calls `bwa-index.cwl`, `samtools-faidx.cwl` and `picard-CreateSequenceDictionary.cwl` to prepare a reference genome.

In a simliar way, users can define original workflows that make use of any Command Line Tools as long as the tools is described by a CWL script.

##### Main Problem #####

Main concern here: how to define Workflow so that the output from the first tool used will act as the input for the next one in line. There must be a simple solution; the order of a workflow is defined by the dependencies between the steps. 

This is the next step to be done, I have `ExomeCap1.cwl` partially written but not working at this point. As can be seen below, all of the individual scripts are written, simply have to figure out how to string the inputs and outputs of each command in the pipeline.

### CWL Github ###

Common Workflow Language has a repository that contains lots of bioinformatics tools written as CWL scripts. Many of them have too many parameters for our use but interesting to look into.

Link: https://github.com/common-workflow-language/workflows/


```python
import os
os.listdir('/home/cc/DataProcessing')
```




    ['picard-SortSam.cwl',
     'samtools-view-job.yml',
     'picard-ReorderSam.cwl',
     'picard-MarkDuplicates.cwl',
     'picard-AddOrReplaceReadGroups.cwl',
     'samtools-index.cwl',
     'PrepareRef.cwl',
     'PrepareRef-job.yml',
     'input_R2.fastq',
     'input_R1.fastq',
     'bwa-mem-job.yml',
     'bwa-mem.cwl',
     'ExomeCapPart1.cwl',
     'samtools-view-conv.cwl',
     'samtools-view.cwl']




```python

```
