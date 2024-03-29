---
layout: post
title: "Machine Learning in Genomic Medicine: A Review of Computational Problems and Data Sets"
date: 2016-08-23
paper_ref: Leung, Michael K. K., 2016
redirect_from:
    - /papersummaries/2016/08/23/ML-for-genomics.html
    - /paper_summaries/2016/08/23/ML-for-genomics.html
    - /paper-summaries/2016/08/23/ML-for-genomics.html
---
---

[{{ page.paper_ref }}](http://www.psi.toronto.edu/publications/2015/Machine%20Learning%20in%20Genomic%20Medicine-%20A%20Review%20of%20Computational%20Problems%20and%20Data%20Sets.pdf)

## Summary
Major points made by the article: 

* "Our view is that to make genomic medicine a reality, we must develop computer systems that can accurately interpret the text of the genome just as the machinery inside the cell does".
* "Protein-coding exons are the most understood regions in the genome (re: "start" and "stop" codons").
* A long standing open problem is predicting whether a mutation will disrupt the stability or structure of the final protein molecule
* "Predicting **phenotypes** (e.g., traits and disease risks) from biomarkers such as the genome is, in principle, a supervised machine learning problem". The correct approach is not so simple; the computational model should be trained to predict measurable intermediate cell variables, also known as molecular phenotypes, and then these variables can be linked to phenotypes.
* **Alternative Splicing (AS)** is the selection and ligation of specific exons during post-transcriptional modification.
* On average, each protein-coding gene has approximately four transcripts (# of ways of selecting and combining available exons). We would like to be able to predict splicing by discovering the instructions that control splicing

### Computational Model of Splicing
By accurately modeling splicing and AS computationally, researchers have been able to predict how it is affected by variations in the genome, and then to assess whether a mutation in the genome affects disease risk.

### Computational Model of Protein-DNA and Protein-RNA binding
"Accurate models of protein-sequence binding are essential for interpreting the genome and for predicting the effects of mutations...Biologists have developed high-throughput experiments that measure the sequence specificity of individual proteins."

Example computational model: inputs = genomic sequence, outputs is a binding score. One would like to predict the "motifs", or patterns, that a particular protein binds to.

### Specific Discussion Related to Deep Learning
* Deep Learning has been used to improve predictive performance- [see Feedforward NNs for AS patterns](http://bioinformatics.oxfordjournals.org/content/30/12/i121.long).
* CNNs have been used to improve predictive performance for [binding specificity](http://materiais.dbio.uevora.pt/BD/Crescimento/DeepBind.pdf).
* Cellular processes are highly stochastic and hence the genotype of an individual may not be sufficient to completely determine their phenotype
* Measuring hundreds of thousands of cell variable measurements per patient for a small group of people potentially gives a better chance at deciphering the genomic instructions of the cell. More data for a model to learn from.
* Necessary to use "large-scale machine learning"
* RNNs can be useful for the following
    * genome annotation
    * Modelling of cell variable dynamics through time
    * Creating a sequential state model of protein binding based on RNNs or LSTMs
    * Imputation of epigenomic tracks - seq2seq
* Machine Learning models need to be more interpret-able for genomics!

## Notes
Since this is my first foray into computational biology, I'm going to keep track of a lot of terminology here: 

    1. Protein-coding genes describe how to build large molecules made from amino-acid chains (human genome contains ~20,000)
    2. Non-coding genes describe how to build small molecules made from ribonucleic acid (RNA) chains (human genome contains ~25,000)
    3. Information structures making up alternating regions on a typical gene are known as Introns and Exons 
    4. Protein-sequence binding is the binding of proteins to nucleotide sequences
    5. Position-Frequency Matrix - "workhorse of binding site modeling"

## Strengths
Excellent paper for Machine Learning researchers to get a first look at diving into genomics. 
