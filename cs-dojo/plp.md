---
layout: default
title: Programming Language Principles
permalink: /cs-dojo/plp/
---
<br>

<div class="home">
  {% for post in site.categories.lecture-notes %}
  <div class="post postContent">
    <div  class="postDate"><time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">{{ post.date | date: "%b %-d, %Y" }}</time>
    </div><br>
    <div class="postTitle">
    <a class='postLink' href="{{site.url}}{{site.baseurl}}{{post.url}}">{{post.title}}</a>
    <div class="paperRef">
      // 
      {{ post.keywords }}
    </div>
    </div>
    <br>

  </div>


  {% endfor %}
</div>