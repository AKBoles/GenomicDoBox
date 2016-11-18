cwlVersion: v1.0
class: CommandLineTool
baseCommand: [bwa, index] 
inputs:
  genome:
    type: File
    inputBinding:
      position: 1
outputs: []
