---
layout: post
title: "What Can Neural Networks Reason About?" 
date: 2020-03-22
paper_ref: Xu, Li, Zhang, Du, Kawarabayashi, Jegelka, 2020
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

[{{page.paper_ref}}](https://openreview.net/forum?id=rJxbJeHFPS)

## Summary

This work proposes a theory they call "algorithmic alignment" to explain why some classes of neural net architectures generalize much better than others on certain reasoning problems. They use PAC learning to derive sample complexity bounds that show that the number of samples needed to achieve a desired amount of generalization increases when certain subproblems are "hard" to learn.

For example, they empirically show that DeepSets can easily learn summary statistics for a set of numbers, like "max" or "min". Since a single MLP has to learn the aggregation function (an easy subproblem) plus the for loop over all elements (a harder subproblem), their theory suggests that the number of samples required to acheive good generalization at test time is much higher for the MLP, which their experiments confirm. Interestingly, they explain why graph neural nets (GNNs) align well with dynamic programming (DP) problems (because of their iterative message-passing style updates), but then also explain why they do not align well with NP-Hard problems. They provide further experimental evidence on a shortest-paths DP problem and Subset-Sum NP-Hard problem to verify this.

## What About Transformers?

The paper doesn't discuss Transformers, so as a simple exercise, I thought about how it fits into their framework. [Transformers map readily onto fully connected GNNs](https://graphdeeplearning.github.io/post/transformers-are-gnns/), which suggests that they should "align algorithmically" with DP problems but not NP-Hard problems. Note that for a set of $K$ objects, a multi-head attention Transformer/GNN performs an $O(K^2 d)$ operation. This highlights one limitation of Transformers; they can reason about object-object relations, but not higher order relations such as object-object-object. Relational reasoning over $k$-partite graphs, $k > 2$, show up in certain NP-Hard problems like [Multidimensional Assignment](https://pubsonline.informs.org/doi/pdf/10.1287/opre.16.2.422). It seems like algorithm alignment will certainly be useful for future research on designing neural net architectures for NP-Hard problems.