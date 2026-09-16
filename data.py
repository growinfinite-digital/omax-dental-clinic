# -*- coding: utf-8 -*-
CLINIC = {
    "name": "Omax Dental & Maxillofacial Center",
    "phone_display": "+91 97632 36116",
    "phone_tel": "+919763236116",
    "whatsapp": "https://wa.me/919763236116?text=Hello%2C%20I%27d%20like%20to%20book%20an%20appointment.",
    "email": "omaxdentalandmaxillofacial@gmail.com",
    "address_line1": "Omkar Society, Laxmi Polyclinic, Vishal Nagar",
    "address_line2": "Pimple Nilakh, Wakad, Pimpri-Chinchwad, Pune, Maharashtra 401127",
    "address_full": "Omkar society, laxmi polyclinic, vishal nagar, pimple nilakh, Wakad, Pimpri-Chinchwad, Pune, Maharashtra 401127",
    "maps_link": "https://maps.app.goo.gl/69Xu9zCsujwmAiX39",
    "hours": [("Monday – Saturday", "10:00 AM – 1:30 PM"), ("Monday – Saturday", "5:00 PM – 9:00 PM"), ("Sunday", "Closed")],
}

MAPS_EMBED = "https://www.google.com/maps?q=Omax%20Dental%20%26%20Maxillofacial%20Center%2C%20Omkar%20Society%2C%20Vishal%20Nagar%2C%20Pimple%20Nilakh%2C%20Wakad%2C%20Pimpri-Chinchwad%2C%20Pune%2C%20Maharashtra%20401127&output=embed"

DOCTORS = [
    {
        "name": "Dr. Mahesh Pund",
        "slug": "dr-mahesh-pund",
        "qual": "BDS, MDS",
        "role": "Oral &amp; Maxillofacial Surgeon",
        "exp": "9 Years",
        "reg": "A-36669",
        "bio": "Dr. Mahesh Pund leads surgical care at Omax Dental, with nine years dedicated to oral and maxillofacial procedures — from wisdom tooth extractions and dental implants to facial trauma and jaw surgery. He combines a precise surgical hand with a calm, unhurried chairside manner, and is known locally for taking the time to walk patients through every step before it happens.",
    },
    {
        "name": "Dr. Ashwini Jadhav-Pund",
        "slug": "dr-ashwini-jadhav-pund",
        "qual": "BDS, MDS",
        "role": "Periodontist",
        "exp": "9 Years",
        "reg": "A-39365",
        "bio": "Dr. Ashwini Jadhav-Pund specialises in the health of gums and the structures that support every tooth. With nine years of focused periodontal practice, she treats everything from early gum disease to complex full-mouth rehabilitation, and is especially attentive to patients who feel anxious about dental visits.",
    },
]

WHY_CHOOSE = [
    ("Experienced MDS Specialists", "Every treatment plan is led by post-graduate specialists, not generalists — so the person treating you has trained specifically in that field.", "cap"),
    ("Painless Dentistry", "Modern anaesthesia protocols and a gentle touch mean most patients describe their visit as far more comfortable than they expected.", "drop"),
    ("Advanced Digital Dentistry", "Digital X-rays and precision diagnostics let us plan treatment accurately, with less guesswork and fewer visits.", "scan"),
    ("Latest Equipment", "The clinic is equipped with modern instrumentation maintained to current clinical standards, upgraded as technology moves forward.", "tool"),
    ("Sterilization Standards", "Strict, documented sterilization protocols are followed for every instrument, every patient, without exception.", "shield"),
    ("Premium Patient Care", "From the first call to the final follow-up, care is personal — you're treated as a patient, not a number on a schedule.", "heart"),
    ("Honest Advice", "You'll only ever be advised on treatment you actually need — explained clearly, with the reasoning behind it.", "chat"),
    ("Personalized Treatment", "No two smiles are alike. Every plan is built around your specific teeth, budget, and comfort level.", "smile"),
]

ICONS = {
    "cap": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 3 2 8l10 5 8-4.2V15" stroke-linecap="round" stroke-linejoin="round"/><path d="M6 10.5V16c0 1.5 3 3 6 3s6-1.5 6-3v-5.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "drop": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 3s6 6.5 6 11a6 6 0 1 1-12 0c0-4.5 6-11 6-11Z" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "scan": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M4 8V5a1 1 0 0 1 1-1h3M20 8V5a1 1 0 0 0-1-1h-3M4 16v3a1 1 0 0 0 1 1h3M20 16v3a1 1 0 0 1-1 1h-3M4 12h16" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "tool": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M14.7 6.3a4 4 0 0 1-5.4 5.4L4 17l3 3 5.3-5.3a4 4 0 0 1 5.4-5.4L21 6l-3-3-3.3 3.3Z" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 3 4 6v6c0 4.5 3.4 7.7 8 9 4.6-1.3 8-4.5 8-9V6l-8-3Z" stroke-linecap="round" stroke-linejoin="round"/><path d="m9 12 2 2 4-4" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 20s-7-4.4-9.5-9A5.5 5.5 0 0 1 12 6a5.5 5.5 0 0 1 9.5 5c-2.5 4.6-9.5 9-9.5 9Z" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M4 5h16v11H8l-4 4V5Z" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "smile": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M8 13s1.5 3 4 3 4-3 4-3M9 9h.01M15 9h.01" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="m5 13 4 4L19 7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M6.6 10.8c1.4 2.8 3.7 5.1 6.5 6.5l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.5.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.4 21 3 13.6 3 4.7c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.5.1.4 0 .8-.2 1l-2.3 2.2Z" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M4 6h16v12H4V6Z" stroke-linecap="round" stroke-linejoin="round"/><path d="m4 7 8 6 8-6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 21s7-6.6 7-11.5A7 7 0 0 0 5 9.5C5 14.4 12 21 12 21Z" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="9.5" r="2.4"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M20 12a8 8 0 1 1-12.1-6.9L4 20l5.1-1.9A8 8 0 0 0 20 12Z" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "insta": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><rect x="4" y="4" width="16" height="16" rx="5"/><circle cx="12" cy="12" r="3.4"/><circle cx="16.6" cy="7.4" r="1"/></svg>',
    "fb": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M14 9h2V6h-2c-1.7 0-3 1.3-3 3v2H9v3h2v6h3v-6h2.2l.8-3H14V9Z" stroke-linejoin="round"/></svg>',
    "gbp": '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M8 12h8M12 8v8" stroke-linecap="round"/></svg>',
}

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("doctors.html", "Doctors"),
    ("treatments.html", "Treatments"),
    ("gallery.html", "Smile Gallery"),
    ("contact.html", "Contact"),
]

TESTIMONIALS = [
    ("Sanika R.", "Pimple Nilakh", "Root Canal Treatment", "I put off my root canal for months out of fear. Dr. Pund made the whole procedure painless and explained every step. Genuinely the calmest dental visit I've had."),
    ("Omkar D.", "Wakad", "Dental Implants", "Got a dental implant done after years of avoiding it. The planning was thorough, the clinic is spotless, and the results look completely natural."),
    ("Priyanka S.", "Baner", "Smile Designing", "The smile designing consultation alone was worth it — they showed me exactly what to expect before committing to anything. Beautiful, honest work."),
    ("Rahul K.", "Aundh", "Wisdom Tooth Removal", "Had my wisdom tooth removed by Dr. Mahesh Pund. Quick, precise, and recovery was far easier than I'd braced myself for."),
    ("Neha T.", "Hinjewadi", "Gum Treatment", "Dr. Ashwini treated my bleeding gums with so much patience. No pressure to over-treat — just clear, honest advice."),
    ("Aditya M.", "Balewadi", "Full Mouth Rehabilitation", "Full mouth rehabilitation changed how I eat and smile. The team at Omax mapped out every stage clearly from day one."),
]

FAQS_HOME = [
    ("Where is Omax Dental &amp; Maxillofacial Center located?",
     "The clinic is in Omkar Society, Laxmi Polyclinic, Vishal Nagar, Pimple Nilakh, easily reached from Wakad, Pimpri-Chinchwad and Pune."),
    ("What are your clinic timings?",
     "We're open Monday to Saturday, 10:00 AM – 1:30 PM and 5:00 PM – 9:00 PM. We're closed on Sundays."),
    ("Do you treat dental emergencies?",
     "We do not currently offer emergency dental services. For urgent care, please contact your nearest emergency hospital."),
    ("Do I need an appointment before visiting?",
     "Yes, we recommend calling or messaging us on WhatsApp first so we can plan enough time for your consultation."),
    ("Who are the doctors at Omax Dental?",
     "The clinic is led by Dr. Mahesh Pund, an Oral &amp; Maxillofacial Surgeon, and Dr. Ashwini Jadhav-Pund, a Periodontist — both BDS, MDS with nine years of experience."),
    ("Is teeth whitening or smile designing available?",
     "Yes, Smile Designing and cosmetic treatments including veneers and whitening-adjacent procedures are offered after an in-person consultation."),
    ("Do you provide dental implants?",
     "Yes, dental implants are one of our core specialisations, planned and placed under the surgical expertise of Dr. Mahesh Pund."),
    ("Is the clinic suitable for children?",
     "Yes, we offer Pediatric Dentistry in a calm, patient-friendly environment suited to younger patients."),
    ("How experienced are the doctors?",
     "Both lead doctors have nine years of dedicated clinical experience and hold MDS specialisations in their respective fields."),
    ("Do you accept walk-in patients?",
     "We accommodate walk-ins where possible, but calling or WhatsApping ahead ensures shorter waiting time."),
    ("What areas do you serve?",
     "We regularly see patients from Pimple Nilakh, Vishal Nagar, Wakad, Pimpri-Chinchwad, Aundh, Baner, Hinjewadi and Balewadi."),
    ("How can I book an appointment?",
     "Simply call +91 97632 36116 or message us on WhatsApp and we'll confirm a convenient slot for you."),
]

PRIVACY_SECTIONS = [
    ("Information We Collect", ["Contact details you share with us by phone, WhatsApp or email, such as your name, phone number and reason for visiting.",
                                  "Clinical information recorded during your consultation and treatment, kept strictly for the purpose of providing dental care."]),
    ("How We Use Your Information", ["To schedule and manage your appointments.", "To communicate treatment plans, follow-ups and reminders.",
                                       "To maintain accurate dental and medical records as required by good clinical practice."]),
    ("How We Protect Your Information", ["Patient records are stored securely and access is limited to authorised clinical staff.",
                                           "We do not sell, rent or trade patient information to third parties."]),
    ("Third-Party Services", ["Our website may link to WhatsApp, Google Maps and social media platforms, each governed by their own privacy policies."]),
    ("Your Rights", ["You may request access to, or correction of, your personal information held by the clinic at any time by contacting us directly."]),
    ("Contact Us", ["For any questions about this privacy policy, please reach us at omaxdentalandmaxillofacial@gmail.com or +91 97632 36116."]),
]
