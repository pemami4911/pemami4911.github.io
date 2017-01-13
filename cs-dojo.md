---
layout: page
title: CS-Dojo
permalink: /cs-dojo/
---

<div class="home">
  {% for post in site.categories.lecture-notes %}
  <div class="post postContent">
    <div  class="postDate"><time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">{{ post.date | date: "%b %-d, %Y" }}</time>
    </div>
    <div class="postDay">
      {{post.tag}}
    </div>
    <div class="postTitle">
    <a class='postLink' href="{{site.url}}{{site.baseurl}}{{post.url}}">{{post.title}}</a>
    </div>
    <div class="postExt">
   {{ post.content | strip_html | truncatewords:20}}
    </div>
    <br>

  </div>


  {% endfor %}
</div>



