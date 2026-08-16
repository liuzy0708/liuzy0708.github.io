<h1 id="resources"></h1>

<h2 style="margin: 60px 0px -15px;">🔧 Resources</h2>

<div class="publications">
<ol class="bibliography">

{% for link in site.data.resources.main %}

<li>
<div class="pub-row">
  <div class="pub-thumb">
    {% if link.image contains '.mp4' %}
    <video class="teaser img-fluid z-depth-1" src="{{ link.image }}" preload="auto" autoplay muted loop playsinline></video>
    {% else %}
    <img src="{{ link.image }}" class="teaser img-fluid z-depth-1" alt="{{ link.title }}">
    {% endif %}
    <abbr class="badge">{{ link.conference_short }}</abbr>
  </div>
  <div class="pub-info">
      <div class="title"><a href="{{ link.pdf }}">{{ link.title }}</a></div>
      <div class="author">{{ link.authors }}</div>
      <div class="periodical"><em>{{ link.conference }}</em>
      </div>
         <div class="links">
            {% if link.others %} 
      <strong>{{ link.others  }}</strong>
      {% endif %}
            {% if link.notes %} 
      <strong style="color:#e74d3c"> &nbsp;{{ link.notes }}</strong>
      {% endif %}
      </div>
    <div class="links">
      {% if link.pdf %} 
      <a href="{{ link.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">PDF</a>
      {% endif %}
      {% if link.code %} 
      <a href="{{ link.code }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Code</a>
      {% endif %}
      {% if link.page %} 
      <a href="{{ link.page }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Project Page</a>
      {% endif %}
      {% if link.bibtex %} 
      <a href="{{ link.bibtex }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">BibTex</a>
      {% endif %}
    </div>
  </div>
</div>
</li>

<br>

{% endfor %}

</ol>
</div>
