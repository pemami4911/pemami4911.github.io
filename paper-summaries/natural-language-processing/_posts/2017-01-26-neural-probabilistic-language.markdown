---
layout: post
title: "A Neural Probabilistic Language Model"
date: 2017-01-26
paper_ref: Bengio, et al., 2003
redirect_from:
     - /paper-summaries/2017/01/26/neural-probabilistic-language.html
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  TeX: { equationNumbers: { autoNumber: "AMS" } },
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script> 
---

[{{ page.paper_ref }}](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf)

## Summary

* associate with each word in the vocabulary a distributed *word feature vector* (real valued vector in $\mathbb{R}^n$)
* express the joint probability function of word sequences in terms of the feature vectors of these words in the sequence
* learn simultaneously the word feature vectors and the parameters of that probability function

For discrete random variables, learning a joint probability distribution is hard because a small change in one of the variables could cause a large change in the value of the function to be estimated. Instead, transforming the discrete random variables into a vector space in $\mathbb{R}^n$ allows the use of neural nets or GMMs which are smooth approximators. Additionally, the notion of a "nearby" word within the continuous vector space representation is now defined more clearly.  

Words are mapped into a matrix $C$ of size ($\|V\| \times m$) for a vocabulary size $\|V\|$ and embedding dim $m$. The feature vectors (columns of $C$) are learned simultanesouly with the parameters of the neural network. The input to the time-lagged neural network (RNN) is the concatenated vector of word representations. The objective is to maximize the log-likehood of a given sequence of out-of-sample words. This essentially is the encoder in Neural Machine Translation. 

## Things of interest

* The curse of dimensionality in modeling joint probability of sequences of words in a language is a major stumbling block
* One can reduce the difficulty by using the fact that temporally closer words in the word sequence are statistically more dependent $\rightarrow$ *n-gram* models
* It was noted by the authors that n-gram models and the neural models made different "errors", so an averaging model of the two showed improvements overall
* It is suggested by the authors as well to train multiple smaller networks on partitions of the training data to speed things up
* Learning word embeddings is very parallelizable- specifically, the computation of the output layer of the neural model was found to take up roughly 99.7% of the computation (since you're computing a likelihood of a sequence out of the entire vocabulary)




