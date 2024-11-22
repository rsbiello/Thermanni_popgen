#!/bin/bash

module load rohan-1.0

REF=rTesHer1.1.fasta
CHR=list_89scaffs_1Mb_mod
BAM=PNV_9_HB_S24_001_sorted_dedup_rg_real_rmopt.bam
BED=Thermanni.callable.bed

rohan -t 16 -o PNV_9 --rohmu 5e-05 --map $BED --auto $CHR --tstv 1.85 --size 100000 $REF $BAM
