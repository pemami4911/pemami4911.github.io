---
layout: post
title: "Fast, Exact, and Multi-Scale Inference for Semantic Image Segmentation with Deep Gaussian CRFs"
date: 2017-05-04
category: paper-summaries
paper_ref: Chandra, Kokkinos, 2016
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

[{{page.paper_ref}}](https://arxiv.org/abs/1603.08358)

## Semantic Image Segmentation 

[Image Example](https://wiki.tum.de/download/attachments/23561833/sms.png?version=1&modificationDate=1483619907233&api=v2)


Put simply, the task is to cluster pixels in an image together and to assign all pixels in a cluster a meaningful label. Labels are generally "high-level" concepts, such as "horse", "dog", "boat", etc. 

[Here is the VOC PASCAL 2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/) dataset used in this paper.

## Discussion Q's

## Why G-CRFs?

Joint distributions are hard, so exploit factorizable (exponential-family) probability distributions and conditional independence. This results in a graph-like structure. 

If the label assigned to each pixel is a random variable, then an conditional random field suggests that there's a dependence between a pixel's label and the label's of other nearby pixels. This seems intuitive.

Author's argue that continuous Gaussian outputs are unimodal conditioned on the data, so given an image, one solution dominates the posterior. The log-likelihood is a quadratic, which allows the approximate inference task to be cast a quadratic optimization in an energy-minimization setting. 

## Deep G-CRF architecture

The network infers what the $A$ (pairwise) and $B$ (unary) terms in the energy function are for an image. Then the QO + softmax module gives the final per-class scores for each pixel in the image (See Fig. 1)

## Shared pair-wise terms

$A$ is no longer dependent on the number of class labels. Now, the inference equation $(A + \lambda I) x = B$ is reduced to a system of $L + 1$ equations for $A$ of dim $P \times P$, where $P$ is the number of pixels.

## Conjugate Gradient method 

The $A$ matrix is very sparse, since it only deals with 4, 8, or 12-connected neighborhoods. CG is the current recommended approach for solving $Ax = b$ when $A$ is sparse [why?](https://math.stackexchange.com/questions/655306/conjugate-gradient-method-and-sparse-systems) When $A$ is dense, it is recommended to factorize A and then use backsubstitution. [see here](https://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf)

## Experiments

* metric - Intersection over Union
* baseline - Extended DeepLab-LargeFOV
* QO network - Baseline extended to have a binary and unary stream. QO module can be shared by all resolutions, or replicated three times for each scale

Without more details and tests of significance, hard to say whether this method is really more effective. It seems to do about ~1-2% IOU better than the baselines. Also seems to be much faster. 