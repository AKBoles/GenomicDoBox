cmdPipeline.md
==============

### Goal ###

    Process 2 paired-end FASTQ files into a managable, analyzable format

### Input ###

    input_R1.fastq , input_R2.fastq
	
	R1, R2 describe what end the sequence read was initialized from
	
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

### Run Commands ###

1. bwa mem - DESCRIPTION

	~~~
	bwa mem -t 48 /home/cc/RefData/genome_sorted.fa input_R1.fastq input_R2.fastq > step1.sam
	~~~

2. samtools view - DESCRIPTION

	~~~
	samtools view -hS -F 3844 -q 10 step1.sam > step2.sam
	~~~
	
3. bwa mem - DESCRIPTION

	~~~
	samtools view -bS -@ 48 step2.sam > step3.bam
	~~~

4. picard SortSam - DESCRIPTION

	~~~
	java -Xmx64g -jar  /usr/local/lib/picard/picard.jar SortSam SORT_ORDER=coordinate INPUT=step3.bam OUTPUT=step4.bam VALIDATION_STRINGENCY=LENIENT CREATE_INDEX=TRUE
	~~~
	
5. picard MarkDuplicates - DESCRIPTION

	~~~
	java -Xmx64g -jar /usr/local/lib/picard/picard.jar MarkDuplicates INPUT=step4.bam OUTPUT=step5.bam METRICS_FILE=metrics CREATE_INDEX=true VALIDATION_STRINGENCY=LENIENT REMOVE_DUPLICATES=true
	~~~

6. picard AddOrReplaceReadGroups - DESCRIPTION

	~~~
	java -Xmx64g -jar /usr/local/lib/picard/picard.jar AddOrReplaceReadGroups INPUT=step5.bam OUTPUT=step6.bam RGID=2 RGLB=Unknown RGPL=Illumina RGPU=sampleIndex RGSM=sampleName VALIDATION_STRINGENCY=SILENT
	~~~
	
7. picard ReorderSam - DESCRIPTION

	~~~
	java -Xmx64g -jar /usr/local/lib/picard/picard.jar ReorderSam INPUT=step6.bam OUTPUT=final.bam R= /home/cc/RefData/genome_sorted.fa
	~~~

8. samtools view - DESCRIPTION

	~~~
	samtools index final.bam ???
	~~~