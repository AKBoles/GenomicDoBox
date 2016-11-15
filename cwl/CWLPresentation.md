
Common Workflow Language (CWL)
==============================

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
    [job HelloWorld.cwl] /tmp/tmpRnvNLB$ echo \
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

cwl-runner hello.cwl hello.yml
```

    {}


    /usr/local/bin/cwl-runner 1.0.20161107145355
    [job hello.cwl] /tmp/tmpD3oAFX$ echo \
        'Hello World!'
    Hello World!
    Final process status is success


CWL for Bioinformatics
----------------------

### Preparing Reference Genome ###

##### A first example #####

    A first example of implementing a bioinformatics workflow in CWL would be a pipeline defined to prepare (index, etc) a reference genome for use in a DNA processing pipeline.
    
    Typically indexing a genome starts with the Burrows-Wheeler Aligner algorithm (BWA) command line tool: bwa index. This can be implemented in CWL / YAML as follows:

bwa_index.cwl

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

index_argu.yml

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

And the corresponding CreateSequenceDictionary-argu.yml:

~~~yaml
reference:
  class: File
  path: /home/cc/RefData/genome_sorted.fa
outfile: genome_sorted.dict
~~~

    The output is shown below:


```python
%%bash

cwl-runner picard-CreateSequenceDictionary.cwl CreateSequenceDictionary-argu.yml
```

    {
        "result": {
            "checksum": "sha1$5ef243ff04d3552611c17e58e6cf4f40d8b90e63", 
            "basename": "genome_sorted.dict", 
            "location": "file:///home/cc/Presentation/genome_sorted.dict", 
            "path": "/home/cc/Presentation/genome_sorted.dict", 
            "class": "File", 
            "size": 3549
        }
    }


    /usr/local/bin/cwl-runner 1.0.20161107145355
    [job picard-CreateSequenceDictionary.cwl] /tmp/tmp5lu1Ua$ java \
        -Xmx64g \
        -jar \
        /usr/local/lib/picard/picard.jar \
        CreateSequenceDictionary \
        R=/tmp/tmprIlt_v/stg28cd8269-6979-4a18-bf7b-ab782a8fc3ee/genome_sorted.fa \
        O=genome_sorted.dict
    [Tue Nov 15 20:57:30 UTC 2016] picard.sam.CreateSequenceDictionary REFERENCE=/tmp/tmprIlt_v/stg28cd8269-6979-4a18-bf7b-ab782a8fc3ee/genome_sorted.fa OUTPUT=genome_sorted.dict    TRUNCATE_NAMES_AT_WHITESPACE=true NUM_SEQUENCES=2147483647 VERBOSITY=INFO QUIET=false VALIDATION_STRINGENCY=STRICT COMPRESSION_LEVEL=5 MAX_RECORDS_IN_RAM=500000 CREATE_INDEX=false CREATE_MD5_FILE=false GA4GH_CLIENT_SECRETS=client_secrets.json
    [Tue Nov 15 20:57:50 UTC 2016] picard.sam.CreateSequenceDictionary done. Elapsed time: 0.33 minutes.
    Runtime.totalMemory()=4546101248
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

cd /home/cc/RefData

cwl-runner PrepareRef.cwl PrepareRef-job.yml
```
