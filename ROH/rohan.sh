#!/bin/bash

module load rohan-1.0

REF= #/path/to/reference/xxx.fa
CHR= #/path/to/list/chromosomes
BAM= #/path/to/BAM/xxx.bam
BED= #/path/to/map/xxx.bed

rohan -t 16 -o PNV_9 --rohmu 5e-05 --map $BED --auto $CHR --tstv 1.85 --size 100000 $REF $BAM
