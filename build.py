# -*- coding: utf-8 -*-
import os, re
from data import CLINIC, DOCTORS, WHY_CHOOSE, ICONS, NAV, TESTIMONIALS, FAQS_HOME, PRIVACY_SECTIONS, MAPS_EMBED
from treatments_data import TREATMENTS

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.omaxdentalclinic.in"  # placeholder — update once the live domain is chosen

def wa(text=None):
    return CLINIC["whatsapp"]

def tel():
    return "tel:" + CLINIC["phone_tel"]

def rel(depth):
    return "" if depth == 0 else "../" * depth

def head(title, desc, canonical_path, depth=0, og_image="images/og-cover.jpg", extra_schema=""):
    r = rel(depth)
    canonical = SITE + "/" + canonical_path
    return f"""<meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#222121">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Omax Dental &amp; Maxillofacial Center">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/{og_image}">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{SITE}/{og_image}">

  <link rel="icon" href="{r}images/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&amp;family=Manrope:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{r}css/style.css">
  {extra_schema}"""

LOCAL_BUSINESS_SCHEMA = """<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Dentist",
    "name": "Omax Dental & Maxillofacial Center",
    "image": "%(site)s/images/clinic-exterior.jpg",
    "telephone": "+919763236116",
    "email": "omaxdentalandmaxillofacial@gmail.com",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Omkar Society, Laxmi Polyclinic, Vishal Nagar, Pimple Nilakh, Wakad",
      "addressLocality": "Pimpri-Chinchwad",
      "addressRegion": "Maharashtra",
      "postalCode": "401127",
      "addressCountry": "IN"
    },
    "url": "%(site)s/",
    "priceRange": "$$",
    "openingHoursSpecification": [
      {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"10:00","closes":"13:30"},
      {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"17:00","closes":"21:00"}
    ],
    "medicalSpecialty": ["Dentistry","OralAndMaxillofacialSurgery","Periodontics"],
    "hasMap": "%(maps)s"
  }
  </script>""" % {"site": SITE, "maps": CLINIC["maps_link"]}

def doctor_schema():
    people = []
    for d in DOCTORS:
        people.append("""{
      "@type": "Physician",
      "name": "%s",
      "medicalSpecialty": "%s",
      "hasCredential": "%s"
    }""" % (d["name"], re.sub("<.*?>","",d["role"]), d["qual"]))
    return """<script type="application/ld+json">
  { "@context": "https://schema.org", "@graph": [ %s ] }
  </script>""" % ",".join(people)

def breadcrumb_schema(items, depth):
    # items: list of (name, path)
    els = []
    for i, (name, path) in enumerate(items, start=1):
        url = SITE + "/" + path if path else SITE + "/"
        els.append('{"@type":"ListItem","position":%d,"name":"%s","item":"%s"}' % (i, name, url))
    return """<script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[%s]}
  </script>""" % ",".join(els)

def faq_schema(faqs):
    items = []
    for q, a in faqs:
        qq = re.sub("<.*?>","",q).replace('"','\\"')
        aa = re.sub("<.*?>","",a).replace('"','\\"')
        items.append('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (qq, aa))
    return """<script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}
  </script>""" % ",".join(items)

def header(active, depth=0):
    r = rel(depth)
    links = []
    for href, label in NAV:
        cls = ' class="active"' if href == active else ""
        links.append(f'<a href="{r}{href}"{cls}>{label}</a>')
    return f"""<a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="container bar">
      <a class="brand" href="{r}index.html" aria-label="Omax Dental & Maxillofacial Center — home">
        <img src="{r}images/logo.png" alt="Omax Dental &amp; Maxillofacial Center logo">
        <span class="name">Omax Dental<small>Dental &amp; Maxillofacial Center</small></span>
      </a>
      <nav class="primary-nav" aria-label="Primary">
        {''.join(links)}
      </nav>
      <div class="header-cta">
        <a class="btn btn-outline btn-sm" href="{tel()}"><span class="full">Call Now</span></a>
        <a class="btn btn-gold btn-sm" href="{wa()}" target="_blank" rel="noopener"><span class="full">WhatsApp Us</span></a>
        <button class="menu-toggle" aria-label="Open menu" aria-expanded="false"><span></span></button>
      </div>
    </div>
  </header>"""

def footer(depth=0):
    r = rel(depth)
    treat_links = "".join(f'<li><a href="{r}treatments/{t["slug"]}.html">{t["name"]}</a></li>' for t in TREATMENTS[:7])
    return f"""<footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="name">Omax Dental</div>
          <p>Premium dental &amp; maxillofacial care in Vishal Nagar, Pimple Nilakh — precise, honest, and personal, from routine cleanings to complex surgical care.</p>
          <div class="social-row">
            <a href="#" aria-label="Omax Dental on Instagram">{ICONS['insta']}</a>
            <a href="#" aria-label="Omax Dental on Facebook">{ICONS['fb']}</a>
            <a href="{CLINIC['maps_link']}" target="_blank" rel="noopener" aria-label="Omax Dental on Google Business Profile">{ICONS['gbp']}</a>
          </div>
        </div>
        <div>
          <h4>Explore</h4>
          <ul>
            <li><a href="{r}about.html">About Us</a></li>
            <li><a href="{r}doctors.html">Our Doctors</a></li>
            <li><a href="{r}treatments.html">All Treatments</a></li>
            <li><a href="{r}gallery.html">Smile Gallery</a></li>
            <li><a href="{r}contact.html">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4>Popular Treatments</h4>
          <ul>{treat_links}</ul>
        </div>
        <div>
          <h4>Visit Us</h4>
          <ul>
            <li>{CLINIC['address_line1']}, {CLINIC['address_line2']}</li>
            <li><a href="{tel()}">{CLINIC['phone_display']}</a></li>
            <li><a href="mailto:{CLINIC['email']}">{CLINIC['email']}</a></li>
            <li>Mon–Sat, 10:00 AM–1:30 PM &amp; 5:00–9:00 PM</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; <span id="year"></span> Omax Dental &amp; Maxillofacial Center. All rights reserved.</span>
        <span><a href="{r}privacy-policy.html">Privacy Policy</a></span>
      </div>
    </div>
  </footer>
  <a class="float-wa" href="{wa()}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{ICONS['wa']}</a>
  <script>document.getElementById('year').textContent = new Date().getFullYear();</script>
  <script src="{r}js/script.js"></script>"""

def page_shell(title, desc, canonical_path, active_nav, body, depth=0, extra_schema="", og_image="images/og-cover.jpg"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(title, desc, canonical_path, depth, og_image, extra_schema)}
</head>
<body>
{header(active_nav, depth)}
<main id="main">
{body}
</main>
{footer(depth)}
</body>
</html>"""

def eyebrow(text):
    return f'<span class="eyebrow">{text}</span>'

def smile_arc(w=64, center=False):
    cls = "smile-arc center" if center else "smile-arc"
    return f'''<span class="{cls}"><svg width="{w}" height="18" viewBox="0 0 64 18" fill="none"><path d="M2 3c8 12 22 12 30 12s22 0 30-12" stroke="#A69152" stroke-width="1.6" stroke-linecap="round"/></svg></span>'''

def check_svg():
    return ICONS['check']

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

print("helpers loaded")

# ================= HOME =================
def build_home():
    why_cards = "\n".join(f'''<div class="why-card reveal">
          <div class="icon">{ICONS[icon]}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>''' for title, desc, icon in WHY_CHOOSE)

    treat_cards = "\n".join(f'''<a class="treat-card reveal" href="treatments/{t['slug']}.html">
          <div class="thumb"><img src="images/treatments/{t['slug']}.jpg" alt="{t['name']} at Omax Dental, Pimple Nilakh" loading="lazy" width="480" height="360"></div>
          <div class="body">
            <h3>{t['name']}</h3>
            <p>{t['short']}</p>
            <span class="view">View Details {ICONS['arrow']}</span>
          </div>
        </a>''' for t in TREATMENTS[:9])

    doctor_cards = "\n".join(f'''<div class="doctor-card reveal">
          <div class="photo"><img src="images/doctors/{d['slug']}.jpg" alt="{d['name']}, {re.sub('<.*?>','',d['role'])} at Omax Dental" loading="lazy" width="420" height="520"></div>
          <div class="info">
            <h3>{d['name']}</h3>
            <span class="role">{d['role']}</span>
            <div class="meta">
              <div><span>Qualification</span><strong>{d['qual']}</strong></div>
              <div><span>Experience</span><strong>{d['exp']}</strong></div>
              <div><span>Registration</span><strong>{d['reg']}</strong></div>
            </div>
            <p class="bio">{d['bio'][:150]}&hellip;</p>
            <div style="margin-top:18px"><a class="btn btn-outline btn-sm" href="doctors.html">Read Full Profile</a></div>
          </div>
        </div>''' for d in DOCTORS)

    gallery_preview = "\n".join(f'''<figure class="reveal"><img src="images/gallery/preview-{i}.jpg" alt="Smile transformation at Omax Dental, {tags}" loading="lazy" width="360" height="{h}"></figure>'''
        for i, (tags, h) in enumerate([("before and after result",300),("clinic interior",420),("treatment in progress",300),("smile close-up",380),("clinic equipment",300),("patient consultation",420)], start=1))

    testi_cards = "\n".join(f'''<div class="testi-card reveal">
          <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p>&ldquo;{quote}&rdquo;</p>
          <footer>{name}<span>{area} &middot; {treat}</span></footer>
        </div>''' for name, area, treat, quote in TESTIMONIALS[:6])

    faq_items = "\n".join(f'''<div class="faq-item">
          <button class="faq-q" aria-expanded="false">{q}<span class="plus"></span></button>
          <div class="faq-a"><p>{a}</p></div>
        </div>''' for q, a in FAQS_HOME)

    body = f"""
  <section class="hero">
    <div class="container grid">
      <div class="hero-copy reveal">
        {eyebrow('Omax Dental &amp; Maxillofacial Center')}
        <h1>Premium Dental Care for Every Smile</h1>
        <p class="lede">Advanced Dental &amp; Maxillofacial Care delivered with precision, compassion, and modern technology &mdash; in the heart of Vishal Nagar, Pimple Nilakh.</p>
        <div class="hero-actions">
          <a class="btn btn-gold" href="{tel()}">{ICONS['phone']} Call Now</a>
          <a class="btn btn-outline" href="{wa()}" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp Us</a>
        </div>
        <div class="hero-strip">
          <div><strong>9+ Yrs</strong><span>Specialist Experience</span></div>
          <div><strong>2</strong><span>MDS Specialists On-Site</span></div>
          <div><strong>21</strong><span>Dental &amp; Surgical Treatments</span></div>
          <div><strong>6</strong><span>Days a Week, By Appointment</span></div>
        </div>
      </div>
      <div class="hero-media reveal reveal-delay-1">
        <div class="hero-frame">
          <img src="images/hero-clinic.jpg" alt="Omax Dental &amp; Maxillofacial Center treatment room in Pimple Nilakh" width="800" height="800">
        </div>
      </div>
    </div>
  </section>

  <section class="on-ivory">
    <div class="container">
      <div class="section-head reveal">
        {eyebrow('Why Choose Us')}
        <h2>Care that feels considered, not rushed</h2>
        <p>Every detail, from sterilization to the first phone call, is built around one idea: you should always know exactly what's happening and why.</p>
      </div>
      <div class="grid-4">{why_cards}</div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head reveal">
        {eyebrow('Treatments')}
        <h2>Comprehensive care, one trusted clinic</h2>
        <p>From routine cleanings to specialist surgical procedures &mdash; every treatment is planned and delivered in-house.</p>
      </div>
      <div class="grid-3">{treat_cards}</div>
      <div class="view-all-wrap reveal"><a class="btn btn-gold" href="treatments.html">View All 21 Treatments {ICONS['arrow']}</a></div>
    </div>
  </section>

  <section class="on-ivory">
    <div class="container">
      <div class="section-head reveal">
        {eyebrow('Meet Our Doctors')}
        <h2>Specialists, not generalists</h2>
        <p>Two MDS-qualified specialists lead every case at Omax Dental, each focused on their own field of expertise.</p>
      </div>
      <div class="grid-2">{doctor_cards}</div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head reveal">
        {eyebrow('Smile Gallery')}
        <h2>Real results from real patients</h2>
        <p>A glimpse at the clinic, our treatments, and the smiles we've helped along the way.</p>
      </div>
      <div class="masonry">{gallery_preview}</div>
      <div class="view-all-wrap reveal"><a class="btn btn-outline" href="gallery.html">View Full Gallery {ICONS['arrow']}</a></div>
    </div>
  </section>

  <section class="on-ivory">
    <div class="container">
      <div class="section-head center reveal">
        {eyebrow('Testimonials')}
        <h2>What patients are saying</h2>
      </div>
      <div class="testi-row">{testi_cards}</div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head reveal">
        {eyebrow('FAQ')}
        <h2>Common questions, answered</h2>
      </div>
      <div class="faq-list">{faq_items}</div>
    </div>
  </section>

  <section class="tight">
    <div class="container">
      <div class="cta-band reveal">
        <div>
          <h2>Ready to book your visit?</h2>
          <p>Call or message us on WhatsApp &mdash; we'll find a time that works for you.</p>
        </div>
        <div class="cta-actions">
          <a class="btn btn-ghost-light" href="{tel()}">{ICONS['phone']} Call Now</a>
          <a class="btn btn-gold" href="{wa()}" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp Us</a>
        </div>
      </div>
    </div>
  </section>
"""
    schema = LOCAL_BUSINESS_SCHEMA + faq_schema(FAQS_HOME)
    html = page_shell(
        "Best Dentist in Pimple Nilakh, Vishal Nagar | Omax Dental &amp; Maxillofacial Center",
        "Premium dental &amp; maxillofacial care in Vishal Nagar, Pimple Nilakh, Pimpri-Chinchwad. Dental implants, root canal, smile designing &amp; more, led by MDS specialists.",
        "index.html", "index.html", body, depth=0, extra_schema=schema
    )
    write("index.html", html)

build_home()
print("home built")

# ================= ABOUT =================
def build_about():
    body = f"""
  <section class="hero" style="padding-bottom:56px;">
    <div class="container grid">
      <div class="hero-copy reveal">
        {eyebrow('About Omax Dental')}
        <h1>Dentistry built on trust, precision and time</h1>
        <p class="lede">Omax Dental &amp; Maxillofacial Center was founded on a simple premise: patients deserve specialists, honest advice, and care that never feels rushed.</p>
      </div>
      <div class="hero-media reveal reveal-delay-1">
        <div class="hero-frame">
          <img src="images/about-clinic.jpg" alt="Inside Omax Dental &amp; Maxillofacial Center, Pimple Nilakh" width="800" height="800">
        </div>
      </div>
    </div>
  </section>

  <section class="on-ivory">
    <div class="container split">
      <div class="reveal">
        <img class="rounded" src="images/about-mission.jpg" alt="Consultation room at Omax Dental, Vishal Nagar">
      </div>
      <div class="copy-block reveal">
        {eyebrow('Our Mission')}
        <h2>Care that respects your time, your teeth, and your trust</h2>
        <p>Our mission is straightforward &mdash; deliver dental and maxillofacial care that's clinically excellent and genuinely comfortable, without ever recommending treatment a patient doesn't need. Every plan starts with listening.</p>
        {eyebrow('Our Vision')}
        <h2>To be Pimple Nilakh's most trusted dental address</h2>
        <p>We want patients across Vishal Nagar, Wakad and Pimpri-Chinchwad to think of Omax Dental first &mdash; not because we're the loudest, but because the care speaks for itself, visit after visit.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head reveal">
        {eyebrow('Why Patients Trust Us')}
        <h2>The standards behind every appointment</h2>
      </div>
      <div class="grid-4">
        <div class="why-card reveal"><div class="icon">{ICONS['scan']}</div><h3>Modern Dentistry</h3><p>Digital X-rays and current clinical techniques guide every diagnosis and treatment plan.</p></div>
        <div class="why-card reveal"><div class="icon">{ICONS['shield']}</div><h3>Sterilization</h3><p>Documented sterilization protocols are followed for every instrument, without exception.</p></div>
        <div class="why-card reveal"><div class="icon">{ICONS['heart']}</div><h3>Patient-First Philosophy</h3><p>Treatment recommendations are based purely on clinical need, explained in plain language.</p></div>
        <div class="why-card reveal"><div class="icon">{ICONS['cap']}</div><h3>Specialist-Led</h3><p>MDS specialists lead surgical and periodontal cases in-house, not general practitioners.</p></div>
      </div>
    </div>
  </section>

  <section class="on-ivory">
    <div class="container">
      <div class="section-head reveal">
        {eyebrow('Meet the Doctors')}
        <h2>The team behind your care</h2>
      </div>
      <div class="grid-2">
        <div class="doctor-card reveal">
          <div class="photo"><img src="images/doctors/dr-mahesh-pund.jpg" alt="Dr. Mahesh Pund, Oral &amp; Maxillofacial Surgeon" loading="lazy" width="420" height="520"></div>
          <div class="info"><h3>Dr. Mahesh Pund</h3><span class="role">Oral &amp; Maxillofacial Surgeon</span>
            <div class="meta"><div><span>Qualification</span><strong>BDS, MDS</strong></div><div><span>Experience</span><strong>9 Years</strong></div><div><span>Registration</span><strong>A-36669</strong></div></div>
          </div>
        </div>
        <div class="doctor-card reveal">
          <div class="photo"><img src="images/doctors/dr-ashwini-jadhav-pund.jpg" alt="Dr. Ashwini Jadhav-Pund, Periodontist" loading="lazy" width="420" height="520"></div>
          <div class="info"><h3>Dr. Ashwini Jadhav-Pund</h3><span class="role">Periodontist</span>
            <div class="meta"><div><span>Qualification</span><strong>BDS, MDS</strong></div><div><span>Experience</span><strong>9 Years</strong></div><div><span>Registration</span><strong>A-39365</strong></div></div>
          </div>
        </div>
      </div>
      <div class="view-all-wrap reveal"><a class="btn btn-gold" href="doctors.html">View Full Profiles {ICONS['arrow']}</a></div>
    </div>
  </section>

  <section class="tight">
    <div class="container">
      <div class="cta-band reveal">
        <div><h2>Serving Pimple Nilakh &amp; beyond</h2><p>Vishal Nagar &middot; Wakad &middot; Pimpri-Chinchwad &middot; Aundh &middot; Baner &middot; Hinjewadi &middot; Balewadi</p></div>
        <div class="cta-actions">
          <a class="btn btn-ghost-light" href="{tel()}">{ICONS['phone']} Call Now</a>
          <a class="btn btn-gold" href="{wa()}" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp Us</a>
        </div>
      </div>
    </div>
  </section>
"""
    schema = LOCAL_BUSINESS_SCHEMA + breadcrumb_schema([("Home",""),("About","about.html")], 0)
    html = page_shell(
        "About Us | Omax Dental &amp; Maxillofacial Center, Pimple Nilakh",
        "Learn about Omax Dental &amp; Maxillofacial Center in Vishal Nagar, Pimple Nilakh &mdash; our mission, our specialists, and why patients across Pimpri-Chinchwad trust us.",
        "about.html", "about.html", body, depth=0, extra_schema=schema
    )
    write("about.html", html)

build_about()
print("about built")

# ================= DOCTORS =================
def build_doctors():
    cards = []
    for d in DOCTORS:
        cards.append(f'''<div class="doctor-card reveal">
          <div class="photo"><img src="images/doctors/{d['slug']}.jpg" alt="{d['name']}, {re.sub('<.*?>','',d['role'])} at Omax Dental, Pimple Nilakh" loading="lazy" width="420" height="520"></div>
          <div class="info">
            <h3>{d['name']}</h3>
            <span class="role">{d['role']}</span>
            <div class="meta">
              <div><span>Qualification</span><strong>{d['qual']}</strong></div>
              <div><span>Experience</span><strong>{d['exp']}</strong></div>
              <div><span>Registration No.</span><strong>{d['reg']}</strong></div>
            </div>
            <p class="bio">{d['bio']}</p>
            <div class="hero-actions" style="margin-top:20px">
              <a class="btn btn-outline btn-sm" href="{tel()}">{ICONS['phone']} Call Now</a>
              <a class="btn btn-gold btn-sm" href="{wa()}" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp</a>
            </div>
          </div>
        </div>''')
    body = f"""
  <section class="treat-hero">
    <div class="container">
      <nav class="breadcrumb reveal" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>Doctors</span></nav>
      {eyebrow('Our Doctors')}
      <h1>Specialists you can put your trust in</h1>
      <p class="lede">Two MDS-qualified specialists, each with nine years of focused clinical experience, lead every case at Omax Dental &amp; Maxillofacial Center.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="grid-2">{''.join(cards)}</div>
    </div>
  </section>
  <section class="on-ivory tight">
    <div class="container">
      <div class="cta-band reveal">
        <div><h2>Book a consultation</h2><p>Speak directly with Dr. Pund or Dr. Jadhav-Pund about your dental concerns.</p></div>
        <div class="cta-actions">
          <a class="btn btn-ghost-light" href="{tel()}">{ICONS['phone']} Call Now</a>
          <a class="btn btn-gold" href="{wa()}" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp Us</a>
        </div>
      </div>
    </div>
  </section>
"""
    schema = LOCAL_BUSINESS_SCHEMA + doctor_schema() + breadcrumb_schema([("Home",""),("Doctors","doctors.html")], 0)
    html = page_shell(
        "Our Doctors | Dr. Mahesh Pund &amp; Dr. Ashwini Jadhav-Pund | Omax Dental",
        "Meet Dr. Mahesh Pund (Oral &amp; Maxillofacial Surgeon) and Dr. Ashwini Jadhav-Pund (Periodontist) &mdash; MDS specialists at Omax Dental, Pimple Nilakh.",
        "doctors.html", "doctors.html", body, depth=0, extra_schema=schema
    )
    write("doctors.html", html)

build_doctors()
print("doctors built")

# ================= TREATMENTS LISTING =================
def build_treatments_listing():
    cards = "\n".join(f'''<a class="treat-card reveal" href="treatments/{t['slug']}.html">
          <div class="thumb"><img src="images/treatments/{t['slug']}.jpg" alt="{t['name']} treatment at Omax Dental, {t['area']}" loading="lazy" width="480" height="360"></div>
          <div class="body">
            <h3>{t['name']}</h3>
            <p>{t['short']}</p>
            <span class="view">View Details {ICONS['arrow']}</span>
          </div>
        </a>''' for t in TREATMENTS)
    body = f"""
  <section class="treat-hero">
    <div class="container">
      <nav class="breadcrumb reveal" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>Treatments</span></nav>
      {eyebrow('All Treatments')}
      <h1>Complete dental &amp; maxillofacial care, under one roof</h1>
      <p class="lede">From routine cleanings to specialist surgical procedures &mdash; 21 treatments, each led by a qualified specialist at our Pimple Nilakh clinic.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="grid-3">{cards}</div>
    </div>
  </section>
  <section class="on-ivory tight">
    <div class="container">
      <div class="cta-band reveal">
        <div><h2>Not sure which treatment you need?</h2><p>Call or WhatsApp us &mdash; we'll help you figure out the right first step.</p></div>
        <div class="cta-actions">
          <a class="btn btn-ghost-light" href="{tel()}">{ICONS['phone']} Call Now</a>
          <a class="btn btn-gold" href="{wa()}" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp Us</a>
        </div>
      </div>
    </div>
  </section>
"""
    schema = LOCAL_BUSINESS_SCHEMA + breadcrumb_schema([("Home",""),("Treatments","treatments.html")], 0)
    html = page_shell(
        "Dental Treatments in Pimple Nilakh | Implants, Root Canal, Braces &amp; More",
        "Explore all 21 dental &amp; maxillofacial treatments at Omax Dental, Pimple Nilakh &mdash; dental implants, root canal, smile designing, braces, surgery and more.",
        "treatments.html", "treatments.html", body, depth=0, extra_schema=schema
    )
    write("treatments.html", html)

build_treatments_listing()
print("treatments listing built")

# ================= TREATMENT DETAIL PAGES =================
def build_treatment_page(t, idx):
    others = [x for x in TREATMENTS if x['slug'] != t['slug']]
    related = others[idx % len(others):] + others[:idx % len(others)]
    related = related[:5]

    benefits_html = "\n".join(f'<li>{check_svg()}<span>{b}</span></li>' for b in t['benefits'])
    steps_html = "\n".join(f'<li><div><strong>{title}</strong><span>{desc}</span></div></li>' for title, desc in t['procedure'])
    who_html = "\n".join(f'<li>{check_svg()}<span>{w}</span></li>' for w in t['who'])
    faq_html = "\n".join(f'''<div class="faq-item">
          <button class="faq-q" aria-expanded="false">{q}<span class="plus"></span></button>
          <div class="faq-a"><p>{a}</p></div>
        </div>''' for q, a in t['faqs'])
    related_html = "\n".join(f'<a href="{r["slug"]}.html">{r["name"]} {ICONS["arrow"]}</a>' for r in related)

    body = f"""
  <section class="treat-hero">
    <div class="container">
      <nav class="breadcrumb reveal" aria-label="Breadcrumb"><a href="../index.html">Home</a><span>/</span><a href="../treatments.html">Treatments</a><span>/</span><span>{t['name']}</span></nav>
      {eyebrow(t['area'] + ' &middot; Omax Dental')}
      <h1>{t['name']} in {t['area']}, Pimpri-Chinchwad</h1>
      <p class="lede">{t['lede']}</p>
      <div class="hero-actions">
        <a class="btn btn-gold" href="{tel()}">{ICONS['phone']} Call Now</a>
        <a class="btn btn-outline" href="{wa()}" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp Us</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container split">
      <div class="copy-block reveal">
        {eyebrow('About the Treatment')}
        <h2>What it involves</h2>
        <p>{t['about']}</p>

        {eyebrow('Benefits')}
        <h2>Why patients choose this treatment</h2>
        <ul class="check-list">{benefits_html}</ul>

        {eyebrow('Procedure')}
        <h2>What to expect, step by step</h2>
        <ol class="step-list">{steps_html}</ol>

        {eyebrow('Who Needs It')}
        <h2>Signs this treatment may help you</h2>
        <ul class="check-list">{who_html}</ul>

        {eyebrow('Recovery')}
        <h2>Healing &amp; aftercare</h2>
        <p>{t['recovery']}</p>

        {eyebrow('FAQ')}
        <h2>Frequently asked questions</h2>
        <div class="faq-list">{faq_html}</div>
      </div>

      <aside class="reveal">
        <img class="rounded" src="../images/treatments/{t['slug']}-detail.jpg" alt="{t['name']} procedure at Omax Dental, {t['area']}" loading="lazy" style="margin-bottom:24px;">
        <div class="sidebar-card">
          <h3>Book This Treatment</h3>
          <p style="margin-top:8px;font-size:.9rem;color:var(--ink-70)">Call or WhatsApp us to schedule a consultation with our specialists.</p>
          <div class="cta-mini">
            <a class="btn btn-gold" href="{tel()}">{ICONS['phone']} Call Now</a>
            <a class="btn btn-outline" href="{wa()}" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp Us</a>
          </div>
        </div>
        <div class="sidebar-card" style="margin-top:20px;">
          <h3>Related Treatments</h3>
          <ul>{related_html}</ul>
        </div>
      </aside>
    </div>
  </section>

  <section class="on-ivory tight">
    <div class="container">
      <div class="cta-band reveal">
        <div><h2>Serving {t['area']} &amp; nearby areas</h2><p>Vishal Nagar &middot; Wakad &middot; Pimpri-Chinchwad &middot; Aundh &middot; Baner &middot; Hinjewadi &middot; Balewadi</p></div>
        <div class="cta-actions">
          <a class="btn btn-ghost-light" href="{tel()}">{ICONS['phone']} Call Now</a>
          <a class="btn btn-gold" href="{wa()}" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp Us</a>
        </div>
      </div>
    </div>
  </section>
"""
    schema = (LOCAL_BUSINESS_SCHEMA
              + breadcrumb_schema([("Home",""),("Treatments","treatments.html"),(t['name'], f"treatments/{t['slug']}.html")], 1)
              + faq_schema(t['faqs']))
    plain_name = re.sub("<.*?>","",t['name'])
    area_suffix = t['area'] if t['area'] == "Pimple Nilakh" else f"{t['area']}, Pimple Nilakh"
    title = f"{plain_name} in {area_suffix} | Omax Dental"
    desc = f"{plain_name} at Omax Dental &amp; Maxillofacial Center, {area_suffix}. {t['short']} Call or WhatsApp to book."
    html = page_shell(title, desc, f"treatments/{t['slug']}.html", "treatments.html", body, depth=1, extra_schema=schema,
                       og_image=f"images/treatments/{t['slug']}.jpg")
    write(f"treatments/{t['slug']}.html", html)

for i, t in enumerate(TREATMENTS):
    build_treatment_page(t, i)
print(f"{len(TREATMENTS)} treatment pages built")

# ================= GALLERY =================
def build_gallery():
    groups = [
        ("before-after", "Before &amp; After", 8),
        ("clinic", "Clinic", 6),
        ("treatments", "Treatments", 6),
    ]
    filters = '<button class="gfilter active" data-filter="all" aria-pressed="true">All</button>' + \
        "".join(f'<button class="gfilter" data-filter="{g}" aria-pressed="false">{label}</button>' for g, label, n in groups)
    figs = []
    heights = [280,340,300,380,260,320,300,360]
    for g, label, n in groups:
        for i in range(1, n+1):
            h = heights[(i + len(g)) % len(heights)]
            figs.append(f'<figure data-group="{g}"><img src="images/gallery/{g}-{i}.jpg" alt="{label} &mdash; Omax Dental, Pimple Nilakh" loading="lazy" width="360" height="{h}"><figcaption>{label}</figcaption></figure>')
    body = f"""
  <section class="treat-hero">
    <div class="container">
      <nav class="breadcrumb reveal" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>Smile Gallery</span></nav>
      {eyebrow('Smile Gallery')}
      <h1>Real transformations from our Pimple Nilakh clinic</h1>
      <p class="lede">Before-and-after results, a look inside the clinic, and treatments in progress.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="gallery-filters reveal">{filters}</div>
      <div class="masonry">{''.join(figs)}</div>
    </div>
  </section>
  <div class="lightbox" role="dialog" aria-modal="true" aria-label="Enlarged image">
    <button class="lightbox-close" aria-label="Close image">&times;</button>
    <img src="" alt="">
  </div>
  <section class="on-ivory tight">
    <div class="container">
      <div class="cta-band reveal">
        <div><h2>Like what you see?</h2><p>Your own smile transformation could start with a single call.</p></div>
        <div class="cta-actions">
          <a class="btn btn-ghost-light" href="{tel()}">{ICONS['phone']} Call Now</a>
          <a class="btn btn-gold" href="{wa()}" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp Us</a>
        </div>
      </div>
    </div>
  </section>
"""
    schema = LOCAL_BUSINESS_SCHEMA + breadcrumb_schema([("Home",""),("Smile Gallery","gallery.html")], 0)
    html = page_shell(
        "Smile Gallery | Before &amp; After Results | Omax Dental, Pimple Nilakh",
        "Browse real before-and-after smile transformations, clinic photos, and treatments in progress at Omax Dental &amp; Maxillofacial Center, Pimple Nilakh.",
        "gallery.html", "gallery.html", body, depth=0, extra_schema=schema
    )
    write("gallery.html", html)

build_gallery()
print("gallery built")

# ================= CONTACT =================
def build_contact():
    body = f"""
  <section class="treat-hero">
    <div class="container">
      <nav class="breadcrumb reveal" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>Contact</span></nav>
      {eyebrow('Contact Us')}
      <h1>Let's get your visit booked</h1>
      <p class="lede">Call or WhatsApp us directly &mdash; no forms, no waiting for a callback.</p>
    </div>
  </section>
  <section>
    <div class="container contact-grid">
      <div class="reveal">
        <div class="contact-card">
          <h3>Get in Touch</h3>
          <div class="contact-row"><div class="ic">{ICONS['pin']}</div><div><strong>Address</strong><span>{CLINIC['address_line1']}, {CLINIC['address_line2']}</span></div></div>
          <div class="contact-row"><div class="ic">{ICONS['phone']}</div><div><strong>Phone</strong><span><a href="{tel()}">{CLINIC['phone_display']}</a></span></div></div>
          <div class="contact-row"><div class="ic">{ICONS['wa']}</div><div><strong>WhatsApp</strong><span><a href="{wa()}" target="_blank" rel="noopener">{CLINIC['phone_display']}</a></span></div></div>
          <div class="contact-row"><div class="ic">{ICONS['mail']}</div><div><strong>Email</strong><span><a href="mailto:{CLINIC['email']}">{CLINIC['email']}</a></span></div></div>
          <div class="contact-row"><div class="ic">{ICONS['clock']}</div><div><strong>Business Hours</strong><span>Mon&ndash;Sat, 10:00 AM&ndash;1:30 PM &amp; 5:00&ndash;9:00 PM<br>Sunday: Closed</span></div></div>
          <div class="hero-actions" style="margin-top:22px">
            <a class="btn btn-gold" href="{tel()}">{ICONS['phone']} Call Now</a>
            <a class="btn btn-outline" href="{wa()}" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp Us</a>
          </div>
        </div>
        <div class="contact-card">
          <h3>Follow Us</h3>
          <p style="margin-top:8px;font-size:.9rem;color:var(--ink-70)">Stay updated with clinic news and smile stories.</p>
          <div class="social-row">
            <a href="#" aria-label="Omax Dental on Instagram">{ICONS['insta']}</a>
            <a href="#" aria-label="Omax Dental on Facebook">{ICONS['fb']}</a>
            <a href="{CLINIC['maps_link']}" target="_blank" rel="noopener" aria-label="Omax Dental on Google Business Profile">{ICONS['gbp']}</a>
          </div>
        </div>
      </div>
      <div class="reveal reveal-delay-1">
        <div class="map-frame">
          <iframe src="{MAPS_EMBED}" title="Omax Dental &amp; Maxillofacial Center location map" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
        </div>
        <div class="view-all-wrap" style="margin-top:18px;">
          <a class="btn btn-outline" href="{CLINIC['maps_link']}" target="_blank" rel="noopener">Get Directions {ICONS['arrow']}</a>
        </div>
      </div>
    </div>
  </section>
"""
    schema = LOCAL_BUSINESS_SCHEMA + breadcrumb_schema([("Home",""),("Contact","contact.html")], 0)
    html = page_shell(
        "Contact Us | Omax Dental &amp; Maxillofacial Center, Pimple Nilakh",
        "Visit or contact Omax Dental &amp; Maxillofacial Center in Vishal Nagar, Pimple Nilakh, Pimpri-Chinchwad. Call or WhatsApp +91 97632 36116 to book.",
        "contact.html", "contact.html", body, depth=0, extra_schema=schema
    )
    write("contact.html", html)

build_contact()
print("contact built")

# ================= PRIVACY =================
def build_privacy():
    sections = "\n".join(f"<h2>{title}</h2>{''.join(f'<p>{item}</p>' if False else '' for item in [])}<ul>{''.join(f'<li>{item}</li>' for item in items)}</ul>" for title, items in PRIVACY_SECTIONS)
    body = f"""
  <section class="treat-hero">
    <div class="container">
      <nav class="breadcrumb reveal" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>Privacy Policy</span></nav>
      {eyebrow('Privacy Policy')}
      <h1>How we handle your information</h1>
      <p class="lede">Last updated August 2026. This policy explains what information Omax Dental collects and how it's used.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="privacy-body reveal" style="max-width:760px;">
        {sections}
      </div>
    </div>
  </section>
"""
    schema = breadcrumb_schema([("Home",""),("Privacy Policy","privacy-policy.html")], 0)
    html = page_shell(
        "Privacy Policy | Omax Dental &amp; Maxillofacial Center",
        "Read the privacy policy for Omax Dental &amp; Maxillofacial Center, Pimple Nilakh &mdash; how patient information is collected, used and protected.",
        "privacy-policy.html", "", body, depth=0, extra_schema=schema
    )
    write("privacy-policy.html", html)

build_privacy()
print("privacy built")

# ================= ROBOTS + SITEMAP =================
def build_robots_sitemap():
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    urls = ["index.html","about.html","doctors.html","treatments.html","gallery.html","contact.html","privacy-policy.html"]
    urls += [f"treatments/{t['slug']}.html" for t in TREATMENTS]
    entries = "\n".join(f"  <url><loc>{SITE}/{u}</loc><changefreq>monthly</changefreq></url>" for u in urls)
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n'
    write("sitemap.xml", sitemap)

build_robots_sitemap()
print("robots + sitemap built")
