---
layout: post
title:	"Prioritized Experience Replay"
date: 	2016-01-26 2:20 PM
paper_ref: Schaul, Quan, Antonoglou, Silver, 2016
redirect_from: 
    - /papersummaries/2016/01/26/prioritizing-experience-replay.html
    - /paper_summaries/2016/01/26/prioritizing-experience-replay.html  
    - /paper-summaries/2016/01/26/prioritizing-experience-replay.html
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

[{{ page.paper_ref }}](http://arxiv.org/pdf/1511.05952.pdf)

## Summary ##
Uniform sampling from replay memories is not an efficient way to learn. Rather, using a clever prioritization scheme to label the experiences in replay memory, learning can be carried out much faster and more effectively. However, certain biases are introduced by this non-uniform sampling; hence, weighted importance sampling must be employed in order to correct for this. It is shown through experimentation with the Atari Learning Environment that prioritized sampling with Double DQN significantly outperforms the previous state-of-the-art Atari results.

## Evidence ## 
* Implemented Double DQN with main changes being the addition of prioritized experience replay sampling and importance-sampling 
* Tested on Atari Learning Environment

## Strengths ## 
* Lots of insight about the repercussions of this research and plenty of discussion on extensions

## Notes ## 
* The magnitude of the TD-error indicates how unexpected a certain transition was
* The TD-error can be a poor estimate about the amount an agent can learn from a transition when rewards are noisy
* Problems with greedily selecting experiences: 
	* High-error transitions are replayed too frequently
	* Low-error transitions are almost entirely ignored
	* Expensive to update entire replay memory, so errors are only updated for transitions that are replayed
	* Lack of diversity leads to over-fitting
* A stochastic sampling method is introduced which finds a balance between greedy prioritization and random sampling (current method)
* Two variants of $$ P(i) = \frac{p^{\alpha}_i}{\sum_k p^{\alpha}_k} $$ were studied, where $P$ is the probability of sampling transition $i$, $p_i > 0$ is the priority of transition $i$, and the exponent $\alpha$ determines how much prioritization is used, with $\alpha = 0$ the uniform case
	* Variant 1: proportional prioritization, where $p_i = \| \delta_i\| + \epsilon$ is used and $\epsilon$ is a small positive constant that prevents the edge-case of transitions not being revisited once their error is zero. $\delta$ is the TD-error
	* Variant 2: rank-based prioritization, with $p_i = \frac{1}{rank(i)}$ where $rank(i)$ is the rank of transition $i$ when the replay memory is sorted according to $\delta_i$
* <b>Key insight</b> The estimation of the expected value of the total discounted reward with stochastic updates requires that the updates correspond to the same distribution as the expectation. Prioritized replay introduces a bias that changes this distribution uncontrollably. This can be corrected by using importance-sampling (IS) weights $ w_i = (\frac{1}{N} \frac{1}{P(i)})^{\beta} $ that fully compensate for the non-uniform probabilities $P(i)$ if $\beta = 1$. These weights are folded into the Q-learning update by using $w_i \times \delta_i$, which is normalized by $\frac{1}{\max_i w_i}$
* IS is annealed from $\beta_0$ to 1, which means its affect is felt more strongly at the end of the stochastic process; this is because the unbiased nature of the updates in RL is most important near convergence
* IS also reduces the gradient magnitudes which is good for optimization; allows the algorithm to follow the curvature of highly non-linear optimization landscapes because the Taylor expansion (gradient descent) is constantly re-approximated