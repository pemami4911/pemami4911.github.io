---
layout: post
title:  "[DRAFT] On the difficulty of reinforcement learning"
date:   2017-01-05
category: blog
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

# Outline

## Topics to touch on

1. Classic results on the complexity of MDPs and POMDPs
2. The distinction of various kinds of POMDPs, and why some are harder than others
3. Speculation on how bad the quality of our solutions are when the # of observations is very large, or continuous
3. Why many problems that RL is being applied on today, and ultimately real world problems, are varients of POMDPs
4. The main issues with RL that were tackled in 2016 and their respective solutions (Auxiliary tasks, transfer learning, better exploration - underappreciated VIME, Value Iteration Networks - Model-based and model-free being too restrictive)
Bad objective functions? Sparse rewards? Inverse reinforcement learning??
5. What is the next big challenge (Starcraft II)? Is Deep RL enough? Curriculum learning, unsupervised learning, auxiliary tasks, etc. Planning (lookahead / model-based) vs model-free 
6. What else needs to be done to make a significant jump in the field? Paradigm shift