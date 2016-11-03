Genomic DoBox
=============

### Project Definition ###

Using the power of Chameleon Cloud, this application probes an OpenStack Swift Container for DNA sequenced data and then processes it into a human-friendly format. The DNA processing is done by using primarily Linux-based Command Line Tools in a specific order - commonly called "pipelines". For the sake of privacy, the current processing pipelines are not being released on Github quite yet. For clarities sake, a generic pipeline is included in the JSON folder.

Current Linux image being use: Ubuntu 14.04

### Acknowledgements ###

Graduate Student Researcher at the Open Cloud Institute at the University of Texas San Antonio. This project is done in collaboration with the University of Texas Health Science Center at San Antonio.

### Python Folder ###

Contains python files that allow the application to run. See the README.md file inside the folder for more information.

### Json Folder ###

Contains JSON files that help set up the reference genome and HG19 Database for data processing. See the README.md file inside the folder for more information.

### Bash Folder ###

Contains bash scripts that are relevant to the application. See the README.md file inside the folder for more information.

### CWL Folder ###

Contains Common Workflow Language scripts to be used alongside the JSON scripts. See the README.md file inside the folder for more information.

### Running Instructions ###

1. run requirements.txt by using: 
    ~~~
    $ sudo pip install -r requirements.txt
    ~~~

2. Install all of the necessary processing tools using written in INSTALLATION.md
    
      * Note that a setup.py python script is being worked on to remove the need to install necessary tools via copy and paste.
      
3. Start the application by navigating to the python folder and then using: 
    ~~~
    $ python orchestration.py sample.json
    ~~~
    
      * Note that the user will be required to first source an openrc file that logs them into their Chameleon Cloud project.
      * Currently the user needs to specify the location of a JSON file containing their desired pipeline to be run as a command line argument.


### Github Link ###

https://github.com/AKBoles/GenomicDoBox

### Tools Used ###

1. Burrows-Wheeler Aligner: http://bio-bwa.sourceforge.net/

2. SAMtools: http://samtools.sourceforge.net/

3. Picard: https://broadinstitute.github.io/picard/

### Relevant Supplemental Information ###

1.	Chameleon Cloud: https://www.chameleoncloud.org/

2.	OpenStack Python SDK: http://docs.openstack.org/user-guide/sdk.html

3.	1000 Genomes Project: http://www.internationalgenome.org/

4.  FASTQ File Type Description: https://en.wikipedia.org/wiki/FASTQ_format
