
<h1 id="research"></h1>

<h2 style="margin: 60px 0px 10px;">📚 Research</h2>

<div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
  <h3 style="color: #667eea; margin-top: 0; border-bottom: 2px solid #667eea; padding-bottom: 10px; font-size: 24px;">
    🔬 Research Fields
  </h3>
  
  <div style="margin-bottom: 25px;">
    <h4 style="color: #2c3e50; margin: 15px 0 10px 0; font-size: 20px;">
      Safety-guaranteed Control of Dynamic Systems in Non-stationary Environment
    </h4>
    <ul style="line-height: 1.8; color: #555; font-size: 20px;">
      <li>Learning for UAV attitude control</li>
      <li>Vision-language-safe action models for embodied artificial intelligence</li>
    </ul>
  </div>

  <div style="margin-bottom: 25px;">
    <h4 style="color: #2c3e50; margin: 15px 0 10px 0; font-size: 20px;">
      Real-time Safety Assessment of Dynamic Systems in Non-stationary Environment
    </h4>
    <ul style="line-height: 1.8; color: #555; font-size: 20px;">
      <li>Online active learning methods and their optimization</li>
      <li>Detection and adaptation methods of concept drift</li>
      <li>Incremental learning</li>
    </ul>
  </div>

  <div style="margin-bottom: 10px;">
    <h4 style="color: #2c3e50; margin: 15px 0 10px 0; font-size: 20px;">
      Multi-mode Fault Diagnosis of Dynamic Systems under Variable Operating Modes
    </h4>
    <ul style="line-height: 1.8; color: #555; font-size: 20px;">
      <li>Online semi-supervised learning methods and their optimization</li>
      <li>Imbalance problem in the framework of online learning</li>
      <li>Explainable artificial intelligence</li>
    </ul>
  </div>
</div>

<div style="background: #fff; padding: 20px; border: 1px solid #e0e0e0; border-radius: 10px; margin-bottom: 20px;">
  <h3 style="color: #667eea; margin-top: 0; border-bottom: 2px solid #667eea; padding-bottom: 10px; font-size: 24px;">
    💼 Research Projects
  </h3>
  <ul style="line-height: 2; color: #555; font-size: 20px;">
    <li><strong>National Natural Science Foundation of China (for Ph.D. Candidate)</strong> under Grant 624B2087 <em>(Host)</em></li>
      <li><strong>Innovative Entrepreneurial Training Plan Program of College Students</strong> in Chongqing <em>(Host)</em></li>
    <li><strong>National Natural Science Foundation of China</strong> under Grant 61573290, 61503237, 61733009, 61973332 <em>(Participant)</em></li>
    <li><strong>National Key Research and Development Program of China</strong> under Grant 2017YFA0700300 <em>(Participant)</em></li>
    <li><strong>Key Project from Natural Science Foundation of Guangdong Province</strong> under Grant 2018B030311054 <em>(Participant)</em></li>
  </ul>
</div>

<div style="background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%); padding: 20px; border-radius: 10px;">
  <h3 style="color: #667eea; margin-top: 0; border-bottom: 2px solid #667eea; padding-bottom: 10px; font-size: 24px;">
    📈 Research Statistics
  </h3>
  <div style="display: flex; gap: 30px; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 200px;">
      <p style="font-size: 20px; color: #555; margin: 10px 0 5px 0; font-weight: 600;">
         Google Citation:
      </p>
      <strong>
        <a style="color:#e74d3c; font-weight:600; font-size: 28px;" href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=sRkvMF8AAAAJ&citation_for_view=sRkvMF8AAAAJ:zYLM7Y9cAGgC">
          <i id="total_citation_mtl">200+</i>
        </a>
      </strong>
    </div>
    <div style="flex: 1; min-width: 200px;">
      <p style="font-size: 20px; color: #555; margin: 10px 0 5px 0; font-weight: 600;">
         H-index:
      </p>
      <strong>
        <a style="color:#e74d3c; font-weight:600; font-size: 28px;" href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=sRkvMF8AAAAJ&citation_for_view=sRkvMF8AAAAJ:zYLM7Y9cAGgC">
          <i id="totalHindex_mtl"></i>
        </a>
      </strong>
    </div>
    <div style="flex: 1; min-width: 200px;">
      <p style="font-size: 20px; color: #555; margin: 10px 0 5px 0; font-weight: 600;">
         i10-index:
      </p>
      <strong>
        <a style="color:#e74d3c; font-weight:600; font-size: 28px;" href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=sRkvMF8AAAAJ&citation_for_view=sRkvMF8AAAAJ:zYLM7Y9cAGgC">
          <i id="i10index_mtl"></i>
        </a>
      </strong>
    </div>
  </div>
</div>

<script>
    $(document).ready(function () {
        $.getJSON("https://raw.githubusercontent.com/liuzy0708/liuzy0708.github.io/main/google_scholar_crawler/results/gs_data.json", function (data) {
            document.getElementById('total_citation_mtl').textContent = data['citedby'];
            document.getElementById('totalHindex_mtl').textContent = data['hindex'];
            document.getElementById('i10index_mtl').textContent = data['i10index'];
        });
    });
</script>
