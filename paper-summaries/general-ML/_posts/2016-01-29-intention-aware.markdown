---
layout: post
title: "Intention-Aware Risk Estimation: Field Results"
date:  2016-01-29 9:00 PM
paper_ref: Lefevre, Vasquez, Laugier, Ibanez-Guzman, 2015
redirect_from:
    - /papersummaries/2016/01/29/intention-aware.html
    - /paper_summaries/2016/01/29/intention-aware.html
    - /paper-summaries/2016/01/29/intention-aware.html
---
---

[{{ page.paper_ref }}](https://5d4cfa3b-a-62cb3a1a-s-sites.googlegroups.com/site/stlefevre/Lefevre_ARSO_15.pdf?attachauth=ANoY7co6MtWJ5P60cdRkTvURboXJZ6O2hEVInCYPLqHZU_kuFkCuu1JRNd2p4aLm5aT4BSzIfz8LMN3S4TBZarCcir48nbbXrxHo5qTaS1Fwzkm1AEp_faxVlca3P7vTOF0WXUvptIjkdQFrFKHkOz3CIFqHLJF96Q59rTqD14uvPfbGn1XOF9ta3W3eTC0SDCrNJFqTQ7hJ62eMvVhcwiwCvcGOMf155w%3D%3D&attredirects=0)

## Summary ##
The proposed contribution is a framework for assessing risk by estimating the intentions of drivers and detecting conflicts between them. Traffic rules are explicitly represented in the model in order to reason about what the drivers are expected to do.

Bayesian programming is used to generate the risk probabilities. Particle filtering is used to approximately solve the inference problem of finding the risk based on the probability that a driver does not intend to stop at an intersection when he is expected to. 

## Evidence ## 
The algorithm was tested on a T-shaped intersection with two passenger vehicles equipped with Vehicle-to-Vehicle communication modems that shared their pose and speed information at a rate of 10 Hz. The test vehicles were *not* equipped with autonomous emergency braking functions, instead an auditory and visual warning were triggered whenever the algorithm detected a dangerous situation. 

Experimentation involved a priority vehicle and obstacle vehicle. Evaluation for the performance of the risk assessment algorithms was based on: 
* The rate of false alarms
* The rate of missed detections
* The collision prediction horizon 

Out of the 90 dangerous trials, 60 were performed with the warning system running on the priority vehicle, and 30 on the obstacle vehicle. In the 20 non-dangerous trials, there were no false alarms. For every one of the 90 dangerous tests, the system was able to issue a warning early enough for the driver to avoid collision by breaking.

## Strengths ## 
* No need for lengthy training 
* The proposed algorithm is generic and could be implemented for various driving scenarios
* No trajectory rollouts 

## Weaknesses ## 
* Speed of the vehicles during experimentatin was not reported
* No collisions during experimentation since only real vehicles were used
* Evaluation of the robustness of the algorithm is left in question due to minimal variablility in experimentation scenarios

## Notes ## 
* The risk of a situation is computed based on the probability that intention and expectation do not match, given measurements of the state 
* a Markov State Space Model is used (this appears to be very similar to the dynamic Bayes net) to propagate the system variables for the bayesian computation