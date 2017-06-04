---
layout: post
title: "Topology and Data"
date: 2017-04-20
paper_ref: Gunnar Carlsson, 2009
redirect_from: 
    - /paper-summaries/2017/04/20/topology-data.html
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

[{{page.paper_ref}}](http://www.ams.org/images/carlsson-notes.pdf)

## Definitions

**Homology** is a general way of associating a sequence of algebraic objects such as abelian groups or modules to other mathematical objects such as topological spaces. Homology itself was developed as a way to analyse and classify manifolds according to their cycles – closed loops (or more generally submanifolds) that can be drawn on a given n dimensional manifold but not continuously deformed into each other [1](https://en.wikipedia.org/wiki/Homology_(mathematics)#Construction_of_homology_groups).

**Connectivity information** is information concerning the loops and higher dimensional analogues in a space. 

**Functoriality** is the notion that invariants should be related not just to objects being studied, but also to the maps between those objects.

Two mathematical objects are said to be **homotopic** if one can be continuously deformed into the other. 

The **k-th Betti number** corresponds to an informal notion of the number of independent k-dimensional surfaces in a k-dimensional vector space.

A **simplicial complex structure** on a space is an expression of the space as a union of points, intervals, triangles, and higher dimensional analogues. 

## Summary 

The homology of simplicial complexes is algorithmically computable; hence, it is desirable to construct a simplicial complex which computes the homology of an underlying space X. One way to do this is to produce a homotopy equivalence from X to the simplicial complex. 

Consider the case where there is a large amount of potentially noisy high-dimensional data. A question that can be asked is whether it is possible to infer the Betti numbers of the underlying space from the noisy data. The Cech complex [2](https://jeremykun.com/2015/08/06/cech-vietoris-rips-complex/) on a metric space, which is a covering by balls of a fixed radius $\epsilon$, is useful because it can be shown to be homotopy equivalent to the underlying Reimannian manifold. However, the data cannot be assumed to always lie on a manifold. The philosophy of selecting all values of $\epsilon$ at once to compute a summary of homological information is known as *persistence*.

## Interesting points

* "Topology is exactly that branch of mathematics which deals with qualitative geometric information."



