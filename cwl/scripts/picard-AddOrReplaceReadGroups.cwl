cwlVersion: v1.0

class: CommandLineTool
baseCommand: java
arguments:
  - valueFrom: -Xmx64g
    position: 1
  - valueFrom: /usr/local/lib/picard/picard.jar
    position: 2
    prefix: -jar
  - valueFrom: AddOrReplaceReadGroups
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
  rgid:
    type: int
    inputBinding:
      position: 6
      prefix: RGID=
      separate: false
  rglb:
    type: string
    inputBinding:
      position: 7
      prefix: RGLB=
      separate: false
  rgpl:
    type: string
    inputBinding:
      position: 8
      prefix: RGPL=
      separate: false
  rgpu:
    type: string
    inputBinding:
      position: 9
      prefix: RGPU=
      separate: false
  rgsm:
    type: string
    inputBinding:
      position: 10
      prefix: RGSM=
      separate: false
  valid:
    type: string
    inputBinding:
      position: 11
      prefix: VALIDATION_STRINGENCY=
      separate: false
outputs: 
  result:
    type: File
    outputBinding:
      glob: $(inputs.output)
