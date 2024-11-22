#!/bin/bash

module load plink-1.90

VCF=Thermanni.callable.89scaffs.vcf.gz

plink --vcf $VCF --keep-allele-order --allow-extra-chr --homozyg-window-snp 50 --homozyg-kb 50 --homozyg-snp 100 --homozyg-density 50 --homozyg-gap 1000 --homozyg-window-het 0 --homozyg-window-missing 5 --homozyg-window-threshold 0.05 --het --out roh.89scaffs.custom.hom_50kb.het_0
