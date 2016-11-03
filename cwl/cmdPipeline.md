cmdPipeline.md
==============

### Goal ###

    Process 2 paired-end FASTQ files into a managable, analyzable format.

### Input ###

    input_R1.fastq , input_R2.fastq
	
	R1, R2 describe from what end the sequence read was initialized.
	
### Output (for pipeline described in this document) ###

	final.bam
	
	BAM is the binary version of SAM and came about primarily because of the popularity of SAMtools
	
### Linux Intance File System ###

	*Specific setup for this document.

~~~
/home/cc/
	RefData/
		sorted_genome.fa
		all_other_files_for_genome
	DataProcessing/
		all_data_to_be_processed
~~~

	*Tools to be used
	
~~~
/usr/local/lib/
	DESCRIBE TOOLS
~~~

### Run Commands ###

The following commands can be found at the documentation as given directly below: 

    BWA : http://bio-bwa.sourceforge.net/bwa.shtml
    
    SAMtools : http://www.htslib.org/doc/samtools.html
    
    Picard : https://broadinstitute.github.io/picard/command-line-overview.html
    
To run the commands, simply navigate to the DataProcessing file in the home directory and type the following commands into the command line. It is as simple as that! If there is an error, the error messages generated are really well documented online so a simple Google search should yield intelligent responses.

1. bwa mem

	~~~
	bwa mem -t 48 /home/cc/RefData/genome_sorted.fa input_R1.fastq input_R2.fastq > step1.sam
	~~~

2. samtools view

	~~~
	samtools view -hS -F 3844 -q 10 step1.sam > step2.sam
	~~~
	
3. bwa mem

	~~~
	samtools view -bS -@ 48 step2.sam > step3.bam
	~~~

4. picard SortSam

	~~~
	java -Xmx64g -jar  /usr/local/lib/picard/picard.jar SortSam SORT_ORDER=coordinate INPUT=step3.bam OUTPUT=step4.bam VALIDATION_STRINGENCY=LENIENT CREATE_INDEX=TRUE
	~~~
	
5. picard MarkDuplicates

	~~~
	java -Xmx64g -jar /usr/local/lib/picard/picard.jar MarkDuplicates INPUT=step4.bam OUTPUT=step5.bam METRICS_FILE=metrics CREATE_INDEX=true VALIDATION_STRINGENCY=LENIENT REMOVE_DUPLICATES=true
	~~~

6. picard AddOrReplaceReadGroups

	~~~
	java -Xmx64g -jar /usr/local/lib/picard/picard.jar AddOrReplaceReadGroups INPUT=step5.bam OUTPUT=step6.bam RGID=2 RGLB=Unknown RGPL=Illumina RGPU=sampleIndex RGSM=sampleName VALIDATION_STRINGENCY=SILENT
	~~~
	
7. picard ReorderSam

	~~~
	java -Xmx64g -jar /usr/local/lib/picard/picard.jar ReorderSam INPUT=step6.bam OUTPUT=final.bam R= /home/cc/RefData/genome_sorted.fa
	~~~

8. samtools view

	~~~
	samtools index final.bam final.bai
	~~~

### Comparison to CWL ###

In this folder, the script `bwa_mem.cwl` can be found. This implements the same command as the initial `bwa mem` command that converts the two FASTQ files to the SAM format. This script can be run two different ways:

1. Using the Command Line only.
    
    This method is good for testing out a script. For example, bwa_mem.cwl would be run as follows (notice that all of the input values are given as command line arguments):
    
    ~~~
    $ cwl-runner bwa_mem.cwl --numthreads 48 --genome \home\cc\RefData\genome_sorted.fa --fastq_one input_R1.fastq --fastq_two inpute_R2.fastq --outfile step1.sam
    ~~~
    
2. Using a YAML script to give inputs:

    This method is best for portability and removes the need for user input. When using a YAML script, the initial CWL script is altered from the structure shown in `bwa_mem.cwl` but not much. However, the command input into the command line does differ as the YAML script contains all of the inputs. (lease see the following link for excellent examples of how a CWL and a YAML script can work together: http://www.commonwl.org/v1.0/UserGuide.html ) Note that `bwa_inputs.yaml` is a ficticious script and not created at this time.
    
    ~~~
    $ cwl-runner bwa_mem.cwl bwa_inputs.yaml
    ~~~
