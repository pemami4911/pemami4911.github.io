---
layout: post
title: "Interaction Networks for Learning about Objects, Relations, and Physics"
date: 2017-05-14
paper_ref: Battaglia, et. al., 2016
redirect_from:
    - /paper-summaries/2017/05/14/interaction-networks-for-learning-about-objects-relations-physics.html
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

[{{page.paper_ref}}](https://arxiv.org/abs/1612.00222)

## Summary

This ambitious paper proposes a deep learning framework for modeling the physical interactions between objects in an environment. The authors present Interaction Networks (IN), which explicitly separate the processes of learning object dynamics and relations between objects. 

IN is designed to work on graphs where objects are nodes and edges are relations between objects. This is to make it scalable to different environments.

The architecture is simple; two MLPs learn representations over object dynamics and relations between objects, respectively. The input to the system is the state decomposed into the objects and their physical relations (gravitational attraciton, collisions, springs), as well as external effects (gravity). Object states can be further decomposed into position and velocity. In general, the output is the velocity of the objects at the subsequent time step.

The system is evaluated on interesting physical reasoning tasks, such as n-bodies interacting, bouncing balls colliding, and string/mass systems. IN showed significantly lower MSE when predicting future states of objects in the scenes compared to simple baselines.

A custom physics engine was used to generate trajectories for training data. All training objectives and test measures used MSE between the model's predictions and the ground truth target.