---
layout: post
title: "Fast, Exact, and Multi-Scale Inference for Semantic Image Segmentation with Deep Gaussian CRFs"
date: 2017-05-04
paper_ref: Chandra, Kokkinos, 2016
redirect_from:
    - /paper-summaries/2017/05/04/semantic-image-seg-with-deep-g-crfs.html
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

The basic idea is to set the outputs of a convolutional neural network to be the energy of a segmentation hypothesis, in the form of 
$$
\begin{equation}
E(x) = \frac{1}{2} x^{\intercal}(A + \lambda I) x - Bx
\end{equation}
$$ 
. The network predicts what the $A$ (pairwise) and $B$ (unary) terms in the energy function are for an image. $\lambda$ is set manually to enforce positive-definiteness. Then a Quadratic Optimization + softmax module gives the final per-class scores for each pixel in the image (See Fig. 1) by solving for $x$. Originally, $A$ is a $(P \times L) \times (P \times L)$ matrix, where $L$ is the number of class labels and $P$ is number of pixels.

## Shared pair-wise terms

$A$ is no longer dependent on the number of class labels; only care about pixel interactions independent on what the label is. Now, the inference equation $(A + \lambda I) x = B$ is reduced to a system of $L + 1$ equations for $A$ of dim $P \times P$.

## Conjugate Gradient method 

Need to solve $x = A^{-1}b$. 
The $A$ matrix is very sparse, since it only deals with 4, 8, or 12-connected neighborhoods. CG is the current recommended approach for solving $Ax = b$ when $A$ is sparse [why?](https://math.stackexchange.com/questions/655306/conjugate-gradient-method-and-sparse-systems) When $A$ is dense, it is recommended to factorize A and then use backsubstitution. [see here](https://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf)

## Experiments

Try out the above + fusing information across 3 different resolutions.

* metric - Intersection over Union
* baselines - Multiresolution DeepLab-LargeFOV, CRF-RNN
* QO network - Baseline extended to have a binary and unary stream. QO module can be shared by all resolutions, or replicated three times for each scale

75.5% mean IOU on VOC PASCAL 2012 for this approach. Without more details and tests of significance, hard to say whether this method is really more effective than prev SOTA. It seems to do about ~1-2% IOU better than the baselines. Also seems to be much faster. 