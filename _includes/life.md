
<h1 id="life"></h1>

<h2 style="margin: 60px 0px 10px;" data-lang-en="🖼️ Photo Wall" data-lang-zh="🖼️ 照片墙">🎖 Honors</h2>

<p class="wall-title">Graduate in Chongqing</p>

<div class="photo-wall">
  <img class="photo photo--wide" src="./assets/img/pics/photo_wall_4.jpeg" alt="">
</div>

<p class="wall-title">Happy New Year</p>

<div class="photo-wall">
  <img class="photo" src="./assets/img/pics/photo_wall_2.jpg" alt="">
</div>


<style>
  .wall-title{
    color:#6C3082;
    font-size:22px;
    font-weight:bold;
    padding:5px;
    text-align:center;
  }

  .photo-wall{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:12px;              /* 图片之间的间距 */
  }

  /* 默认：两列布局（桌面端） */
  .photo{
    width:30%;
    height:auto;           /* 关键：保持原始比例 */
    display:block;
    object-fit:contain;    /* 不裁剪、不拉伸 */
  }

  /* 宽图（比如第一张占更大宽度） */
  .photo--wide{
    width:50%;
  }

  /* 移动端：自动改成单列/双列更合理 */
  @media (max-width: 768px){
    .photo{ width: 92%; }
    .photo--wide{ width: 92%; }
  }
</style>
