#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: [samtools, view]
arguments:
  - valueFrom: -bS
    position: 1
inputs:
  numThreads:
    type: int
    inputBinding:
      position: 2
      prefix: -@
      separate: true 
  output:
    type: string
    inputBinding:
      position: 3
      prefix: -o
      separate: true
  input:
    type: File
    inputBinding:
      position: 4
outputs: 
  result:
    type: File
    outputBinding:
      glob: $(inputs.output)
