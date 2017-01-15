cwlVersion: cwl:draft-3
class: Workflow
inputs:
  - id: numInput
    type: int
  - id: genomeInput
    type: File
  - id: fastq_oneInput
    type: File
  - id: fastq_twoInput
    type: File
  - id: output1
    type: string
  - id: formatInput
    type: int
  - id: qualityInput
    type: int
  - id: output2
    type: string
  - id: numThreads3
    type: int
  - id: output3
    type: string
  - id: sortorder4
    type: string
  - id: output4
    type: string
  - id: valid4
    type: string
  - id: createind4
    type: boolean
  - id: output5
    type: string
  - id: metrics5
    type: string
  - id: createind5
    type: boolean
  - id: valid5
    type: string
  - id: removedup5
    type: boolean
  - id: output6
    type: string
  - id: rgid6
    type: int
  - id: rglb6
    type: string
  - id: rgpl6
    type: string
  - id: rgpu6
    type: string
  - id: rgsm6
    type: string
  - id: valid6
    type: string
  - id: output7
    type: string
  - id: reference7
    type: File
  - id: output8
    type: string

outputs:
  - id: workflowOutput
    type: File
    source: "#picard-samtool-view/result"

steps:
 - id: bwa-mem
   run: bwa-mem.cwl
   inputs:
      - id: numthreads
        source: "#numInput"
      - id: genome
        source: "#genomeInput"
      - id: fastq_one
        source: "#fastq_oneInput"
      - id: fastq_two
        source: "#fastq_twoInput"
      - id: output
        source: "#output1"
   outputs:
      - id: result

 - id: samtool
   run: samtools-view.cwl
   inputs:
      - id: format
        source: "#formatInput"
      - id: quality
        source: "#qualityInput"
      - id: input
        source: "#bwa-mem/result"
      - id: output
        source: "#output2"
   outputs:
      - id: result

 - id: samtool-conv
   run: samtools-view-conv.cwl
   inputs:
      - id: numThreads
        source: "#numThreads3"
      - id: input
        source: "#bwa-mem/result"
      - id: output
        source: "#output3"
   outputs:
      - id: result

 - id: picard-Sort
   run: picard-SortSam.cwl
   inputs:
      - id: sortorder
        source: "#sortorder4"
      - id: input
        source: "#samtool-conv/result"
      - id: output
        source: "#output4"
      - id: valid
        source: "#valid4"
      - id: createind
        source: "#createind4"
   outputs:
      - id: result

 - id: picard-MarkDup
   run: picard-MarkDuplicates.cwl
   inputs:
      - id: input
        source: "#picard-Sort/result"
      - id: output
        source: "#output5"
      - id: metrics
        source: "#metrics5"
      - id: createind
        source: "#createind5"
      - id: valid
        source: "#valid5"
      - id: removedup
        source: "#removedup5"
   outputs:
      - id: result

 - id: picard-AddorRep
   run: picard-AddOrReplaceReadGroups.cwl
   inputs:
      - id: input
        source: "#picard-MarkDup/result"
      - id: output
        source: "#output6"
      - id: rgid
        source: "#rgid6"
      - id: rglb
        source: "#rglb6"
      - id: rgpl
        source: "#rgpl6"
      - id: rgpu
        source: "#rgpu6"
      - id: rgsm
        source: "#rgsm6"
      - id: valid
        source: "#valid6"
   outputs:
      - id: result

 - id: picard-ReorderSam
   run: picard-ReorderSam.cwl
   inputs:
      - id: input
        source: "#picard-AddorRep/result"
      - id: output
        source: "#output7"
      - id: reference
        source: "#reference7"
   outputs:
      - id: result

 - id: samtool-view
   run: samtools-view.cwl
   inputs:
      - id: input
        source: "#picard-ReorderSam/result"
      - id: output
        source: "#output8"
   outputs:
      - id: result
