cwlVersion: v1.0

class: CommandLineTool
baseCommand: java
arguments:
  - valueFrom: -Xmx64g
    position: 1
  - valueFrom: /usr/local/lib/picard/picard.jar
    position: 2
    prefix: -jar
  - valueFrom: ReorderSam
    position: 3

inputs:
  input:
    type: File
    inputBinding:
      position: 4
      prefix: INPUT=
      separate: false
  output:
    type: string
    inputBinding:
      position: 5
      prefix: OUTPUT=
      separate: false
  reference:
    type: File
    inputBinding:
      position: 6
      prefix: R=
      separate: true
outputs: 
  result:
    type: File
    outputBinding:
      glob: $(inputs.output)
