#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: [samtools, view]
arguments:
  - valueFrom: -hS  
    position: 1
inputs:
  format:
    type: int
    inputBinding:
      position: 2
      prefix: -F
      separate: true 
  quality:
    type: int
    inputBinding:
      position: 3
      prefix: -q
      separate: true
  output:
    type: string
    inputBinding:
      position: 4
      prefix: -o
      separate: true
  input:
    type: File
    inputBinding:
      position: 5
outputs: 
  result:
    type: File
    outputBinding:
      glob: $(inputs.output)
