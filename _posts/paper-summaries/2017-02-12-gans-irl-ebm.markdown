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

In generative modeling, there is a trade-off between maximum-likelihood approaches that produce a moment-matching distribution that tries to "cover" all the modes of the unknown data distribution. This leads to a solution with probability mass in parts of the space that have negligible probability under the true distribution. In contrast, it may be preferable to estimate this unknown data distribution by "filling in" as many modes as possible; this effectively allows one to produce more realistic samples but with lower diversity. 

## Notes

In Section 2.3.2. Guided Cost Learning, we have the following importance sampling formulation of the cost function:

$$
\begin{align}
\mathbb{L}_{cost} (\theta) &= \mathbb{E}_{\tau \sim p} \big[ - \log p_{\theta} (\tau) \big] = \mathbb{E}_{\tau \sim p} \big[ c_{\theta} (\tau) \big] + \log Z \nonumber \\

&= \mathbb{E}_{\tau \sim p} \big[ c_{\theta} (\tau) \big] + \log \bigg ( \int \frac{\exp(-c_{\theta})}{q(\tau)} q(\tau) d\tau \bigg) \nonumber \\

&= \mathbb{E}_{\tau \sim p} \big[ c_{\theta} (\tau) \big] + \log \bigg ( \mathbb{E}_{\tau \sim q} \bigg [\frac{\exp(-c_{\theta}(\tau))}{q(\tau)} \bigg ]\bigg). \nonumber

\end{align}
$$

We want our biased distribution $q(\tau) \propto \| \exp(-c_{\theta})(\tau)) \| = \exp(-c_{\theta}(\tau)). 

## Questions
