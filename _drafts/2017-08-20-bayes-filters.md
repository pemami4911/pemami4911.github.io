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

In this post, I will be going over the mathematics at the core of the Kalman filter (warning: math/probability heavy post!). This is the most commonplace algorithm in target-tracking applications. There are many other resources out there that describes it and provides code in your favorite programming language *TODO* {cite, cite, cite}. Instead, I'm going to focus on illuminating the intuition that motivates the theory, to give the curious reader a deeper understanding.

## A Motivating Example

Suppose your self-driving car has a forward-facing radar that it is using for tracking vehicles driving in front of it. One can imagine that this would be especially useful for fusing with other sensors, like a stereo camera, in the perception stack of an advanced driver assistance system (ADAS). 

{%
    include image.html
    img="/img/bayes_filters/radar_tracking.PNG"
    caption="Tracks from a multi-sensor fusion system powering an ADAS [1]"
%}

Lets say that your radar provides you with discrete-time detections at a rate of 30 Hz. We'll let each detection be defined as

$$
\begin{equation}
z_t = \begin{bmatrix}
       r_t \\
       \theta_t \\
       \end{bmatrix}
\end{equation}
$$

where $r_t$ is the range (longitudinal distance) in meters from your sensor to the vehicle in front of you, and $\theta_t$ is the yaw angle in radians. This seems straightforward enough- you power on your sensors and collect some data of a car driving in front of you... and you observe that your recorded data looks something like this: 

{%
    include image.html
    img="/img/bayes_filters/noisy_radar.png"
%}

That's not too useful. Your ADAS needs extremely precise measurements so your self-driving vehicle can make safe driving decisions. It looks like your detections are being corrupted by additive Gaussian noise, which means we can directly model the effects of the noise on our measurements as follows:

$$
\begin{equation}
\hat{z_t} = z_t + \nu
\end{equation}
$$

where $\nu \sim N(0, R)$, i.e., $\nu$ is distributed according to a stationary (it doesn't vary over time) mean-zero Gaussian distribution with covariance $R$. 

The noisy measurement $\hat{z_t}$ informs us about the *state* $x_t$ of the car we're tracking. To keep our problem simple, we'll use a 2-D coordinate system where the bottom-center of our vehicle is $(0, 0)$, and the position of the car we're tracking is given by a coordinate-pair $(x, y)$. Using some trigonometry, you could convert our noisy measurement provided by the radar into an estimate of this car's position. Since the conversion from the polar coordinates of the radar measurement to the coordinate system of the system state is nonlinear, in truth we would need to use something called the *Extended Kalman Filter* **TODO** {cite}. We'll ignore that in this post, since handling nonlinearity is not our focus today.

The Kalman Filter is a linear-Gaussian state-space model that provides us with a principled way of *filtering* out the noise from the radar measurement. Given this filtered measurement, it then uses it to update its estimate of the state of the car being tracked. 

## Bayesian Recursive Filters

The Kalman Filter falls under the broad category of Bayesian recursive filters. We'll begin our discussion by looking carefully at what this means. 

### Markov Assumption

There are a number of modeling assumptions that the Kalman Filter makes about the system. First and foremost, the Kalman Filter attempts to model the discrete-time evolution of the state of the system as a Markov chain. The **Markov Assumption** of a Markov chain states that the probability of transitioning to a future state is conditionally independent of the past states given the present. Likewise, the probability of receiving a measurement is conditionally independent of past states and measurements given the current state. This is depicted graphically in the figure below. 

{%
  include image.html
  img="/img/bayes_filters/KF_Markov.png"
  caption="The probability of the next state of the system is conditionally independent on all of the past states given the present"
%}

At time $t$, you have that $p(z_t \| x_1, ... x_t) = p(z_t \| x_t)$ and $p(x_t \| x_1, ..., x_t) = p(x_t \| x_t-1)$.

<a name="References"></a>

## References

1. Chavez-Garcia, Ricardo Omar, and Olivier Aycard. "Multiple sensor fusion and classification for moving object detection and tracking." IEEE Transactions on Intelligent Transportation Systems 17.2 (2016): 525-534.




