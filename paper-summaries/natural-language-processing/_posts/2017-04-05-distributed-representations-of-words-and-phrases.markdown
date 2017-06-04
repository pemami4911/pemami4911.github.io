---
layout: post
title: "Distributed Representations of Words and Phrases and their Compositionality"
date: 2017-04-05
paper_ref: Mikolov, et. al., 2013
redirect_from:
    - /paper-summaries/2017/04/05/distributed-representations-of-words-and-phrases.html
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

[{{page.paper_ref}}](https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf)

## Skip-gram model

Objective is to find word representations that are useful for predicting the surrounding words in a sentence or a document. Given a sequence of words $w_1, w_2, ..., w_T$, the Skip-gram model aims to max the average log probability

$$
\frac{1}{T} \sum_{t=1}^{T} \sum_{-c \le j \le c, j \neq 0} \log p(w_{t+j} | w_t)
$$

where `c` is the size of the training context. Larger `c` results in more training examples and thus can lead to a higher accuracy at the expense of increased training time. The probability $p(w_O \| w_I )$ is represented with a softmax.

## Heirarchical Softmax

Instead of evaluated `W` output nodes of a neural network to get the probability distribution, where `W` is the size of the target dictionary, only need to evaluate about $\log_2 (W)$ nodes.

The idea is to represent the output layer as a binary tree with `W` leaves and, for each node, explicitly represents the relative probabilities of its child nodes. Then the probability $p(w_O \| w_I )$ can be defined by the product of probabilities of a path down the tree from the root. The root here is the first word in the sequence. The individual probabilities are outputs of a sigmoid, scaled by +1 or -1 if the current word `w`'s probability matches that of its child.

## Negative Sampling

A simplified form of something called Noice Constrastive Estimation (NCE). NCE aims to learn a model that is able to differentiate data from noise by means of logistic regression. The negative sampling objective simplifies this because for the Skip-gram model, only the high-quality vector representation is needed. The task becomes to distinguish the target word from draws from a noise distribution using logistic regression over `k` negative samples for each data sample.

## Conclusion

The authors used a few other tricks, like sub-sampling frequent words such as "in", "the", "a". Also, they used unigrams and bigrams to identify phrases during training. This approach can be applied to massive monolingual corpuses to quickly learn high-quality vector representations of words.

