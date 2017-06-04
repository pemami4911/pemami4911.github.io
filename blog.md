---
layout: page
title: Blog
permalink: /blog/
front: true
---

<div class="home">
  {% for post in site.categories.blog %}
  <div class="post postContent">
    <div  class="postDate"><time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">{{ post.date | date: "%b %-d, %Y" }}</time>
    </div><br>
    <div class="postDay">
      {{post.tag}}
    </div>
    <div class="postTitle">
    <a class='postLink' href="{{site.url}}{{site.baseurl}}{{post.url}}">{{post.title}}</a>
    </div>
    <div class="postExt">
        An introduction to the Deep Deterministic Policy Gradient (DDPG) algorithm
    </div>
    <br>

  </div>


  {% endfor %}
</div>



