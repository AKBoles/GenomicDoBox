cwlVersion: v1.0

class: CommandLineTool
baseCommand: java
arguments:
  - valueFrom: -Xmx64g
    position: 1
  - valueFrom: /usr/local/lib/picard/picard.jar
    position: 2
    prefix: -jar
  - valueFrom: SortSam
    position: 3

inputs:
  sortorder:
    type: string
    inputBinding:
      position: 4
      prefix: SORT_ORDER=
      separate: false
  input:
    type: File
    inputBinding:
      position: 5
      prefix: INPUT=
      separate: false
  output:
    type: string
    inputBinding:
      position: 6
      prefix: OUTPUT=
      separate: false
  valid:
    type: string
    inputBinding:
      position: 7
      prefix: VALIDATION_STRINGENCY=
      separate: false
  createind:
    type: string
    inputBinding:
      position: 8
      prefix: CREATE_INDEX=
      separate: false
outputs: 
  result:
    type: File
    outputBinding:
      glob: $(inputs.output)
