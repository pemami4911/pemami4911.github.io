---
layout: post
title:  "A Note on Bayesian Recursive Filters"
date:   2017-08-20
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

## Introduction 

In this post, I will be presenting the mathematics at the core of the Kalman filter and particle filter. These algorithms are commonplace in target tracking applications, and there exist many other resources that describe these algorithms and provide implementations in your favorite scientific programming language *TODO* {cite, cite, cite}. I will instead focus on illuminating the intuition found within the two filter's derivations to give the curious reader the ability to do a lot more than just copy and paste their equations.

## A Motivating Example

Suppose your self-driving car has a forward-facing radar that it is using for tracking vehicles driving in front of it. One can imagine that this would be especially useful for fusing with the perception stack of an advanced driver assistance systems (ADAS). 

{%
    include image.html
    img="/img/bayes_filters/radar_tracking.PNG"
    caption="Tracks from a multi-sensor fusion system powering an ADAS [1]"
%}

Lets say that your radar provides you with detections at a rate of 30 Hz. We'll let each detection be defined as

$$
\begin{equation}
z_t = \begin{bmatrix}
       r_t \\
       \theta_t \\
       \end{bmatrix}
\end{equation}
$$

where $r_t$ is the range (longitudinal distance) in meters from your sensor to the vehicle in front of you, and $\theta_t$ is the yaw angle in radians. This seems straightforward enough; you decide to power on your radar and collect some data... Not so fast! You observe that your recorded data looks something like this: 

{%
    include image.html
    img="/img/bayes_filters/noisy_radar.png"
%}

That's not too useful; your ADAS needs extremely precise measurements to make safe driving decisions. It looks like your detections are being corrupted by additive Gaussian noise, which means we can directly model the effects of the noise as follows:

$$
\begin{equation}

\end{equation}
$$

## Bayesian Recursive Filters

Both the Kalman filter and the particle filter fall under the category of Bayesian recursive filters. We'll begin our discussion by looking carefully at what this means. 

We can use a very simple probabilistic graphical model to represent the evolution of the state. 

### Markov Assumption

<a name="References"></a>

## References

1. Chavez-Garcia, Ricardo Omar, and Olivier Aycard. "Multiple sensor fusion and classification for moving object detection and tracking." IEEE Transactions on Intelligent Transportation Systems 17.2 (2016): 525-534.




