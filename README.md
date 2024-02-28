### Introduction

Homopolymer (HP) sequencing is error-prone in next-generation sequencing (NGS) assays, and may induce false insertion/deletions and substitutions. DNA homopolymer (HP) tracts, also known as mononucleotide microsatellites, are sequences consisting of a series of consecutive identical bases, such as poly(dA).poly(dT) and poly(dG).poly(dC), which are the simplest of the sequence repeats in the genome. This program aimed to identify the specific homopolymeric sequences.


### Manual

**Dependencies:**
* python3
* numpy

**Install Using Bioconda**
	conda create -n python3 -c conda-forge -y
	conda install python=3
	conda install conda-forge::numpy

### Useage

**To run ArtifactsFinder**

	python3 homoploymer_finder.py Sample.recal.bam Sample input.site.xls test

Note : 
Sample.recal.bam is the input bam file; 
Sample is the sample name; 
input.site.xls is the input specific homopolymeric sequences file; 
test is the prefix in the output results name (Sample.prefix.homoploymer.repeat.xls,Sample.prefix.homoploymer.all.xls)


### Input File
**bam file**
```
An example of a bam file can be viewed here: ([`Sample.recal.bam`](HomoploymerFinder/example/Sample.recal.bam)).

Note: Must have an index file for bam.
```

**specific homopolymeric sequences file**
```
An example of a specific homopolymeric sequences file can be viewed here: ([`input.site.xls`](HomoploymerFinder/example/input.site.xls)).
```
### Output File
**sam file**
```
An example of a sam file can be viewed here: ([`Sample.sam`](HomoploymerFinder/example/Sample.sam)).

Note: The sam file is extract bam from specified region. Here is the bam of the last region in the input homopolymeric sequences file.
```
**Sample.test.homoploymer.repeat.xls**
```
An example of a Sample.test.homoploymer.repeat.xls file can be viewed here: ([`Sample.test.homoploymer.repeat.xls`](HomoploymerFinder/example/Sample.test.homoploymer.repeat.xls)).

Note: The results which satisfy left sequence, right sequence, and insert sequence contains one or more repeating unit of target repeated sequences.
```
**Sample.test.homoploymer.all.xls**
```
An example of a Sample.test.homoploymer.all.xls file can be viewed here: ([`Sample.test.homoploymer.all.xls`](HomoploymerFinder/example/Sample.test.homoploymer.all.xls)).

Note: The all results which satisfy left sequence, right sequence. The insert sequence may contains repeating unit of target repeated sequences and other bases.
```
###Contact
If you have any questions, please contact lilicai@chosenmedtech.com .
