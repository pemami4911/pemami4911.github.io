---
layout: post
title:  "How Hard is Reinforcement Learning?"
date:   2018-01-17
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

In the reinforcement learning setting, an agent interacts with its environment by taking actions and receiving feedback based on having taken a certain action while in a certain state. This feedback, a.k.a. the positive or negative *reinforcement*, usually comes from the environment ([this is not always the case](http://web.eecs.umich.edu/~baveja/Papers/FinalNIPSIMRL.pdf)) and is generally associated with the agent's next state transition. This sequence of agent-environment interactions can be described by a stochastic process. Formally, a discrete-time and discrete-space Markov Decision Process (MDP) is a tuple $(S, A, C, T)$, where $S$ is a finite set of states, $A$ is a finite set of actions, $C$ is a cost function, and $T$ is a stochastic matrix encoding state transition probabilities. At each time $t = 0, 1, ...$ the current state is $s_{t} \in S$, the action taken at time $t$ is denoted by $a_{t} \in A$, and the cost incurred at this time step is $c(s_{t}, a_{t})$. The next state of the process is $s_{t+1}$ and has probability distribution given by $\tau (s_{t+1} \| s_{t}, a_{t}) \in T$. In the simplest case, a policy $\pi$ is a mapping from $s_{t}$ to $a_{t}$. For the *finite horizon* problem, we are given an MDP and an integer $H$. The goal of the agent is to find the policy that minimizes the expectation of the cumulative cost incurred over finite-horizon trajectories:

$$
\mathop{\mathbb{E}} \bigg [ \sum_{t = 0}^{H} c(s_{t}, \pi (s_{t})) \bigg ].
$$

Usually you will need an initial state distribution $s_0 \sim \rho$ as well. A generalization of this problem is to assume that the agent only has access to partial information about the state of the environment at each time step; this is known as a partially-observable MDP (POMDP). The agent receives observations $z_{t} \in Z$, where $Z$ is a finite set of possible observations, from the environment at each time step with probability $o(z_{t} \| s_{t}, a_{t})$. We can define a belief distribution $bel_{t} = [bel_{t, 1} bel_{t, 2} ... bel_{t, \|S\|}]$, which is the vector of conditional probabilities of being in each state $s \in S$ at time step $t$ given the most recent observation and action. It is common to view this problem as a discrete-time continuous-state Markov process. In this setting, policies are mappings from the current belief distribution to actions. 

## P-completeness of Markov decision processes

In complexity theory, the class **P** refers to the "tractable" problems. A proof that the finite-horizon MDP is [P-complete](https://en.wikipedia.org/wiki/P-complete) is provided in [2]. The authors use a reduction from the circuit value problem, a well-known P-complete problem, to show membership in P. They also show that the discounted horizon and average cost variants of MDPs are also P-complete. In practice, solving MDPs exactly can be cumbersome due to the curse of dimensionality; the number of states often grows exponentially with the number of state variables [1]. Regardless, there exists dynamic programming algorithms that run in polynomial time that can solve MDPs with millions of states on today's computers. 

## Hardness of POMDPs

The Markovian assumption that is used to efficiently solve MDPs is relaxed for POMDPs. Now, the agent's observations at each time step do not give it complete information about the current state. Notably, it can be formulated as the following decision problem: ''Given an environment, is there some deterministic memoryless policy mapping observations to actions that guarantees the agent will achieve its goal?''. It turns out that this version of the reinforcement learning problem is NP-complete [5]. A reduction from the classic NP-complete problem 3-CNF-SAT is given in [5]. Furthermore, the variation of this problem where policies are not memoryless, in that they form a mapping from *histories* of all present and past observations to actions, is PSPACE-hard. [PSPACE](https://en.wikipedia.org/wiki/PSPACE) is the class of problems that can be solved by only using a polynomial amount of space. A proof for this claim via a reduction from QSAT (the quantified satisfiability problem) is in [2].

## Non-approximability of POMDPs

When developing solutions for POMDPs, there are trade-offs that must be made between the run-time complexity of the algorithm and the solution quality; that is, unless P = NP or P = PSPACE. The question arises whether it is possible to devise an approximate scheme to find a policy whose performance is within a reasonable fraction of the optimal policy. However, an optimal policy for POMDPs with non-negative rewards (or negative costs) is [$\epsilon$-approximable](https://en.wikipedia.org/wiki/Polynomial-time_approximation_scheme) if and only if P = NP [3]. This follows from a reduction from 3-CNF-SAT with similar construction to [5], except that the cost function is formulated as a function of $\epsilon$ for certain states. These results imply that both exact and approximation algorithms are not useful for solving practically-sized POMDPs; unsurprisingly, the best solvers known today are able to generate solutions quickly, but offer little to no optimality guarantees. 

## Conclusion

Most real-world reinforcement learning problems have incredibly complicated state and/or action spaces. Despite the fact that the fully-observable MDP is P-complete, most realistic MDPs are partially-observed, which we have established as being an NP-hard problem at best. Even $\epsilon$-approximable algorithms for POMDPs are only solvable in polynomial time if P = NP. However, recent research has pointed out that there exist specific instances of POMDPs that have polynomial-time approximation schemes [6], so long as the belief space admits certain convenient properties. These approximation algorithms are derived from Point Based Value Iteration (PBVI) [4], a method that uses sampling to reduce the dimensionality of the belief space. One can imagine why this would be a successful heuristic; an agent should only need to explore a small fraction of the entire belief space for a given environment and task. So, what are the implications of the hardness of reinforcement learning discussed here to deep reinforcement learning? It's hard to say exactly, but DRL agents are nonetheless able to find decent policies in challenging domains such as Atari and Mujoco (e.g., by leveraging clever exploration and powerful representation learning). Hopefully we will see the success of DRL on truly difficult POMDPs like Starcraft 2 quite soon.  

## References

1. Sutton, R. S. and Barto, A. G. Reinforcement learning: An introduction. MIT press Cambridge, 1998, Vol. 1(1)
2. Papadimitriou, C. H. and Tsitsiklis, J. N. The complexity of Markov decision processes. Mathematics of operations research, INFORMS, 1987, Vol. 12(3), pp. 441-450
3. Lusena, C., Goldsmith, J. and Mundhenk, M. Nonapproximability results for partially observable Markov decision processes. J. Artif. Intell. Res.(JAIR), 2001, Vol. 14, pp. 83-103
4. Pineau, J., Gordon, G., Thrun, S. and others. Point-based value iteration: An anytime algorithm for POMDPs. IJCAI, 2003, Vol. 3, pp. 1025-1032
5. Littman, M. L. Memoryless policies: Theoretical limitations and practical results. From Animals to Animats 3: Proceedings of the Third International Conference on Simulation of Adaptive Behavior, 1994, Vol. 3, pp. 238
6. Lee, W. S., Rong, N. and Hsu, D. J. What makes some POMDP problems easy to approximate? Advances in neural information processing systems, 2007, pp. 689-696