---
layout: post
title: "Pixel Recursive Super Resolution"
date: 2017-03-28
paper_ref: Dahl, Norouzi, Shlens, 2017
redirect_from:
    - /paper-summaries/2017/03/28/pixel-recursive-super-res.html
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

[{{page.paper_ref}}](https://arxiv.org/abs/1702.00783)

## Summary

This paper proposes a novel neural architecture for solving the super resolution task for large factors of magnification. The problem is challenging, because the input images can be as low-res as 8 x 8; hence, there is a wide variety of high-res images that could correspond to this image. The author's neural architecture consists of an autoregressive PixelCNN network augmented with a conditioning Convolutional Neural Network; the autoregressive aspect is to allow the network to output pixels sequentially and thereby capture the conditional dependency between a pixel and its neighbors. This is in contrast to prior work that assume conditional independence between pixels, and use a MSE per-pixel loss for supervision. 

## Questions for discussion

* Not too familiar with this line of research; 32 x 32 images is still fairly "low-res". Is this state-of-the-art? 
* The authors highlighted how the perceptual quality did not always correspond with negative log likelihood. Why might this be? NLL is equivalent to MLE, which is equivalent to minimizing KL divergence... 

## General commentary

* Dictionary-inspired methods that search a bank of pre-learned filters on images and selecting appropriate patches by an efficient hashing mechanism has comparable performance
* PixelCNN is a stochastic model that provides an explicit model for $ \log p( y_i \| x, y_{< i}) $. However, the auto-regressive distribution largely ignores the conditioning on the low-resoultion image without explicitly separating the network into two components, one being a "conditioning" network.
* Had to add an extra term to the loss, the cross-entropy between the conditioning network's predictions via a softmax over the `K` possible values that the `i'th` output pixel can take and the ground truth labels
