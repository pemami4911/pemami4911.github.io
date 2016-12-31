---
layout: post
title: "Linear Least-Squares Algorithms for Temporal Difference Learning"
date: 2016-12-30
category: paper-summaries
paper_ref: Bradtke, Barto, 1996
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

[{{ page.paper_ref }}](http://scholarworks.umass.edu/cgi/viewcontent.cgi?article=1016&context=cs_faculty_pubs)

## Summary

### A Brief Description of TD-Lambda

In TD($\lambda$), a parameterized linear function approximator is used to represent the value function. 
The parameter update for vector $\theta_{t}$ is:

$$
\begin{equation}

\theta_{t+1} = \theta_{t} + \alpha_{\eta(x_{t})} \big [ R_{t} + \gamma V_{t}(x_{t+1} - V_{t} \big ] \sum_{k=1}^{t} \lambda^{t-k} \nabla_{\theta_{t}} V_{t}(x_k)

\end{equation}
$$

It is important that $V_{t}$ be linear in the parameter vector $\theta_{t}$ and $\lambda \neq 0$ so that $\nabla_{\theta_{t}} V_{t}(x_k)$ does not depend on $\theta_{t}$. This allows for an efficient, recursive algorithm to be derived to compute the sum at the end of Equation (1). 

{%
    include image.html
    img="/assets/td-lambda.png"
    caption="Episodic TD-Lambda algorithm. The parameter vector is updated only at the end of the episode"
%}

Daya and Sejnowski (1994) proved parameter convergence with probability 1 under these conditions for TD($\lambda$) applied to absorbing Markov chains in a episodic-setting (i.e., offline).

Bradtke (1994) introduced a normalized version of TD(0) to solve instabilities in the learning algorithm caused by the size of the input vectors $\phi_{x}$

### LSTD

The general problem consists of a system with inputs $\hat \omega_{t} = \omega_{t} + \zeta_{t}$ where $\zeta_{t}$ is the input observation noise at time $t$. For a linear function approximator $\Psi$, we have 

$$
\begin{align}
\psi_{t} &= \Psi(\hat \omega_{t} - \zeta_{t}) + \eta_{t} \\
         &= \hat \omega_{t}^{\intercal} \theta^{*} - \zeta_{t}^{\intercal} + \eta_{t}
\end{align}
$$

We introduce an *instrumental variable* $\rho_{t}$, which is a vector that is correlated with the true input vectors, $\omega_{t}$, but that is uncorrelated with the observation noise, $\zeta_{t}$. Solving the linear-least squares equation by taking the gradient of the quadratic objective function results in this parameter estimate:

$$
\begin{equation}

\theta_{t} = \bigg [ \frac{1}{t} \sum_{k=1}^{t} \rho_{k}\hat\omega_{k}^{\intercal} \bigg ]^{-1} \bigg [ \frac{1}{t} \sum_{k=1}^{t} \rho_{k} \psi_{k} \bigg].

\end{equation}
$$

The correlation matrix $Cor(\rho, \omega)$ must be nonsingular and finite, the correlation matrix $Cor(\rho, \zeta)$ = 0, and the output observation noise $\eta_{t}$ must be uncorrelated with the instrumental variable for $\theta_{t}$ to converge with probability 1 to $\theta^{*}$
## Takeaways
