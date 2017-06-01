---
layout: post
title: "Recurrent Environment Simulators"
date: 2017-05-31
category: paper-summaries
paper_ref: Chiappa, et. al., 2017
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

[{{page.paper_ref}}](https://arxiv.org/abs/1704.02254)

## Summary

This paper extends the results on action-conditional video prediction from [Oh, et. al., 2015](https://arxiv.org/abs/1507.08750). The motivation behind this line of research is to investigate whether training RL agents to learn how their actions affect the environment reduces the amount of time they spend in exploration. The authors outline the following main challenges:

1. The properties of generalization and sensitivity to model structure of these methods are poorly understood.
2. Accurate prediction for long time periods into the future is hard
3. Models that predict the high-dim image directly each time an action is taken are inefficient

The general approach is to use a Conv-RNN to take an observation from the environment and produce a high-dim state representation. This high-dim state representation can be combined with the action taken by the agent to predict how the environment will react. 

One of the main contributions of this work is fusing the action with the hidden state representation when predicting the next hidden state representation in time. In previous work, the action was used to directly predict the next image. Why? Authors suggest it could "enable the model to incorporate action informatio more effectively".

Using observations from the environment forces the agent to make predictions only when the next frame is available - rolling forward the agent's own predictions in the future allows it to predict many time steps ahead in a more efficient manner. 

**Prediction-dependent transitions** are ones of the form $$ s_t = f(s_{t-1}, a_{t-1}, C(\mathbb{I}(\hat x_{t-1}, x_{t-1}))) $$ where $s_t$ is the hidden state representation. 

There's a trade-off between short- and long-term accuracy and prediction-dependent vs -independent transitions.