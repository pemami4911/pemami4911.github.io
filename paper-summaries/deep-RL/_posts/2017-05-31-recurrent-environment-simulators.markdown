---
layout: post
title: "Recurrent Environment Simulators"
date: 2017-05-31
paper_ref: Chiappa, et. al., 2017
redirect_from:
    - /paper-summaries/2017/05/31/recurrent-environment-simulators.html
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

1. The properties of generalization and sensitivity to model structure of these methods are poorly understood
2. Accurate prediction for long time periods into the future is hard
3. Models that predict the high-dim image directly each time an action is taken are inefficient

The general approach is to use a Conv-RNN to take an observation from the environment and produce a high-dim state representation. This high-dim state representation can be combined with the action taken by the agent to predict how the environment will change. In other words, the goal is to learn a parametric model that approximates the state-action transition. 

One of the main contributions of this work is fusing the action with the hidden state representation when predicting the next hidden state representation in time. In previous work, the action was used instead to directly predict the next image. Why? Authors suggest it could "enable the model to incorporate action information more effectively".

Using observations directly from the environment to predict the next hidden state representation forces the agent to make predictions only when the next frame is available, i.e., 1-step prediction. Rolling forward the agent's own predictions in the future allows it to predict many time steps ahead in a more efficient manner. 

**Prediction-dependent transitions** are ones of the form $$ s_t = f(s_{t-1}, a_{t-1}, C(\mathbb{I}(\hat x_{t-1}, x_{t-1}))) $$ where $s_t$ is the hidden state representation. 

There's a trade-off between short- and long-term accuracy and prediction- vs observation-dependent transitions. When prediction-dependent transitions are mostly used, the agent learns better global dynamics of the game and can do better with long-term accuracy. When observation-dependent transitions are mixed with prediction-dependent, the agent pays more attention to details that provide it with better short-term accuracy.  

They evaluated their model on Breakout, Freeway, and Pong by replacing the real game with the learned environment simulator. A human would "play" the game, and the learned simulator would return the next frame given the action input by the human.

## Related works

* [Action-conditional Video Prediction](http://papers.nips.cc/paper/5859-action-conditional-video-prediction-using-deep-networks-in-atari-games)
* [UNREAL](https://arxiv.org/pdf/1611.05397.pdf)
* [Learning to Act By Predicting the Future](https://blog.acolyer.org/2017/05/12/learning-to-act-by-predicting-the-future/)

