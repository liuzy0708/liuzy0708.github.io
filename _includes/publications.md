<h1 id="publications"></h1>

<h2 style="margin: 60px 0px -15px;" data-lang-en="📝 Main Publications" data-lang-zh="📝 学术论文">📝 Main Publications <temp style="font-size:15px;">[</temp><a href="https://scholar.google.com/citations?user=sRkvMF8AAAAJ&hl=zh-CN" target="_blank" style="font-size:15px;">Google Scholar</a><temp style="font-size:15px;">]</temp><temp style="font-size:15px;">[</temp><a href="https://dblp.uni-trier.de/pid/42/6886.html" target="_blank" style="font-size:15px;">DBLP</a><temp style="font-size:15px;">]</temp></h2>


<div class="publications">
<ol class="bibliography">

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 12px 20px; border-radius: 8px; margin: 30px 0 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  <p style="color: white; font-size: 24px; font-weight: bold; margin: 0; letter-spacing: 1px;">
    📄 Preprint
  </p>
</div>


{% for link in site.data.publications.Preprint %}

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

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 12px 20px; border-radius: 8px; margin: 30px 0 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  <p style="color: white; font-size: 24px; font-weight: bold; margin: 0; letter-spacing: 1px;">
    📚 Journal
  </p>
</div>


{% for link in site.data.publications.Journal %}

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

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 12px 20px; border-radius: 8px; margin: 30px 0 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  <p style="color: white; font-size: 24px; font-weight: bold; margin: 0; letter-spacing: 1px;">
    🎓 Conference
  </p>
</div>


{% for link in site.data.publications.Conference %}

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
