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

It is desirable for an agent to symbolically reason about its environment, in order to expediate the process of learning optimal behaviors. However, "classic" symbolic AI suffers from the **symbol grounding problem**, which is that symbolic elements have traditionally been hand-crafted, and hence, brittle. Deep Learning can be used to automatically learn optimal "symbols", upon which a reinforcement learning agent could learn behaviors motivated by these learned symbols. 

The aspects of AI that this work focuses on are closely related to those proposed in the manifesto written by [Lake et. al.](http://pemami4911.github.io/paper-summaries/general-ai/2016/05/13/learning-to-think.html). There are also nods to [Douglas Hofstadter's](http://cogs.indiana.edu/people/profile.php?u=dughof) work on analogy as being the main driving force behind intelligence, as well as [Marcus Hutter's](http://www.hutter1.net/) Universal Artificial Intelligence work.

1. Conceptual abstraction - agents can use abstractions to make analogies and hence learn optimal behaviors faster
2. Compositional structure - probabilistic first-order logic provides the underlying framework for a representation medium that is compositional
3. Common sense priors - priors from simple object tracking! Persistence, kinematics (constant velocity models), etc.
4. Causal reasoning - the proposed architecture attempts to discover causal structure in the environment to accelerate learning by explicitly maintaining sets of causal rules

A Q-learning agent is designed for their toy example. The state space consists of the different interactions between the learned symbolic abstractions of the environment. A tracking process is carried out separately from the agent for keeping track of the different symbolic abstractions. 

Main result: on random toy problem instances, DQN is not able to better than chance... Hypothesis: DQN relies on the fact that you should be able to internally learn a model for $p(s_{t+1}\|s_{t},a_{t})$ after going through a lot of examples. When this distribution is non-stationary, it can't! However, the proposed architecture doesn't seem to care about this. It instead directly is learning about object interactions.



