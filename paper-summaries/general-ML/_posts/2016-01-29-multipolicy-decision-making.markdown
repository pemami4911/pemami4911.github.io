---
layout: post
title: "Multipolicy Decision-Making for Autonomous Driving via Changepoint-based Behavior Prediction"
date:  2016-01-29 10:00 PM
paper_ref: Galceran, Cunningham, Eustice, Olson, 2015
redirect_from:
    - /papersummaries/2016/01/29/multipolicy-decision-making.html
    - /paper_summaries/2016/01/29/multipolicy-decision-making.html
    - /paper-summaries/2016/01/29/multipolicy-decision-making.html
---
---
[{{ page.paper_ref }}](http://www.roboticsproceedings.org/rss11/p43.pdf)

## Summary ##
This paper presents an integrated behavioral anticipation and decision-making system that models behavior for both our vehicle and nearby vehicles as the result of closed-loop policies. Only a finite set of *a priori* known policies are considered. Bayesian changepoint detection is used to estimate which policy a given vehicle was executing at each point in its history of actions, then infer the likelihood of each potential intention of the vehicle.

<b>A statistical test is proposed based on changepoint detection to identify anomalous behavior of other vehicles, such as driving in the wrong direction or swerving out of lanes.</b>

## Evidence ## 
Anomaly detection was explored by recording three trajectories corresponding to two bikes and a bus. The bikes crossed an intersection from a sidewalk, while the bus made a significantly wide turn. System was able to detect these trajectories as anomalous (Not within the set of known policies)

Evaluated in simulated driving environment

## Notes ## 
* Bayesian Changepoint detection infers the points in the history of observations where the underlying policy that generated the observations changed. Then, the likelihood of all available policies for the target car given the distribution over the car's potential policies at the current timestep can be computed (sounds like HMM). 
* The CHAMP algorithm infers the maximum *a posteriori* set of times at which changepoints between policies have occurred, yielding a set of segments. Given a segment from time *s* to *t* and a policy *pi*, CHAMP approx the log of the policy-evidence for that segment via the (Bae)yesian information criterion (BIC)
* Viterbi path is found for the most likely sequence of latent policies 
* For decision-making, a set of samples are drawn from the distribution over policies of other cars where each sample assigns a policy to each nearby vehicle, excluding the ego car. For each policy available to the ego car (not all policies are available in every scenario e.g. intersection handling policy is not applicable when driving on a highway), and for each sample s, the process is rolled out forward in time until the decision horizon. This yields a set of simulated trajectories. The reward is evaluated for each element of the set of simulated trajectories and the maximal policy for the ego vehicle is chosen. This repeats continuously in a receding horizon manner. 

* Reward function 
	* distance to the goal at the end of the evaluation horizon
	* minimum distance to obstacles to evaluate safety 
	* lane choice bias to add a preference for the right lane
	* maximum yaw rate and longitudinal jerk to measure passenger comfort
