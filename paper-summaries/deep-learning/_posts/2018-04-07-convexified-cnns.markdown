---
layout: post
title: "Convexified Convolutional Neural Networks"
date: 2018-04-07
paper_ref: Zhang, Liang, Wainwright, 2016
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

[{{ page.paper_ref }}](https://arxiv.org/abs/1609.01000)

## Summary

In this paper, the authors proposed a method for convexifying convolutional neural networks to train them without backpropagation. Furthermore, this relaxation to the convex setting allows for theoretical proofs of bounds on the generalization error. 

Succinctly, they propose to use RKHS and the kernel trick to lift the data into a high-dimensional space that is expressive enough to capture certain nonlinear activation functions. Hence, on experiments on MNIST and CIFAR-10, they show that they can outperform smaller CNNs by "convexifying" them. 

They note that their method doesn't work with max pooling or very deep CNNs with lots of bells and whistles. 

This is a thought-provoking paper. I like how the authors pursued a theoretically interesting question, even though there isn't much practical use yet for this. I don't have personal experience writing theory papers, but I imagine that this is a good(?) representation of how they often go in ML. The research is driven by an interesting theoretical question, not a practical application that needs solving/SOTA results.