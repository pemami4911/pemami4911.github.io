---
layout: post 
title: Learning From Demonstrations in the Wild
date: 2018-12-26
paper_ref: Behbahani et al., 2018 
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

[{{page.paper_ref}}](https://arxiv.org/abs/1811.03516v1)

## Summary

The motivation behind this work is to develop an automated process for learning the behaviors of road users from large amounts of unlabeled video data. A generative model (trained policy) of road user behavior could be used within a larger traffic scene understanding pipeline. In this paper, they propose Horizon GAIL, an imitation-learning algorithm based on GAIL, that stabilizes learning from demonstration (LfD) over long horizons. Expert policy demonstrations are provided by a slightly improved Deep SORT tracker, and they use PPO as the "student" RL algorithm. The Unity game engine is used to build an RL env that mimcs the scene from the real-world environment to rollout their PPO Horizon-GAIL agent. Their experiments are on 850 minutes of traffic camera data of a large roundabout. By using a curriculum where the episode horizon is extended by 1 timestep each training epoch, they demonstrated how Horizon-GAIL can match the expert policy's state/action distribution much more closely than GAIL, PS-GAIL, and behavior cloning while also improving on training stability.

## Observations

* The ability to auto-generate the Unity env from Google Maps would be crucial to scaling this technique up. maps2sim?
* They provided an empirical comparison of DeepSORT with ViBe's vision tracker, and showed that running the Kalman Filter in 3D space improved Deep SORT's performance in multiple multi-object tracking metrics by a few percentage points
* Each road user is modeled independently, i.e., the policy does not account for other agents in the environment explicitly. It looks like the policy used for learning vehicle and pedestrian behavior is the same, although because of the Mask R-CNN detector, they are able to differentiate between the two classes. In scenarios where the behaviors exhibited by the road users can be highly unpredictable and diverse (a busy traffic intersection with heavy pedestrian presence), perhaps a hierarchical policy could be useful that conditions on the inferred object class.
* Interesting future work might include incorporating multi-agent modeling in the RL framework for more complex traffic scenarios.