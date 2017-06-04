---
layout: post
title:  "Bayesian Theory of Mind: Modeling Joint Belief-Desire Attribution"
date:   2016-01-18 9:00 PM 
paper_ref: Baker, et al., 2011
redirect_from: 
    - /papersummaries/2016/01/18/review-btom.html
    - /paper_summaries/2016/01/18/review-btom.html
    - /paper-summaries/2016/01/18/review-btom.html
---
---
[{{ page.paper_ref }}](http://mindmodeling.org/cogsci2011/papers/0583/paper0583.pdf)

## Introduction ##

Q: What is the 'Theory of Mind'? 

A: "The human capacity for reasoning about agents' mental states such as beliefs and desires" 

The inference problem of determining the mental states and desires that caused some behavior is fundamentally ill-posed (i.e. there are many combinations of beliefs and desires that could explain the same behavior).

One approach to this is to employ the 'principal of rational action', which is the theory that agents are expected to choose actions that maximize their expected utility 

## Bayesian Theory of Mind (BToM) ##
An agent's planning and inference about the world is modeled as a Partially Observable Markov Decision Process. This model includes a representation of the agent's desires (utility function) and the agent's own subjective beliefs about the environment (probability distribution)

An observer of an agent's behavior in an environment attempts to attribute the beliefs and desires that caused the agent to generate such behavior. 

Joint belief and desire inference is carried out with a form of belief filtering; a Dynamic Bayes Net (DBN) is employed to model the agent's desires, observations, states, beliefs, and actions over time. 

## Conclusions ##
An experiment was conducted where a sample of test subjects were asked to infer the beliefs and desires of an agent acting in a simulated environment. The results of this study was compared to BToM. BToM performed very closely to the humans at the task of belief and desire inference. By modifying BToM and running the experiment with the alternative models, it was determined that it is necessary to perform joint inference on both the agent's beliefs and desires, and to explicitly model the agent's observational process. It was also necessary to represent the agent's initial uncertainty over both the beliefs and desires.

The idea of modeling agents in an environment with POMDPs shows significant promise. Due to computational difficulties, this approach is quite restricted. With recent advances in Deep Reinforcement Learning, however, multi-agent POMDPs could see a resurgence in popularity.