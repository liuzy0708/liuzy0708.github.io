<h1 id="publications"></h1>

<h2 style="margin: 60px 0px -15px;">📝 Main Publications <temp style="font-size:15px;">[</temp><a href="https://scholar.google.com/citations?user=sRkvMF8AAAAJ&hl=zh-CN" target="_blank" style="font-size:15px;">Google Scholar</a><temp style="font-size:15px;">]</temp><temp style="font-size:15px;">[</temp><a href="https://dblp.uni-trier.de/pid/42/6886.html" target="_blank" style="font-size:15px;">DBLP</a><temp style="font-size:15px;">]</temp></h2>


<div class="publications">
<ol class="bibliography">

<p style="color: #6C3082; font-size: 25px; font-weight: bold; marginal-left: 200px">Journal</p>


{% for link in site.data.publications.main %}

<li>
<div class="pub-row">
  <div class="col-sm-3 abbr" style="position: relative;padding-right: 5px;padding-left: 0px;">
    <img src="{{ link.image }}" class="teaser img-fluid z-depth-1" style="width: 260px; height: 140px;">
            <abbr class="badge">{{ link.conference_short }}</abbr>
  </div>
  <div class="col-sm-9" style="position: relative;padding-right: 15px;padding-left: 20px;">
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

<p style="color: #6C3082; font-size: 25px; font-weight: bold; marginal-left: 200px">Conference</p>


{% for link in site.data.publications.Conference %}

<li>
<div class="pub-row">
  <div class="col-sm-3 abbr" style="position: relative;padding-right: 5px;padding-left: 0px;">
    <img src="{{ link.image }}" class="teaser img-fluid z-depth-1" style="width: 250px; height: 120px;">
            <abbr class="badge">{{ link.conference_short }}</abbr>
  </div>
  <div class="col-sm-9" style="position: relative;padding-right: 15px;padding-left: 20px;">
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

<strong> <a style="color:#e74d3c; font-weight:600" href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=sRkvMF8AAAAJ&citation_for_view=sRkvMF8AAAAJ:zYLM7Y9cAGgC"><i id="total_citation_mtl">800+</i><i style="color:#e74d3c; font-weight:600"> Citations</i>
  <script>
      $(document).ready(function () {
          
          var gsDataBaseUrl = 'https://github.com/liuzy0708/liuzy0708.github.io'
          
          $.getJSON(gsDataBaseUrl + "google-scholar-stats/gs_data.json", function (data) {
              var totalCitation = data['publications']['sRkvMF8AAAAJ:zYLM7Y9cAGgC']['num_citations']
              document.getElementById('total_citation_mtl').innerHTML = totalCitation;
              var citationEles = document.getElementsByClassName('show_paper_citations')
              Array.prototype.forEach.call(citationEles, element => {
                  var paperId = element.getAttribute('data')
                  var numCitations = data['publications'][paperId]['num_citations']
                  element.innerHTML = '| Citations: ' + numCitations;
              });
          });
      })
 </script>
