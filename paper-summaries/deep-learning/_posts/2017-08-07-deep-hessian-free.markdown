---
layout: post
title: "Deep Learning via Hessian-Free Optimization"
date: 2017-08-07
paper_ref: James Martens, 2010
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

[{{page.paper_ref}}](http://www.cs.toronto.edu/~jmartens/docs/Deep_HessianFree.pdf)

## Summary

This paper introduces a fairly complex optimization algorithm for deep nets that uses approximate 2nd-order gradient information 

* In Hessian-Free optimization, you can directly approximate a Hessian-vector product $Hv$ with the method of finite-differences; this only costs 1 more gradient evaluation
* linear conjugate gradient algorithm allows one to solve for the optimal search direction in $O(N)$ iterations ($N$ is the number of parameters) with only matrix-vector products
* Newton's method is scale invariant, e.g., for a new parameterization $\hat{\theta} = A \theta$ for some invertible matrix $A$, the optimal search direction is now $\hat{p} = A p$ where $p$ is the original optimal search direction. Gradient descent is not (need proof!) - so many bad things about GD, but it's so easy to implement..

## Considerations when applying this technique

* Need to use an adaptive damping parameters $\lambda$ beause the relative scale of $B = H(\theta)$ is changing and $H(\theta)$ must remain positive semidefinite. Recommended heuristic is given in Section 4.1
* Gauss-Newton matrix $G$ can produce better search directions than $H$, see [this blog post](http://andrew.gibiansky.com/blog/machine-learning/gauss-newton-matrix/) for a summary
* Compute gradient on entire dataset, but use minibatches to compute Hessian-vector products. SGD requires 10's of thousands of iterations versus ~200 for HF



