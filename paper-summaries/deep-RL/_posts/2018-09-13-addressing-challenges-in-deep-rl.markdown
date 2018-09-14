---
layout: post
title: Addressing Function Approximation Error in Actor-Critic Methods & Addressing Sample Inefficiency and Reward Bias in Inverse Reinforcement Learning
date: 2018-09-13
paper_ref: Fujimoto et al., 2018, Kostrikov, et al. 2018
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

[Fujimoto et al., 2018](https://arxiv.org/abs/1802.09477) and [Kostrikov et al., 2018](https://arxiv.org/abs/1809.02925)

## Summary

I discuss two recent related papers in the Deep RL literature in this post. The first paper, by Fujimoto et al., introduces techniques for reducing bias and variance in a popular actor-critic method, Deep Deterministic Policy Gradient (DDPG). The second paper, by Kostrikov et al., makes a similar contribution by evaluating and addressing bias and variance in inverse RL. The motivation for these two papers is to take widely used Deep RL algorithms, empirically and theoretically demonstrate specific weaknesses, and suggest reasonable improvements. These are valuable studies.

### Addressing Function Approx. Error in AC Methods

If you are unfamiliar with DDPG, you can check out [my blog post](https://pemami4911.github.io/blog/2016/08/21/ddpg-rl.html) on the algorithm. The most important thing to know is that the success of the whole algorithm relies on having a critic network that can accurately estimate the $Q$-values. The only signal the actor network gets in its gradient to help it achieve higher rewards comes from the gradient of the critic wrt the actions selected by the actor. If the critic gradient is biased, then the actor will surely fail!

In Section 4, the authors begin by empirically demonstrating the overestimation bias present in the critic network (action-value estimator) in DDPG. They show that the overestimation bias essentially stems from the fact that DPG algorithms have to approximate both the policy and the value functions, and the approximate policy is maximized in the gradient direction provided by the approximate value function (rather than the true value function). Then, inspired by Double Q-Learning, they introduce a technique they call "clipped Double Q-Learning in AC" for achieving the same idea. Basically, the critic target becomes
$$
y_1 = r + \gamma \min_{i=1,2} Q_{\theta'_i} (s', \pi_{\theta_1}(s')).
$$
This requires introducing a second critic. The min makes it so that it is possible to underestimate Q-values, but this is preferable to overestimation.

Then, to help with variance reduction, they suggest:
* Delay updating the actor network until the critic network has almost converged
* Add some noise to the actions selected by the actor network when updating the critic to help regularize the critic, reminiscent of Expected SARSA

Their experimental results on MuJoco (they call their algorithm TD3) suggest these improvements are very effective, outperforming PPO, TRPO, ACKTR, and others.

### Addressing Sample Inefficiency and Reward Bias in Inverse RL

Seemingly inspired by the former, a similar paper recently came out exploring inverse RL---specifically, generative adversarial imitation learning (GAIL) and behavioral cloning. In inverse RL, ideally both the number of expert demonstrations and policy interactions with the environment prior to convergence are small. In GAIL, the discriminator learns to distinguish between transitions sampled from an expert and those from a trained policy. The policy is rewarded for confusing the discrminiator.

One way the authors suggest to help with the sample inefficiency of GAIL is by using off-policy RL instead of on-policy RL. They modify the GAIL objective to be 
$$
\max_D \mathcal{E}_\mathscr{R} [\log(D(s,a))] + \mathcal{E}_{\pi_E}[\log(1 - D(s,a))] - \lambda H(\pi).
$$
Basically, $\pi_E$ is the expert policy, from which trajectories are sampled, and $\mathscr{R}$ is the replay buffer, from which trajectories are sampled from ~all previous policies. They ignore the importance sampling term in practice. They discuss this with application to TD3, but TD3 is designed for deterministic policies. I'm sure what the authors mean is that TD3's policy deterministically predicts the mean of a multivariate Gaussian---this Gaussian could then be used to define the entropy term and could be used for importance sampling. This is fairly common for continuous control tasks like MuJoco.

They further analyzed different reward functions for GAIL, and show they certain GAIL reward functions can inhibit learning depending on the particular MDP (e.g., if the environment has a survival bonus or penalty). To create a more robust reward function that will learn the expert policies, they suggest explicitly learning rewards for absorbing states of the MDP. THey implement this by adding an indicator to these particular states so that the GAIL discriminator can identify whether reaching an absorbing state is desirable from the perspective of the expert.

Very interestingly, they used VR to generate expert trajectories of gripping blocks with a Kuka arm. This environment has a per-step penalty, and the normal GAIL reward fails to learn the expert policy due to the the learning inhibition caused by the reward function bias. The proposed method learns to imitate the expert quickly due to its added reward for absorbing states.

The use of off-policy RL with GAIL is cool, but there is little in terms of contribution that is made in this paper wrt to that. It would be interesting to investigate the effects of using off-policy samples in the objective more carefully (why exactly does importance sampling not matter? I suspect that has to do with the policy that TD3 implements...). The absorbing state reward stuff being so useful is surprising, and should be helpful in future applications where GAIL is used.