---
layout: post
title: "A Symmetric and Object-centric World Model for Stochastic Environments"
date: 2020-12-08
category: blog
byline: "Web page for my NeurIPS ORLR Workshop Spotlight paper"
---

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  TeX: { equationNumbers: { autoNumber: "AMS" } },
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>

---
**Patrick Emami**, Pan He, Anand Rangarajan, Sanjay Ranka

2020 NeurIPS Object Representations for Learning and Reasoning Workshop **Oral Presentation**

{%
    include image.html
    img="/img/orlr/orlr_main.png"
%}

## Abstract

Object-centric world models learn useful representations for planning and control but have so far only been applied to synthetic and deterministic environments. We introduce a perceptual-grouping-based world model for the dual task of extracting object-centric representations and modeling stochastic dynamics in visually complex and noisy video environments. The world model is built upon a novel latent state space model that learns the variance for object discovery and dynamics separately. This design is motivated by the disparity in available information that exists between the discovery component, which takes a provided video frame and decomposes it into objects, and the dynamics component, which predicts representations for future video frames conditioned only on past frames. To learn the dynamics variance, we introduce a best-of-many-rollouts objective. We show that the world model successfully learns accurate and diverse rollouts in a real-world robotic manipulation environment with noisy actions while learning interpretable object-centric representations.

[[paper]](https://github.com/orlrworkshop/orlrworkshop.github.io/blob/master/pdf/ORLR_3.pdf) [[code]](https://github.com/pemami4911/symmetric-and-object-centric-world-models) [[poster]](/pdfs/Workshop_poster_HD.pdf)

## Demos

<!-- {%
    include image.html
    img="/img/orlr/BAIR_Ours-video-1-rollout-0.gif"
%}
{%
    include image.html
    img="/img/orlr/BAIR_VRNN-video-1-rollout-0.gif"
%} -->
From left to right: ground truth, **Ours**, OP3, VRNN:

<div class="image-wrapper">
    <img src="/img/orlr/BAIR_gt-video-1-rollout-0.gif">
    <img src="/img/orlr/BAIR_Ours-video-1-rollout-0.gif">
    <img src="/img/orlr/BAIR_OP3-video-1-rollout-0.gif">
    <img src="/img/orlr/BAIR_VRNN-video-1-rollout-0.gif">
</div>

<div class="image-wrapper">
    <img src="/img/orlr/BAIR_gt-video-3-rollout-0.gif">
    <img src="/img/orlr/BAIR_Ours-video-3-rollout-0.gif">
    <img src="/img/orlr/BAIR_OP3-video-3-rollout-0.gif">
    <img src="/img/orlr/BAIR_VRNN-video-3-rollout-0.gif">
</div>

Object decompositions, **Ours**:

<div class="image-wrapper">
    <img src="/img/orlr/BAIR_Ours-slot-video-1-rollout-0.gif">
    <img src="/img/orlr/BAIR_Ours-slot-video-3-rollout-0.gif">
    <img src="/img/orlr/BAIR_Ours-slot-video-4-rollout-0.gif">
    <img src="/img/orlr/BAIR_Ours-slot-video-5-rollout-0.gif">
    <img src="/img/orlr/BAIR_Ours-slot-video-9-rollout-0.gif">
</div>
