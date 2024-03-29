---
layout: post
title: "Tracking Occluded Objects and Recovering Incomplete Trajectories by Reasoning about Containment Relations and Human Actions"
date: 2018-06-03
paper_ref: Liang, Zhu, Zhu, 2018
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

[{{page.paper_ref}}](https://pdfs.semanticscholar.org/4170/0dc1e60f5c8eaef409ef014f37c8b9e1b8cd.pdf)

## Summary

This paper looks at tracking severely occluded objects in long video sequences.

I like this passage:
```
Although some recent work adopted deep neural networks
to extract contexts for object detection and tracking, these
data-driven feedforward methods have well-known problems:
i) They are black-box models that cannot be explained
and only applicable with supervised training by fitting the
typical context of the object, thus difficult to generalize
to new tasks. ii) Lacking explicit representation to handle
occlusions, low resolution, and lighting variations—there
are millions of ways to occlude an object in a given image
 (Wang et al. 2017), making it impossible to have enough
data for training and testing such black box models. In this
paper, we go beyond passive recognition by reasoning about
time-varying containment relations.
```

They look at *containment relations* induced by human activity. A containment relation occurs when an object contains or holds another object, obscuring it from view. Contained objects have the same trajectories as the container.

They use an idea that I have thought about as well and think is powerful; rather than only relying on detections for next state hypotheses, they suggest alternative hypotheses based on occlusion reasoning. The other hypotheses come from containment relations and blocked relations; if an object is contained, it inherits the track state of its container. If an object is blocked, its track state is considered stationary (not always true!). 

This tracking scenario is unique because they only consider human action as the source of state change (i.e., this approach doesn't apply to general ped or vehicle tracking).

They use state-of-the-art detection and activity recognition to carry out object tracking. They use the network flow approach for occlusion-aware data association in a sliding window. I think their algorithm has to decide between containment and blocked occlusion events via the activity recognition.

They note that their approach is limited by how good object detection is. I think an important direction to consider is when external forces other than people can act on the object. This requires a lot more complex modeling of what an occluded object might be doing. Also, we need better object detection!

## Interesting related works

In [Zhang, Li, and Nevatia 2008](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=4587584), they use an Explicit Occlusion Model (EOM) in the network flow data association model. Good potential baseline.