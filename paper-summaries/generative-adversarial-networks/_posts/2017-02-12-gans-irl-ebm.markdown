---
layout: post
title: "A Connection Between Generative Adversarial Networks, Inverse Reinforcement Learning, and Energy-Based Models"
date: 2017-02-12
paper_ref: Finn, Christiano, Abbeel, Levine, 2016
redirect_from:
    - /paper-summaries/2017/02/12/gans-irl-ebm.html
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

Hence, the authors make the claim that for imitation learning and generative modeling, having both a "discriminator" as well as a "generator" encourages mode-seeking behavior. They show a connection between IRL and GANs by theoretically motivating an optimal IRL discriminator that learns the cost function, and an optimal IRL generator that is able to generate high-quality trajectories. It is assumed that one can sample from the generator density, i.e., that it is computable and can be held fixed while training the discriminator. The discriminator is modeled as a Boltzmann distribution with a parameterized energy function.
Since energy-based models are a more general form of the Maximum Entropy IRL problem, the authors also were able to show a direct connection between GANs and EBMs. 

No experiments are provided in this paper, so the efficacy of using GANs for IRL remain to be seen. 

Guided Cost Learning Demo: 

<iframe width="640" height="360" src="https://www.youtube.com/embed/hXxaepw0zAw" frameborder="0" allowfullscreen></iframe>

## Notes

In Section 2.3.2. Guided Cost Learning, we have the following importance sampling formulation of the cost function, where the data is modeled as a Boltzmann distribution:

$$
\begin{align}
\mathbb{L}_{cost} (\theta) &= \mathbb{E}_{\tau \sim p} \big[ - \log p_{\theta} (\tau) \big] = \mathbb{E}_{\tau \sim p} \big[ c_{\theta} (\tau) \big] + \log Z \nonumber \\

&= \mathbb{E}_{\tau \sim p} \big[ c_{\theta} (\tau) \big] + \log \bigg ( \int \frac{\exp(-c_{\theta})}{q(\tau)} q(\tau) d\tau \bigg) \nonumber \\

&= \mathbb{E}_{\tau \sim p} \big[ c_{\theta} (\tau) \big] + \log \bigg ( \mathbb{E}_{\tau \sim q} \bigg [\frac{\exp(-c_{\theta}(\tau))}{q(\tau)} \bigg ]\bigg). \nonumber

\end{align}
$$

We want our biased distribution $q(\tau) \propto \| \exp(-c_{\theta})(\tau)) \| = \exp(-c_{\theta}(\tau))$. This is the optimal importance sampling distribution that produces the importance sampling estimate of some function of a random variable $f(X)$ with minimal variance. It can be shown that $q*(x) \propto f(x) * p(x)$.

Importance sampling estimates suffer from high variance if the sampling distribution $q$ is biased. In Guided Cost Learning, to ensure $q$ samples from all trajectories $\tau$ with high values of $\exp(-c_{\theta}(\tau))$, the demonstration data samples (low cost as result of IRL objective) are mixed with the generated samples from $q$. Hence, $q$ is replaced with $\mu = \frac{1}{2}p + \frac{1}{2}q$ in the cost function.

In Section 3, the author's theoretical argument for comparing GANs and IRL begins by assuming that the discriminator can be written as 

$$
D_{\theta}(\tau) = \frac{\frac{1}{Z} \exp (-c_{\theta}(\tau))}{\frac{1}{Z} \exp (-c_{\theta}(\tau)) + q(\tau)}
$$

To see that is similar to the standard sigmoid binary classification loss, recall the identity

$$
f(x) = \frac{1}{1 + \exp(-x)} = \frac{\exp(x)}{1 + \exp(x)}.
$$

Let $\log Z$ be the bias of the sigmoid and notice that $\log q(\tau)$ is subtracted from the input. 

The author's argument continues by showing that this specific form of a GAN optimizes the same thing that MaximumEnt IRL does (pg. 6).

## Questions

* Being able to compute the generator's density and evaluate it cheaply enables this method, since you can then realistically learn an unbiased estimate of the partition function. What happens when the partition function remains biased?
* In Guided Cost Learning, what form does $q(\tau)$ take? Since it attaches a probability to a trajectory, it should have the same form as the demonstration distribution $p$...i.e., the input is a sequence of ($x_i$, $u_i$) and the output is a probability.
* The GAN training procedure minimizes the [Jensen-Shannon divergence](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence), which works sort of like the reverse-KL divergence. However, GANs don't try to fit as many modes of the data distribution as the model is able to- see [Section 3.2.5](https://arxiv.org/pdf/1701.00160.pdf) of Goodfellow's 2016 NIPS tutorial. In fact, this is in part a symptom of the mode collapse problem that GANs have. So, does training Guided Cost Learning/EBMs with GANs make them susceptible to this problem? The authors don't *really* discuss this, but it may only become apparent in practice. The motivation for the mixed sampling distribution for the importance sampling formulation seems to be realted to this. 