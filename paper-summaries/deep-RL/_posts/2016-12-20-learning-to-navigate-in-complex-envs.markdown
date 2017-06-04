---
layout: post
title: "Learning To Navigate in Complex Environments"
date: 2016-12-20
paper_ref: Mirowski, et. al., 2016
redirect_from:
    - /paper-summaries/2016/12/20/learning-to-navigate-in-complex-envs.html
---
---
[{{ page.paper_ref }}](https://arxiv.org/pdf/1611.03673v2.pdf)

## Summary

A primary goal of this work is to incorporate the learning of complex navigation into the RL problem.
Auxiliary tasks are used to augment the loss to provide denser training signals. The first auxiliary task is reconstruction of a low-dimensional depth map. The second task is self-supervised; the agent is trained to predict if the current location has been previously visited within a local trajectory.

*"The agent is trained by applying a weighted sum of the gradients coming from A3C, the gradients from depth prediction, and ther gradients from the loop closure"*

*"In particular if the prediction loss shares representation with the policy, it could help build useful features for RL much faster, bootstrapping learning"* >> This is interesting, and a bit confusing. It seems like this is generalizing from the observation that including depth prediction in the loss was superior to directly using it as an input. I'm not sure if this is always true, since it seems hard to quantify/evaluate this.

It's pretty cool that they're incorporating aspects of SLAM- penalizing loop closures for efficient exploration.

The authors test a couple different variations on a 3D maze navigation task. They use dynamic mazes and multiple goals to increase the difficulty. The A3C-variant with both auxiliary tasks performed the best on the most difficult tasks. The auxiliary tasks were shown to improve data efficiency.

## Takeaways

* Engineering auxiliary tasks into the loss is an interesting direction. This won't scale on its own for more complex tasks beyond navigation, but can potentially be used in conjunction with transfer learning.

* How does this compare with SOTA SLAM-and-RRT motion-planners? I would like to see this implemented on some robots!

* Cool, but still relies on RL methods based on data-inefficient and high-variance algorithms (A3C)