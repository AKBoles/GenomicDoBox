cwlVersion: v1.0
class: CommandLineTool
baseCommand: [bwa, mem]
stdout: output.txt
inputs:
  numthreads:
    type: int
    inputBinding:
      position: 1
      prefix: -t
      separate: true
  genome:
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
  fastq_one:
    type: File
    inputBinding:
      position: 3
  fastq_two:
    type: File
    inputBinding:
      position: 4
  output1:
    type: string
    inputBinding:
      position: 5
      prefix: '>'
      separate: true
outputs: 
  output:
    type: stdout
  result:
    type: File
    outputBinding:
      glob: $(inputs.output1)
