---
layout: post
title: "Progressive Growing of GANs for Improved Quality, Stability, and Variation"
date: 2018-03-26
paper_ref: Karras, et al., 2018
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

The basic idea is to introduce a curriculum into the GAN training procedure. One starts by training the generator to produce 4 x 4 images, progressively adding layers to increase the resolution. In the paper, they generated high-quality 1024 x 1024 samples from CelebA, LSUN, and CIFAR-10.

This is a nice applied paper where the core idea is quite simple and explained clearly. They describe all of the challenges hidden under the surface of training large-scale GANs and tell the reader how they tackled them. Lots of good deep learning voodoo in this paper.

They found that the progressive scheme helps the GAN converege to much better optimum (image quality is amazing) and reduces total training time by about a factor of 2.

They mainly use the [WGAN-GP](https://arxiv.org/abs/1704.00028) loss. 
Recall that the WGAN loss is $$ \min_G \max_D \mathbb{E}_{x \sim \mathbb{P}_r} [ D(x) ] - \mathbb{E}_{\hat{x} \sim \mathbb{P}_g} [D(\hat{x}) ] $$

The main change made in WGAN-GP is the addition of a gradient penalty term to take care of the 1-Lipschitz constraint. Previous, hard weight clipping within some [-c, c] was used. The new loss looks like $$ \min_G \max_D \mathbb{E}_{x \sim \mathbb{P}_r} [ D(x) ] - \mathbb{E}_{\hat{x} \sim \mathbb{P}_g} [D(\hat{x}) ] + \color{blue}{\lambda \mathbb{E}_{x' \sim \mathbb{P}_{x'}} [ \|( \nabla_{x'} D(x')\|_2 - 1)^2]} $$, and $\lambda$ is set to 10.

Definition: **Inception score** is an evaluation metric for GANs where generated samples are fed into an Inception model trained on ImageNet. Images with meaningful objects are supposed to have low label entropy, but the entropy across images should be high (high variation). 
