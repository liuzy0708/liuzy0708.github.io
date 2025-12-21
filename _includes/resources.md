<h1 id="resources"></h1>

<h2 style="margin: 60px 0px -15px;">🔧 Resources</h2>

<div class="publications">
<ol class="bibliography">

{% for link in site.data.resources.main %}

<li>
<div class="pub-row" style="display: flex; align-items: center;">
  <div class="col-sm-4 abbr" style="position: relative;padding-right: 15px;padding-left: 0px;">
    <img src="{{ link.image }}" class="teaser img-fluid z-depth-1" style="width: 300px; height: 160px;">
            <abbr class="badge">{{ link.conference_short }}</abbr>
  </div>
  <div class="col-sm-8" style="position: relative;padding-right: 15px;padding-left: 20px;">
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


