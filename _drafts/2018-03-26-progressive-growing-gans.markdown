---
layout: post
title: "Progressive Growing of GANs for Improved Quality, Stability, and Variation"
date: 2018-03-26
paper_ref: Karras, et. al., 2018
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

[{{page.paper_ref}}](http://research.nvidia.com/sites/default/files/pubs/2017-10_Progressive-Growing-of/karras2018iclr-paper.pdf)

## Summary

The basic idea is to introduce a curriculum into the GAN training procedure. One starts by training the Generator to produce 4 x 4 images, progressively adding layers to up the resolution. In the paper, they should high-quality 1024 x 1024 samples from CelebA, LSUN, and CIFAR-10.

### Increasing variation

Compute average standard deviation over all features and spatial locations of the minibatch and then insert as a layer near the end. Encourages generated and real image minibatches to have similar statistics.