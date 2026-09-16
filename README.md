# Omax Dental & Maxillofacial Center — Website

## What's included
- `index.html`, `about.html`, `doctors.html`, `treatments.html`, `gallery.html`, `contact.html`, `privacy-policy.html`
- `treatments/` — 21 individual SEO-optimized treatment pages
- `css/style.css` — full design system (no inline CSS)
- `js/script.js` — nav, scroll reveal, FAQ accordion, gallery filter + lightbox, ripple buttons
- `robots.txt`, `sitemap.xml`
- `images/` — empty folders matching every `<img>` reference; drop in real photos using the same filenames (see below) and they'll appear automatically. `images/logo.png` is the logo placeholder.
- `data.py`, `treatments_data.py`, `build.py` — the Python content/generator source. Not needed to run the site, but useful if you want to edit copy in one place and regenerate every page instead of hand-editing 29 HTML files. Run with `python3 build.py`.

## Before going live
1. Add real photos into `images/` (clinic, doctors, treatments, gallery, logo) using the existing filenames — every `<img>` already has a descriptive `alt` tag.
2. Update `SITE` in `build.py` (or the `<link rel="canonical">` / `og:url` tags directly in the HTML) to your real domain once purchased, then re-run `python3 build.py` or find-and-replace across the HTML files.
3. Double-check the PIN code in the footer/schema (currently 401127, taken from the address you provided) against your official clinic address.
4. Upload everything to your web host, keeping the folder structure intact.

## Design system
- Colors: white background, near-black text (#222121), gold accent (#EDD471) and dark gold (#A69152) — used sparingly per the brief.
- Type: Cormorant Garamond (headings) + Manrope (body), loaded from Google Fonts.
- Signature motif: a thin gold "smile arc" line used as a section divider throughout — the one recurring visual element instead of generic numbered badges.
- No contact forms anywhere — every CTA is Call Now or WhatsApp Us (pre-filled with "Hello, I'd like to book an appointment.").
