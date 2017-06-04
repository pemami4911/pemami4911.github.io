---
layout: post
title:  "Incentivizing Exploration in Reinforcement Learning with Deep Predictive Models"
date:   2016-01-22 12:00 PM
paper_ref: Bradly C. Stadie, Sergey Levine, Pieter Abbeel, 2015
redirect_from:
    - /papersummaries/2016/01/22/incentivizing-exploration-in-rl.html
    - /paper_summaries/2016/01/22/incentivizing-exploration-in-rl.html
    - /paper-summaries/2016/01/22/incentivizing-exploration-in-rl.html
---
---
[{{ page.paper_ref }}](http://arxiv.org/abs/1507.00814)

## Summary ##

"Optimism in the face of uncertainty", the mantra of the Upper-Confidence Bound 1 algorithm, becomes impractical to follow when the action space is continuous. Hence, most approaches default to using epsilon-greedy exploration. This paper proposes a scalable and efficient method for assigning exploration bonuses in large RL problems with complex observations. 

A model of the task dynamics is learned to assess the novelty of a new state. As the ability to model the dynamics of a particular state-action pair improves, the "understanding" of the state is thus better and hence its novelty is lower. This circumvents the need to explicitly maintain visitation frequencies for states and state-action pairs in a table. When a state-action pair is not understood well enough to make accurate predictions, it is assumed that more knowledge is needed and hence a higher "novelty" value is assigned to that reward signal.

## Evidence ## 
* This approach was evaluated on 14 games in the Arcade Learning Environment (ALE)
* The reinforcement learning algorithm that was employed was DQN, and performance was evaluated against DQN with epsilon-greedy exploration, Boltzman exploration, and Thompson Sampling
* Not clear that this approach outperforms other state-of-the-art methods consistently

## Strengths ## 
* The paper references methods that were attempted but ultimately failed, such as learning a dynamics model that would predict raw frames (next states) for the Atari simulation

## Weaknesses ## 
* Need to see this method tested on other environments and scenarios

## Interesting related works ## 
* Thompson Sampling
* Boltzman exploration 

## Notes ## 
* PAC-MDP algorithms such as MBIE-EB and Bayesian algorithms such as Bayesian Exploration Bonuses manage the exploration versus exploitation tradeoff by assigning bonuses to novel states. (What are thooose). These sound similar to the UCB1 exploration strategy
* An autoencoder was used to obtain the function sigma that encodes the state prediction model. The choice of autoencoder was for dimensionality reduction of the state space
* "The hidden layers are reduced in dimension until maximal compression occurs with 128 units" 
* An MLP with 2 layers was used to predict model dynamics. The sixth layer of the auto-encoder produces the state with reduced dimensionality 




