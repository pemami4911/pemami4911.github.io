---
layout: post
title: "A Connection Between Generative Adversarial Networks, Inverse Reinforcement Learning, and Energy-Based Models"
date: 2017-02-12
category: paper-summaries
paper_ref: Finn, Christiano, Abbeel, Levine, 2016
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

[{{ page.paper_ref }}](https://arxiv.org/abs/1611.03852)

## Summary

In generative modeling, there is a trade-off between maximum-likelihood approaches that produce a moment-matching distribution that try to "cover" all the modes of the unknown data distribution as opposed to approaches that estimate the unknown data distribution by "filling in" as many modes as possible. The latter effectively allows one to produce more realistic samples but with lower diversity, while the former leads to a solution with probability mass in parts of the space that have negligible probability under the true distribution. 

Hence, the authors make the claim that for imitation learning and generative modeling, having both a "discriminator" as well as a "generator" encourages mode-seeking behavior. They show a connection between IRL and GANs by theoretically motivating an optimal IRL discriminator that learns the optimal cost function, and an optimal IRL generator that is able to generate high-quality trajectories. The key here is formulating the discriminator so that it only needs to estimate a single distribution (it is assumed that one can sample from the generator density, e.g., it is fixed), and this single distribution is modeled as a Boltzmann distribution with a parameterized energy function.

Since energy-based models are a more general form of the Maximum Entropy IRL problem, the authors also were able to show a direct connection between GANs and EBMs. Since the primary challenge of training EBMs is estimating the partition function from the Boltzmann distribution, it is shown how GANs can be used to derive unbiased estimates. Specifically, the generator is trained to produce samples with minimal energy from the data, and the discriminator acts as parameterized energy function whose objective is to maximize the log likelihood of the data. From the two learned distributions, the partition function can be estimated.     

## Notes

In Section 2.3.2. Guided Cost Learning, we have the following importance sampling formulation of the cost function, where the data is modeled as a Boltzmann distribution:

$$
\begin{align}
\mathbb{L}_{cost} (\theta) &= \mathbb{E}_{\tau \sim p} \big[ - \log p_{\theta} (\tau) \big] = \mathbb{E}_{\tau \sim p} \big[ c_{\theta} (\tau) \big] + \log Z \nonumber \\

&= \mathbb{E}_{\tau \sim p} \big[ c_{\theta} (\tau) \big] + \log \bigg ( \int \frac{\exp(-c_{\theta})}{q(\tau)} q(\tau) d\tau \bigg) \nonumber \\

&= \mathbb{E}_{\tau \sim p} \big[ c_{\theta} (\tau) \big] + \log \bigg ( \mathbb{E}_{\tau \sim q} \bigg [\frac{\exp(-c_{\theta}(\tau))}{q(\tau)} \bigg ]\bigg). \nonumber

\end{align}
$$

We want our biased distribution $q(\tau) \propto \| \exp(-c_{\theta})(\tau)) \| = \exp(-c_{\theta}(\tau))$. 

## Questions

