import re

file_path = "/Users/ediz/Documents/antigravity/delightful-archimedes/edizandco-website/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace <title> and <meta>
html = re.sub(r'<title>.*?</title>', '<title>Ediz & Co. — Müşteri Canlandırma Operasyonu</title>', html)
html = re.sub(r'<meta name="description" content=".*?" />', '<meta name="description" content="Takip dışında kalan eski müşteri adaylarınızı 3 iş günü içinde aksiyona hazır fırsat listesine çeviriyoruz." />', html)
html = re.sub(r'<meta property="og:title" content=".*?" />', '<meta property="og:title" content="Ediz & Co. — Müşteri Canlandırma Operasyonu" />', html)
html = re.sub(r'<meta property="og:description" content=".*?" />', '<meta property="og:description" content="Ekibinize kiminle, hangi sırayla, hangi notla temas kuracaklarını gösteren evrensel operasyon dosyası." />', html)

body_content = """<body>

<!-- NAV -->
<nav>
  <a class="nav-logo" href="#">
    <svg xmlns="http://www.w3.org/2000/svg" width="175" height="24" viewBox="0 0 175 24" aria-label="Ediz & Co." style="display:block">
      <text x="0" y="19" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:19px;font-weight:700;fill:#F4F0E8;letter-spacing:0.01em">Ediz &amp; Co.</text>
    </svg>
  </a>
  <ul class="nav-mid">
    <li><a href="#hizmet">Hizmet</a></li>
    <li><a href="#surec">Süreç</a></li>
  </ul>
  <a class="nav-cta" href="#iletisim">Örnek İste</a>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-body">
    <div class="hero-eyebrow">72 Saat Teslimat Garantisi</div>
    <h1 class="hero-h" style="font-size: clamp(3.2rem, 8vw, 8rem);">
      Takip dışında kalan eski müşteri adaylarınızı<br>
      <em>3 iş günü içinde</em><br>
      aksiyona hazır fırsat listesine çeviriyoruz.
    </h1>
  </div>
  <div class="hero-foot">
    <p class="hero-desc">
      Ekibinize kiminle, hangi sırayla, hangi notla temas kuracaklarını (arama, WP, mesaj) gösteren tek bir evrensel operasyon dosyası teslim ediyoruz.
    </p>
    <div class="hero-acts">
      <a class="btn btn-solid" href="#iletisim">İlk 5 Kaydı Ücretsiz Örnekleyelim</a>
      <a class="btn btn-ghost-d" href="#hizmet">Detayları Gör</a>
    </div>
  </div>
</section>

<!-- TICKER -->
<div class="ticker">
  <div class="ticker-track">
    <span>Müşteri Canlandırma Operasyonu</span><span class="dot">&nbsp;·&nbsp;</span>
    <span>72 Saat Garanti</span><span class="dot">&nbsp;·&nbsp;</span>
    <span>Evrensel Operasyon Dosyası</span><span class="dot">&nbsp;·&nbsp;</span>
    <span>Aksiyona Hazır Liste</span><span class="dot">&nbsp;·&nbsp;</span>
    <span>Müşteri Canlandırma Operasyonu</span><span class="dot">&nbsp;·&nbsp;</span>
    <span>72 Saat Garanti</span><span class="dot">&nbsp;·&nbsp;</span>
    <span>Evrensel Operasyon Dosyası</span><span class="dot">&nbsp;·&nbsp;</span>
    <span>Aksiyona Hazır Liste</span><span class="dot">&nbsp;·&nbsp;</span>
  </div>
</div>

<!-- PRICING / HİZMET -->
<section id="hizmet" class="reveal" style="padding: 9rem 4vw; background: var(--dark); color: var(--on-dark);">
  <div class="sec-head-dark">
    <div>
      <div class="sec-label-sm" style="color: var(--accent);">Tek Hizmet. Net Sonuç.</div>
      <h2 class="sec-h-dark">Müşteri Canlandırma<br><em>Operasyonu</em></h2>
    </div>
    <div class="sec-sub-dark">
      Eski listenizi canlandırıyor, size<br>
      <strong>masada kalan parayı getiriyoruz.</strong>
    </div>
  </div>
  
  <div style="margin-top: 4rem; border: 1px solid var(--rule-d); background: var(--ink); padding: 4rem; display: flex; flex-direction: column; gap: 2rem; position: relative;">
    <div style="font-size: 0.65rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent);">Tüm Süreç Dahil</div>
    <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 2rem;">
      <div>
        <h3 style="font-size: 2.5rem; font-weight: 800; letter-spacing: -0.025em; margin-bottom: 0.5rem; color: var(--on-dark);">Komple Canlandırma</h3>
        <p style="font-size: 0.9rem; color: var(--on-dark-m);">500 kayda kadar tam veri analizi ve aksiyon listesi.</p>
      </div>
      <div style="display: flex; align-items: baseline; gap: 0.3rem;">
        <span style="font-size: 4rem; font-weight: 900; letter-spacing: -0.03em; line-height: 1; color: var(--on-dark);">45.000</span><span style="font-size: 1.5rem; font-weight: 700; color: var(--on-dark);">₺</span>
      </div>
    </div>
    
    <div style="height: 1px; background: var(--rule-d); margin: 1rem 0;"></div>
    
    <ul style="list-style: none; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
      <li style="display: flex; gap: 0.8rem; align-items: flex-start; font-size: 0.9rem; color: var(--on-dark-m);"><span style="color: var(--accent); font-weight: 700;">—</span> 500 Kayda Kadar Kapsam</li>
      <li style="display: flex; gap: 0.8rem; align-items: flex-start; font-size: 0.9rem; color: var(--on-dark-m);"><span style="color: var(--accent); font-weight: 700;">—</span> 3 İş Günü Teslimat</li>
      <li style="display: flex; gap: 0.8rem; align-items: flex-start; font-size: 0.9rem; color: var(--on-dark-m);"><span style="color: var(--accent); font-weight: 700;">—</span> 1 Tur İnce Ayar Garantisi</li>
      <li style="display: flex; gap: 0.8rem; align-items: flex-start; font-size: 0.9rem; color: var(--on-dark-m);"><span style="color: var(--accent); font-weight: 700;">—</span> Evrensel Operasyon Dosyası</li>
    </ul>
  </div>
</section>

<!-- PROCESS -->
<section id="surec" class="reveal" style="padding: 9rem 4vw; background: var(--bg-off);">
  <div class="sec-head-light" style="margin-bottom:0">
    <div>
      <div class="sec-label-sm">Süreç</div>
      <h2 class="sec-h-light">3 Günde <em>Nasıl Çalışır?</em></h2>
    </div>
    <p class="sec-sub-light">Eski listelerinizi anında sıcak fırsatlara dönüştüren net ve şeffaf operasyon.</p>
  </div>

  <div class="p-steps">
    <div class="p-step">
      <span class="p-num">01</span>
      <div class="p-title">Veri Kabulü</div>
      <p class="p-desc">Kenarda bekleyen, aranmamış, ulaşılamamış veya soğumuş 500'e kadar eski müşteri kaydınızı bize teslim edersiniz.</p>
    </div>
    <div class="p-step">
      <span class="p-num">02</span>
      <div class="p-title">Derinlemesine Analiz</div>
      <p class="p-desc">Yapay zeka ve operasyon tecrübemizle veriyi tarar; her bir kaydın kim olduğunu, neden durduğunu ve nasıl yeniden tetiklenebileceğini saptarız.</p>
    </div>
    <div class="p-step">
      <span class="p-num">03</span>
      <div class="p-title">Teslimat & Aksiyon</div>
      <p class="p-desc">72 saat içinde; ekibinize kimi arayacağını, kime WhatsApp'tan yazacağını ve temas sırasında tam olarak hangi notu/teklifi kullanacağını gösteren operasyon dosyanızı teslim ederiz.</p>
    </div>
  </div>
</section>

<!-- CTA -->
<section id="iletisim" class="reveal" style="padding: 12rem 4vw; text-align: center; background: var(--dark); color: var(--on-dark); position: relative; overflow: hidden;">
  <div class="cta-eyebrow">Hemen Deneyin</div>
  <h2 class="cta-h" style="font-size: clamp(3.5rem, 8vw, 7rem);">
    20 Kayıt Gönderin,<br>
    <em>İlk 5'ini Ücretsiz Örnekleyelim.</em>
  </h2>
  <p class="cta-sub">Sistemin gücünü görmek için elinizdeki en zorlu veya en eski 20 kaydı bize iletin. Size ücretsiz olarak ilk 5 kaydın canlandırma stratejisini hazırlayalım.</p>
  <div class="cta-acts">
    <a class="btn btn-cream" href="mailto:edizandcompany@gmail.com?subject=Ücretsiz%20Örnekleme%20Talebi">Hemen E-Posta At</a>
    <a class="btn btn-accent" href="https://wa.me/905000000000?text=Merhaba,%20ücretsiz%20örnekleme%20için%2020%20kayıt%20göndermek%20istiyorum." target="_blank" rel="noopener">WhatsApp'tan Ulaş</a>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <svg xmlns="http://www.w3.org/2000/svg" width="160" height="22" viewBox="0 0 160 22" aria-label="Ediz & Co." style="display:block">
    <text x="0" y="17" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:17px;font-weight:700;fill:#F4F0E8;letter-spacing:0.01em">Ediz &amp; Co.</text>
  </svg>
  <ul class="foot-links">
    <li><a href="#iletisim">İletişim</a></li>
    <li><a href="aydinlatma_metni.md">KVKK Aydınlatma Metni</a></li>
  </ul>
  <p class="foot-r">© 2026 Ediz &amp; Co.</p>
</footer>

<script>
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('on'); });
  }, { threshold: 0.06 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
</script>

</body>"""

html = re.sub(r'<body>.*</body>', body_content, html, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Index html overwritten successfully!")
