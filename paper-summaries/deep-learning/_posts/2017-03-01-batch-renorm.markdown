---
layout: post
title: "Batch Renormalization-Towards Reducing Minibatch Dependence in Batch-Normalized Models"
date: 2017-03-01
paper_ref: Ioffe, 2017
redirect_from:
    - /paper-summaries/2017/03/01/batch-renorm.html
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

[{{ page.paper_ref }}](https://arxiv.org/abs/1702.03275)

## Summary

### BatchNorm

Batch Renormalization is a follow-up to the 2015 paper [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/pdf/1502.03167.pdf). The original motivation for BatchNorm came from the fact that the distribution of the inputs to each layer in a deep network changes throughout training as the parameters change. Since this slows down training, the authors reasoned that normalization of these distributions should allow for the use of higher learning rates and increased insensitivity to initializations. BatchNorm achieves the same accuracy as previous networks but with signifcantly fewer training steps.

BatchNorm is an added "layer" to deep networks placed after the output of the layer transformation (e.g., the convolution operation) but before the nonlinearity (e.g., a ReLu layer). During training, the sample estimates for the mean and variance of the layer's outputs are generated from mini-batch statistics. A moving average estimate is maintained as well, and is used during inference.

Some key points about BatchNorm:

* Normalization cannot be interleaved with gradient descent optimization. This is because the gradient descent optimization wouldn't be taking into account the fact that normalization takes place. BatchNorm requires backpropagation to compute derivatives for the normalization w.r.t. minibatch statistics; otherwise, model parameters explode without the loss decreasing.
* Full whitening of each layer's inputs is costly and not everywhere differentiable, so each scalar feature is whitened independently
* To prevent BatchNorm from changing what the network can represent, parameters are introduced that allow the BatchNorm layer to represent the identity transform. These parameters are also optimized with SGD

### BatchRenorm

BatchNorm came with pros and cons. It is less effective when the training minibatches are small or do not consist of independent samples. Small minibatches mean that the sample estimates of the mean and variance during training are less accurate. These inaccuracies are compounded with depth. For non-iid minibatches at train-time, BatchNorm will tend to overfit to the specific distribution of the examples; BatchRenorm aims to break up the dependence between similar samples.

Therefore, the goal of BatchRenorm is to provide the model with the capacity to overcome differences in activitations between training and inference. 

Essentially

* parameters $r$ and $d$ are introduced that relate the output of the normalizations between train time (computed with minibatch statistics) and inference (computed with population statistics for entire training set). If $\mu$ is an estimate of the mean of some particular node $x$, and $\sigma$ is an estimate of its standard deviation perhaps computed as a moving average over the last several minibatches, we have $$ \frac{x_i - \mu}{\sigma} = \frac{x_i - \mu_B}{\sigma_B} r + d\text{, where } r = \frac{\sigma_B}{\sigma}\text{,  }d = \frac{\mu_B - \mu}{\sigma}$$
* $r$ and $d$ are held constant during backprop
* This transform is identity in expectation, and BatchNorm is $r = 1$, $d = 0$.

This allows the layers to observe the "correct" activiations that would be seen during inference. In practice, you start with BatchNorm for a few thousand training steps, then switch to BatchRenorm.

## Questions for discussion

* What is the *cost* of BatchRenorm? Slightly more model complexity because of the added $r$ and $d$, and slightly more complex backprop equations? Hyper-parameter search needed for $r_max$ and $d_max$?

* Doesn't seem to always be necessary to use BatchRenorm - in real world problems, however, training data probably won't be "nice" and iid

* [BatchNorm for Recurrent Networks](https://arxiv.org/abs/1603.09025)? 

* This was used in Deep Reinforcement Learning to stabilize policy gradient methods! 