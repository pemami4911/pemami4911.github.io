---
layout: post
title: "Cooperative Inverse Reinforcement Learning"
date: 2016-08-11
paper_ref: Hadfield-Menell, et al., 2016
redirect_from:
    - /papersummaries/2016/08/11/Coop-Inverse-RL.html
    - /paper_summaries/2016/08/11/Coop-Inverse-RL.html
    - /paper-summaries/2016/08/11/Coop-Inverse-RL.html
---
---
[{{ page.paper_ref }}](http://arxiv.org/pdf/1606.03137v2.pdf)

## Summary

In the future, AI and people will work together, and hence we must concern ourselves with ensuring that the AI will have interests aligned with our own. 
The authors suggest that it is in our best interests to find a solution to the "value-alignment problem". As recently pointed out by Ian Goodfellow,
[this may not always be a good idea](https://www.quora.com/When-do-you-expect-AI-safety-to-become-a-serious-issue).

Cooperative Inverse Reinforcement Learning (CIRL) is a formulation of a cooperative, partial information game between a human and a robot. Both share a reward 
function, but the robot does not initially know what it is. One of the key departures from classical Inverse Reinforcement Learning
is that the "teacher", which in this case is the human, is not assumed to act optimally. Rather, it is shown that sub-optimal actions
on the part of the human can result in the robot learning a better reward function. The structure of the CIRL formulation is such that it should encourage the 
human to not attempt to teach by demonstration in a way that greedily maximizes immediate reward. Rather, the human learns how to "best respond" to the robot.

## Further Notes

CIRL can be formulated as a dec-POMDP, and reduced to a single-agent POMDP. The authors solved a 2D navigation task with CIRL to demonstrate the inferiority of having the human follow a "demonstration-by-expert" policy as opposed to a "best-response" policy.

In the experiments, the authors used regret as a performance measure for learning the reward function with respect to a fully-observed setting where the robot knows the ground truth of the hidden reward function. Another performance measure used is
the KL-divergence between the max-entropy trajectory distributions induced by the estimate of the reward parameters and the ground truth parameters. Finally,
the L2-norm is used as a measure between the vector of rewards defined by the estimate of the reward parameters and the ground truth parameters.

## Comments

I believe that we'll see some work coming out of OpenAI following this line of research in the near future (where you have AI and humans learning to colloborate safely). 
It is also interesting to note that the experiments conducted in this paper are on a grid-world and far from being applied in a real world setting (until we get much better POMDP solvers, that is).  

