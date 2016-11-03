cwlVersion: v1.0
class: CommandLineTool
baseCommand: [bwa, mem]
inputs:
  - id: numthreads
    type: int
    inputBinding:
      position: 1
      prefix: "-t"
  - id: genome
    type: File
    inputBinding:
      position: 2
    secondaryFiles:
      - ".amb"
      - ".ann"
      - ".bwt"
      - ".fai"
      - ".pac"
      - ".sa"
  - id: fastq_one
    type: File
    inputBinding:
      position: 3
  - id: fastq_two
    type: File
    inputBinding:
      position: 4
  - id: outfile
    type: string
    inputBinding:
      position: 5
      prefix: ">"
outputs: 
  - id: result
    type: File
    outputBinding:
      glob: $(inputs.outfile)
