---
layout: post
title: "Building Machines That Learn and Think Like People"
date: 2016-05-13
---
[Lake, et al. 2016](http://arxiv.org/pdf/1604.00289v2.pdf)

## Summary ##

This article presents a roadmap for future progress in developing machines that can learn and "think" like humans. A short-term goal of the authors is to improve today's machine learning techniques so that complex concepts can be learned quickly with only small amounts of data. Currently, our algorithms require ungainly amounts of data and compute to perform at acceptable levels.

<p>
The authors argue that a marriage of two distinct research areas in artificial intelligence, that of statistical pattern recognition and of model-building, will produce a promising avenue for new advances. Learning as a form of explaining observed data through the construction of causal models of the world can potentially be carried out by deep neural networks. 

<p>
The first causal model that is discussed is that of a model of <b>intuitive physics</b>. That is, a machine with an internal model of the physics of its environment would be able to learn more quickly, since it will not need to relearn these principles when attempting to learn new tasks that require physical interaction. 

<p>
The next is that of a model of <b>intuitive psychology</b>. A learning agent that assumes that other agents in its environment are rational and have their own goals and beliefs can try to infer what these might be. Having knowledge of the intentions of other agents in the environment would allow the learning agent to achieve its own goals in a much more efficient way.  

The following ideas are also central to the main ideas presented by the authors.
<p>
Compositionality is the classic idea that new representations can be constructed through the combination of primitive elements. See [Lake et. all 2015](http://web.mit.edu/cocosci/Papers/Science-2015-Lake-1332-8.pdf) for a discussion on the use of compositionality to generate novel handwritten characters. This is central to training agents to learn models of complex symbolic concepts. 

<p>
Learning-to-Learn is closely related to the concept of "transfer-learning" and "representation-learning" in machine learning. Machines that learn like humans will need to be able to learn rich, informative priors and models of the world that can be applied to a variety of tasks. Systems should be able to learn to do new tasks as flexibly and rapidly as humans do. The authors suggest compositionality and the use of causal models to augment the current deep-learning research in transfer-learning.

<p>
There are still a lot of challenges concerning intractability of certain methods and the amount of time necessary for doing optimization over high-dimensional potentially non-convex parameter spaces. Approximate inference is an area of research that aims to address these challenges. Monte Carlo methods are promising for many problems, but runs into problems when the hypothesis space is vast. Deep neural networks may potentially be used for performing probabilistic inference in a generative model or a probabilistic program. 

<p>
There is evidence that the brain uses a form of model-free reinforcement learning to accomplish certain tasks. However, there is also evidence that the brain has a model-based learning system. Shifting between model-free and model-based learning methods can benefit from taking advantage of the causal-model/compositionality discussed above. 

## Strengths ## 

The authors address potential counter-points in Section 5. These are: "Comparing the learning speeds of humans and neural networks on specific tasks is not meaningful, because humans have extensive prior experience", "Biological plausibility suggests theories of intelligence should start with networks", "Language is essential for human intelligence. Why is it not more prominent here?"

## Weaknesses ## 

There isn't a clear definition of "intelligence". The closest is the authors' statement that the goal of those who wish to create machines that learn like humans (e.g. display human-level intelligence) should be to devise ways to carry out learning from far less data and to generalize in richer and more flexible ways.