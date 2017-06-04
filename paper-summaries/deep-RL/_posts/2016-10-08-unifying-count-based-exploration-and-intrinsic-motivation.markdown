---
layout: post
title:	"Unifying Count-Based Exploration and Intrinsic Motivation"
date: 	2016-10-08 1:00 PM
paper_ref: Bellemare, et al., 2016
redirect_from: 
    - /paper-summaries/2017/10/08/unifying-count-based-exploration-and-intrinsic-motivation.html
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
[{{ page.paper_ref }}](https://arxiv.org/abs/1606.01868)


# Summary

This paper presents a novel RL exploration bonus based on an adaptation of count-based exploration for high-dimensional spaces. The main contribution is the derivation of the relationships between *prediction gain* (PG), a quantity called the *pseudo-count*, and the well-known *information gain* from the intrinsic RL literature. The overall presentation is clear and precise, especially when it comes to defining notation and explaining the core concepts. The authors use results from prior work on applying count-based exploration in complex domains, so reading this paper without having that background is a bit challenging (see the bibliography for recent papers by Bellemare and Veness on this topic). These results will help make previous count-based exploration methods, such as those devised around the idea of *optimism in the face of uncertainty*, viable for high-dimensional problems.

## Quick Definitions

This paper presents the following definitions and notation, along with theoretical results about their properties, in a rich manner. I will simply present definitions necessary for understanding the main contribution here; please see the paper for further details. 

1. $ \mathcal{X} := $ finite or countable alphabet, with sub-sequences of length $n$ denoted by $x_{1:n} \in \mathcal{X}^n $
2. A *sequential density model* over $\mathcal{X}$ is a mapping from finite sub-sequences to probalitiy distributions over $\mathcal{X}$. Denote these distributions by $\rho_{n}(x) := \rho(x ; x_{1:n})$
3. The *recoding probability* of a symbol $x$ is denoted by $\rho_{n}^{\prime} := \rho(x ; x_{1:n}x)$. That is, the probability assigned to $x$ by our sequential density model after observing a new occurence of $x$
4. $ \hat{N}(x) := $ the pseudo-count function
5. $ \hat{n} := $ the pseudo-count total

## Main Result

The following equations summarize the main results presented in this paper.

The authors relate the pseudo-count function and the pseudo-count total as follows. 

$$
\begin{equation}
\rho_{n}(x) = \frac{\hat{N}(x)}{\hat{n}} \qquad\text{and}\qquad
\rho_{n}^{\prime} = \frac{\hat{N}(x) + 1}{\hat{n} + 1}
\end{equation}
$$

From (1), we can write: 

$$
\begin{equation}
\hat{N}(x) = \frac{
	\rho_{n}(x)(1 - \rho_{n}^{\prime}(x))
}{
	\rho_{n}^{\prime}(x) - \rho_{n}(x)
}

\end{equation}
$$

By choosing an appropriate sequential density model, such as a graphical model. See the appendix of the paper for the description of the CTS model used by the authors in the experimentation; this model treats a 42 x 42 processed image as a factorizable observation, computing the probability of the image $x$ as the product of the probabilities of each (i, j) pixel. These pixel probabilities are computed via the neighbors of that pixel. See section 5.2 as well for a discussion on using directed graphical models as sequential density models. 

The prediction gain is defined as 

$$
\begin{equation}
PG_{n}(x) := \log \rho_{n}^{\prime}(x) - \log \rho_{n}(x)
\end{equation}
$$

For the information gain (IG) defined as the change in posterior w.r.t. the KL-divergence within a mixture model $\xi$ defined over a class $\mathcal{M}$ of sequential density models, we have: 

$$
\begin{equation}
IG_{n}(x) \le PG_{n}(x) \le \hat{N}(x)^{-1}
\end{equation}
$$

The reward bonus proposed in this paper is as follows: 

$$
\begin{equation}
R_{n}^{+}(x, a) := \beta(\hat{N}(x) + 0.01)^{-1/2} ,
\end{equation}
$$

with $\beta$ = 0.05 selected from a short parameter sweep and the small added constant for numerical stability. The authors compared different forms of this bonus, using $\hat{N}(x)^{-1}$ and $PG_{n}(x)$. 

# Notes

They implemented their exploration as a reward bonus for Double-DQN and [A3C](http://pemami4911.github.io/paper-summaries/2016/08/02/A3C.html), and were able to show significant improvements on many Atari tasks. Most notably, they achieved the highest score to date on Montezuma's Revenge. I am very intrigued by this result; without using some form of memory such as an LSTM to "remember" long-term behaviors, their agent was able to explore efficiently enough to learn how to achieve the hierarchical sub-goals required to visit most of the rooms and achieve high scores. One of the main benefits of *prediction gain* and *pseudo-counts* is that the agent is able to recognize and adjust its behaviors efficiently to salient events, which clearly plays a major role in solving games like Montezuma's Revenge. A convolutional neural net used to represent the value function for an Atari game must have a very large learning capacity, which is normally under-utilized when it comes to "hard" games due to the inefficiency of $\epsilon$-greedy exploration. For example, Montezuma's Revenge has 23 total rooms the agent is able to visit; the authors showed that the agent tends to only visit about 2 of these rooms without the reward bonus. After 100 million frames of training on Montezuma's Revenge with the suggested bonus, the agent had visited about 15 of these rooms! The CNN that uses a reward bonus must be learning representations from within all or most of the rooms, and encoding them in its hidden layers. Even though Montezuma's Revenge is partially observable, the agent is able to "remember" how to do the sub-tasks just by eventually stumbling upon the sparse rewards and cleverly updating its Q-values by means of the bonus. I would like to see what representations were encoded by the hidden layers of the network after training. Perhaps using a recurrent network and/or memory with attention + the reward bonus would help improve the learning speed, so that the sequential nature of the sub-tasks within the game can be encoded more readily.
     
It would be nice to see this approach compared with [VIME](http://pemami4911.github.io/paper-summaries/2016/09/04/VIME.html). VIME computes the amount of information gained about the dynamics model due to the agent taking an action and seeing a certain following state. The authors show that the results should be similar, as maximizing the information gain also maximizes a lower bound on the inverse of the pseudo count. 

The authors mention that other sequential density models with more sophistication could be used, as opposed to the simple CTS model. There clearly is a trade-off, however, such that more complex sequential density models would increase the time and space complexity significantly. For example, [Oh, et al., 2015](https://arxiv.org/abs/1507.08750) designed a recurrent convolutional neural network architecture to predict future frames from a video sequence of an Atari game. They estimated the visitation frequency of a predicted frame by an empirical distribution over the contents of the replay memory; the count was computed using a gaussian kernel that provided a distance metric between frames. This was used as an exploration bonus.    

The authors presented the appropriate metrics and figures to convince the reader of the effectiveness of their solution. They tested it widely on many (~60) Atari games to prove its widespread impact. (On a related note, it makes the difficulty for researchers that do not have access to the computational resources that DeepMind does to carry out such extensive experimentation all the more apparent!).