---
layout: post
title: "Geometric deep learning: going beyond Euclidean data"
date: 2017-11-19
paper_ref: Bronstein, 2017
redirect_from:
    - /paper-summaries/deep-learning/2017/11/19/geometric-deep-learning.html
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

[{{ page.paper_ref }}](https://arxiv.org/abs/1611.08097)

## Notes

This paper surveys progress on adapting deep learning techniques to non-Euclidean data and suggests future directions. One of the strengths (and weaknesses) of deep learning--specifically exploited by convolutional neural networks--is that the data is assumed to exhibit translation invariance/equivariance and invariance to local deformations. Hence, long-range dependencies can be learned with multi-scale, hierarchical techniques where spatial resolution is reduced. However, this means that any information about the data that can't be learned when spatial resolution is reduced can get lost (I believe that residual networks aim to address this by the skip connections that are able to learn an identity operation; also, in computer vision, multi-scale versions of the data are often fed to CNNs). Key areas where this assumption about the data appears to be true is computer vision and speech recognition.

#### Some quick background 

The *Laplacian*, a self-adjoint (symmetric) positive semi-definite operator, which is defined for smooth manifolds and graphs in this paper, can be thought of as the difference between the local average of a function around a point and the value of the function at the point itself. It's generally defined as $\triangle = -\text{div} \nabla$. When discretizing a continuous, smooth manifold with a *mesh*, note that the graph Laplacian might not converge to the continuous Laplacian operator with increasing sampling density. To be consistent, need to create a triangular mesh, i.e., represent the manifold as a polyhedral surface.

### Spectral methods

Fourier analysis on non-Euclidean domains is possible by considering the eigendecomposition of the Laplacian operator. A possible transformation of the Convolution Theorem to functions on manifolds and graphs is discussed, but is noted as not being shift-invariant. 

The Spectral CNN can be defined by introducing a spectral convolutional layer acting on the vertices of the graph and using filters in the frequency domain and the eigenvectors of the Laplacian. However, the spectral filter coefficients will be dependent on the particular eigenvectors (basis) - domain dependency == bad for generalization!

The non-Euclidean analogy of pooling is *graph coarsening*- only a fraction of the vertices of the graph are retained. Strided convolutions can be generalized to the spectral construction by only keeping the low-frequency components - must recompute the graph Laplacian after applying the nonlinearity in the spatial domain, however. 

Performing matrix multiplications on the eigendecomposition of the Laplacian is expensive!

### Spectrum-free Methods

**A polynomial of the Laplacian acts as a polynomial on the eigenvalues**. ChebNet (Defferrard et al.) and Graph Convolutional Networks (Kipf et al.) boil down to applying simple filters acting on the r- or 1-hop neighborhood of the graph in the spatial domain.

Some examples of generalizations of CNNs that define weighting functions for a locally Euclidean coordinate system around a point on a manifold are the 
  * Geodesic CNN
  * Anisotropic CNN
  * Mixture Model network (MoNet)


#### What problems are being solved with these methods?

* Ranking and community detection on social networks
* Recommender systems
* 3D geometric data in Computer Vision/Graphics
    * Shape classification
    * Feature correspondence for 3D shapes
* Behavior of N-particle systems (particle physics, LHC)
* Molecule design
* Medical imaging

### Open Problems

* *Generalization* spectral analogues of convolution learned on one graph cannot be readily applied to other ones (domain dependency). Spatial methods generalize across different domains, but come with their own subtleties
* *Time-varying domains*
* *Directed graphs* non-symmetric Laplacian that do not have orthogonal eigendecompositions for interpretable spectral-domain constructions
* *Synthesis problems* generative models
* *Computation* extending deep learning frameworks for non-Euclidean data