---
layout: post
title: "Towards Deep Symbolic Reinforcement Learning"
date: 2017-08-29
paper_ref: Garnelo, et. al., 2017
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

[{{page.paper_ref}}](https://arxiv.org/abs/1609.05518v2)

## Summary

{%
  include image.html
  img="/img/symbolic-rl.bmp"
%}

It is desirable for an agent to symbolically reason about its environment, in order to expediate the process of learning optimal behaviors. However, "classic" symbolic AI suffers from the **symbol grounding problem**; symbolic elements have traditionally been hand-crafted, and hence, are brittle. On the other hand, Deep Learning can be used to automatically learn ~optimal "symbols", upon which a reinforcement learning agent could learn behaviors motivated by these learned symbols. By forcing a Deep RL agent to operate in a symbolic domain, the decisions made by the agent are naturally more interpretable.

The aspects of AI that this work focuses on are closely related to those proposed in the manifesto written by [Lake et. al.](http://pemami4911.github.io/paper-summaries/general-ai/2016/05/13/learning-to-think.html). There are also nods to [Douglas Hofstadter's](http://cogs.indiana.edu/people/profile.php?u=dughof) work on analogy as being the main driving force behind intelligence, as well as [Marcus Hutter's](http://www.hutter1.net/) Universal Artificial Intelligence work.

1. Conceptual abstraction - agents can use abstractions to make analogies and hence learn optimal behaviors faster
2. Compositional structure - probabilistic first-order logic provides the underlying framework for a representation medium that is compositional
3. Common sense priors - priors from simple object tracking! Persistence, kinematics (constant velocity models), etc.
4. Causal reasoning - the proposed architecture attempts to discover causal structure in the environment to accelerate learning by explicitly maintaining sets of causal rules

A Q-learning agent is designed for their toy example. The state space consists of the different interactions between the learned symbolic abstractions of the environment. A tracking process is carried out separately from the agent for keeping track of the different symbolic abstractions. 

Main result: on random toy problem instances, DQN is not able to better than chance... Hypothesis: DQN relies on the fact that you should be able to internally learn a model for $p(s_{t+1}\|s_{t},a_{t})$ after going through a lot of examples. When this distribution is non-stationary, it can't! However, the proposed architecture doesn't seem to care about this. It instead directly is learning about object interactions.

### Methodology

Their environment is a simple B&W grid upon which shapes (O's, X's, and +'s) can be randomly positioned.

1. Low-level symbol generation: Uses a convolutional autoencoder to do simple dimensionality reduction and learn relevant features. Then, they do a form of unsupervised clustering by finding the maximally activated feature corresponding to each pixel, then thresholding these values. Once they have a sparse list of salient pixels, they form a spectrum with the activations across all features, and define a distance metric on the spectra via the sum of squared distances. This allows them to cluster pixels (objects) into certain categories.
2. Representation building: notions of spatial proximity, type-transitions between frames (including birth and death), neighborhood (number of neighbors), relative distances and positions
3. Reinforcement Learning: Agent is the '+', separate Q for interactions between different pairs of object types. State space describes different possible relations between two objects types. Seek to learn how to interact via (U, D, L, R) actions.





