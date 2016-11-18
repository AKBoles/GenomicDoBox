cwlVersion: v1.0

class: CommandLineTool
baseCommand: java
arguments:
  - valueFrom: -Xmx64g
    position: 1
  - valueFrom: /usr/local/lib/picard/picard.jar
    position: 2
    prefix: -jar
  - valueFrom: MarkDuplicates
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
  metrics:
    type: string
    inputBinding:
      position: 6
      prefix: METRICS_FILE=
      separate: false
  createind:
    type: string
    inputBinding:
      position: 7
      prefix: CREATE_INDEX=
      separate: false
  valid:
    type: string
    inputBinding:
      position: 8
      prefix: VALIDATION_STRINGENCY=
      separate: false
  removedup:
    type: string
    inputBinding:
      position: 9
      prefix: REMOVE_DUPLICATES=
      separate: false
outputs: 
  result:
    type: File
    outputBinding:
      glob: $(inputs.output)
