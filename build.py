import json, os, re, html

SRC = "/tmp/wch"
OUT = "/tmp/wch/site"
d = json.load(open(f"{SRC}/extract.json"))
posts = json.load(open(f"{SRC}/posts.json"))
privacy_lines = open(f"{SRC}/privacy.txt").read().split("\n")

NAV = """
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="/"><img src="/assets/logo.png" alt="World Class Housing"></a>
    <nav class="main-nav" id="nav">
      <a href="/services-1">Services</a>
      <a href="/general-6">Properties</a>
      <a href="/about-4">About Us</a>
      <a href="/contact">Contact Us</a>
      <a href="/challenges">Program List</a>
      <a class="btn btn-gold btn-nav" href="/contact">Find Your Stay</a>
    </nav>
    <button class="nav-toggle" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('open')">&#9776;</button>
  </div>
</header>
"""

FOOTER = """
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="f-brand">
      <img src="/assets/logo.png" alt="World Class Housing" class="f-logo">
    </div>
    <div>
      <h4>Contact Us</h4>
      <p>1445 Woodmont Lane #3062<br>Atlanta, GA 30318</p>
      <p><a href="tel:678-661-1746">678-661-1746</a></p>
      <p><a href="mailto:support@worldclasshousing.net">support@worldclasshousing.net</a></p>
    </div>
    <div>
      <h4>Quick Links</h4>
      <p><a href="/">Home</a><br><a href="/contact">Contact Us</a><br><a href="/about-4">About</a><br><a href="/general-6">Properties</a><br><a href="/challenges">Program List</a></p>
    </div>
    <div>
      <h4>Compliance</h4>
      <p><a href="/privacy-policy">Privacy Policy</a><br><a href="/terms-conditions">Terms &amp; Conditions</a></p>
    </div>
  </div>
  <div class="wrap copy"><p>&copy;2024 by World Class Housing.</p></div>
</footer>
"""

def page(title, body, desc="World Class Housing - corporate housing, property management and vacation rentals in Atlanta, GA."):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,600;0,700;1,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
</head>
<body>
{NAV}
<main>
{body}
</main>
{FOOTER}
</body>
</html>"""

CTA = """
<section class="cta-band">
  <div class="wrap">
    <h2>Let's Work Together</h2>
    <p>We utilize targeted marketing and extensive industry knowledge to get top dollar for sellers or find the perfect property for buyers.</p>
    <p>Contact us today to learn how we can help you successfully navigate your home journey!</p>
    <a class="btn btn-gold" href="/contact">Contact Us</a>
  </div>
</section>
"""

def hero(img, kicker, title_html, sub="", buttons=""):
    return f"""
<section class="hero" style="background-image:url('/assets/{img}')">
  <div class="hero-overlay"></div>
  <div class="wrap hero-content">
    {f'<p class="kicker">{kicker}</p>' if kicker else ''}
    <h1>{title_html}</h1>
    <div class="gold-rule"></div>
    {f'<p class="hero-sub">{sub}</p>' if sub else ''}
    {buttons}
  </div>
</section>
"""

def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(content)

# ---------------- HOME ----------------
home_body = hero("hero-home.png", "", "OUR SERVICE IS<br><span class='gold'>WORLD CLASS</span>",
    "World Class Housing will ensure exceptional customer service for our guests, whether its for a vacation or---even relocation!",
    """<div class="btn-row"><a class="btn btn-gold" href="/services-1">View Listings</a><a class="btn btn-outline" href="/contact">Contact Us</a></div>""")
home_body += """
<section class="black-band center">
  <div class="wrap">
    <h2><span class="gold italic big">20</span> Years of Experience</h2>
    <p class="narrow">With 20 years of experience as a top property management company, our corporate housing system is proven to deliver high satisfaction for both owners and tenants.</p>
    <a class="btn btn-outline" href="/about-4">About Us</a>
  </div>
</section>
<section class="light-band">
  <div class="wrap">
    <h2>We Provide Quality</h2>
    <div class="cards3">
      <div class="card">
        <img src="/assets/img-1f0349.jpg" alt="Property Management">
        <h3>Property Management</h3>
        <p>From tenant screening to maintenance and rent collection, we handle it all so you can focus on what matters most</p>
        <a class="btn btn-outline-dark" href="/services-1">Read More</a>
      </div>
      <div class="card">
        <img src="/assets/host-greeting.jpg" alt="Host Greeting Guests">
        <h3>Corporate Housing Vacation Rental</h3>
        <p>Flexible property rentals for corporate clients, traveling nurses, vacationers, and more—short-term or long-term, we’ve got you covered!</p>
        <a class="btn btn-outline-dark" href="/services-1">Read More</a>
      </div>
      <div class="card">
        <img src="/assets/yoga.jpg" alt="Vacation stay">
        <h3>Full Consultation</h3>
        <p>Become a top Airbnb/Vacation rental host with our expert coaching. Learn how to save on expenses and boost your profits!</p>
        <a class="btn btn-outline-dark" href="/services-1">Read More</a>
      </div>
    </div>
  </div>
</section>
<section class="black-band">
  <div class="wrap split">
    <div>
      <h2>Convenient Housing Solutions</h2>
      <p>For business travelers, relocating employees, and project teams, World Class Housing (WCH) offers fully-furnished homes for an exceptional living experience. With flexible leases for short or long-term stays, WCH provides the best local housing options tailored to your needs. Our area experts know the neighborhoods inside out, ensuring the perfect fit for mobile employees or your own housing needs.</p>
      <a class="btn btn-gold" href="/general-6">View More</a>
    </div>
    <img class="split-img" src="/assets/coffee-consult.jpg" alt="Coffee Shop Consultation">
  </div>
</section>
<section class="light-band">
  <div class="wrap">
    <div class="gallery">
      <img src="/assets/g4.jpg" alt="Property kitchen">
      <img src="/assets/g5.jpg" alt="Dining area">
      <img src="/assets/g7.jpg" alt="Property interior">
      <img src="/assets/g8.jpg" alt="Property interior">
      <img src="/assets/g9.jpg" alt="Property interior">
      <img src="/assets/h2.jpg" alt="Bedroom">
      <img src="/assets/h7.jpg" alt="Property photo">
      <img src="/assets/h8.jpg" alt="Property photo">
    </div>
  </div>
</section>
<section class="black-band center">
  <div class="wrap">
    <h2>What We Stand For</h2>
    <div class="cards3 quotes">
      <div class="card quote"><p>"World Class Housing provides a lot of options far as rentals that fit within my requests and budget!"</p><h4>Marcus S.</h4></div>
      <div class="card quote"><p>"They offered a unique blend of comfort, convenience, and efficiency, making it an excellent choice for business travelers and relocating employees."</p><h4>Janet P.</h4></div>
      <div class="card quote"><p>"My recent experience in a stay at a World Class Housing unit surpassed my expectations in several ways."</p><h4>Morgan G.</h4></div>
    </div>
  </div>
</section>
<section class="contact-band" style="background-image:url('/assets/contact-bg.jpg')">
  <div class="contact-overlay"></div>
  <div class="wrap center">
    <h2>Let’s Get Started</h2>
    <p>Get in touch so we can start working together.</p>
    <form class="contact-form" id="contactForm" onsubmit="return sendMail(this)">
      <div class="form-row">
        <input name="firstname" placeholder="First Name" required>
        <input name="lastname" placeholder="Last Name" required>
      </div>
      <input name="email" type="email" placeholder="Email" required>
      <textarea name="message" placeholder="Message" rows="5" required></textarea>
      <button class="btn btn-gold" type="submit">Send</button>
    </form>
  </div>
</section>
<script>
function sendMail(f){
  var body = "Name: " + f.firstname.value + " " + f.lastname.value + "\\nEmail: " + f.email.value + "\\n\\n" + f.message.value;
  window.location.href = "mailto:support@worldclasshousing.net?subject=" + encodeURIComponent("Website inquiry from " + f.firstname.value + " " + f.lastname.value) + "&body=" + encodeURIComponent(body);
  return false;
}
</script>
"""
write("index.html", page("Home | World Class Housing", home_body))

# ---------------- SERVICES ----------------
svc_body = hero("svc-study.jpg", "", "Providing Everything You Need")
svc_body += """
<section class="light-band">
  <div class="wrap">
    <h2 class="center">Services</h2>
    <div class="svc-row">
      <img src="/assets/svc-viewing.jpg" alt="Viewing a Home">
      <div>
        <h3>Property Management</h3>
        <p>WCH handles everything needed to successfully lease your asset, attract responsible tenants, and maximize income. Our expertise spans marketing listings, screening applicants, executing optimal lease agreements, collecting rent on time, coordinating maintenance, and handling evictions if required. Utilizing proven methods, we determine your ideal rental price point to ensure maximum monthly cash flow. We deliver complete peace of mind by keeping your property consistently occupied by pre-qualified tenants.</p>
      </div>
    </div>
    <div class="svc-row flip">
      <img src="/assets/svc-interior.jpg" alt="Apartment Interior with Red Accents">
      <div>
        <h3>Airbnb Vacation Rental</h3>
        <p>WCH offers comprehensive vacation rental management to optimize your property's income and guest experience. Utilizing proven marketing strategies, we attract the ideal renters and determine optimal nightly rates for maximized bookings and revenue. Our dedicated staff handles all guest communications, ensures fast maintenance response, and provides on-call support for a smooth vacation experience. WCH implements strict cleaning protocols between guests, conducts routine property inspections, and provides easy payouts of rental earnings. Partnering with WCH delivers true peace of mind, knowing your vacation rental is in expert hands.</p>
      </div>
    </div>
    <div class="svc-row">
      <img src="/assets/svc-businessman.jpg" alt="Businessman">
      <div>
        <h3>Corporate Housing</h3>
        <p>(WCH) provides fully serviced corporate housing perfectly suited for medical staff, executives, insurance adjusters, construction crews, government employees like FEMA or military, and corporate relocations. Our accommodations encompass apartments, condos, and single-family homes, each fully furnished and equipped with amenities to meet all business needs. WCH handles furnishing, housekeeping, maintenance, utilities, and every detail so guests can focus entirely on their assignments. We deliver flexible corporate housing that reduces company travel costs, enhances employee productivity, and creates a comfortable home base for any industry and purpose.</p>
      </div>
    </div>
  </div>
</section>
""" + CTA
write("services-1/index.html", page("Services | World Class Housing", svc_body))

# Service detail pages (Wix stubs rebuilt from the site's own Services copy)
pm_body = hero("svc-viewing.jpg", "", "Property Management") + """
<section class="light-band"><div class="wrap narrow-text">
<p>WCH handles everything needed to successfully lease your asset, attract responsible tenants, and maximize income. Our expertise spans marketing listings, screening applicants, executing optimal lease agreements, collecting rent on time, coordinating maintenance, and handling evictions if required. Utilizing proven methods, we determine your ideal rental price point to ensure maximum monthly cash flow. We deliver complete peace of mind by keeping your property consistently occupied by pre-qualified tenants.</p>
</div></section>
""" + CTA
write("property-management/index.html", page("Property Management | World Class Housing", pm_body))

ch_body = hero("svc-businessman.jpg", "", "Corporate Housing") + """
<section class="light-band"><div class="wrap narrow-text">
<p>(WCH) provides fully serviced corporate housing perfectly suited for medical staff, executives, insurance adjusters, construction crews, government employees like FEMA or military, and corporate relocations. Our accommodations encompass apartments, condos, and single-family homes, each fully furnished and equipped with amenities to meet all business needs. WCH handles furnishing, housekeeping, maintenance, utilities, and every detail so guests can focus entirely on their assignments. We deliver flexible corporate housing that reduces company travel costs, enhances employee productivity, and creates a comfortable home base for any industry and purpose.</p>
</div></section>
""" + CTA
write("corporate-housing/index.html", page("Corporate Housing | World Class Housing", ch_body))

vr_body = hero("svc-interior.jpg", "", "Vacation Rental") + """
<section class="light-band"><div class="wrap narrow-text">
<p>WCH offers comprehensive vacation rental management to optimize your property's income and guest experience. Utilizing proven marketing strategies, we attract the ideal renters and determine optimal nightly rates for maximized bookings and revenue. Our dedicated staff handles all guest communications, ensures fast maintenance response, and provides on-call support for a smooth vacation experience. WCH implements strict cleaning protocols between guests, conducts routine property inspections, and provides easy payouts of rental earnings. Partnering with WCH delivers true peace of mind, knowing your vacation rental is in expert hands.</p>
</div></section>
""" + CTA
write("copy-of-property-management/index.html", page("Vacation Rental | World Class Housing", vr_body))

# ---------------- ABOUT ----------------
about_body = hero("about-fireplace.jpg", "", "Experience<br><span class='gold'>the World Class Housing Difference</span>")
about_body += """
<section class="light-band">
  <div class="wrap split">
    <div>
      <p>With 20 years of experience as a leading property management company, our managed corporate housing system consistently delivers high satisfaction for both owners and tenants. We recognize the diverse investment property options available and value your home as a significant asset. By attentively listening to your needs and guiding you through the process, we ensure your investment is both straightforward and profitable. Our property management office operates Monday through Friday, staffed with dedicated professionals ready to answer your questions, handle maintenance requests, and maintain your property to the highest standards. We take care of the details so you don’t have to.</p>
    </div>
    <img class="split-img" src="/assets/about-house.jpg" alt="Suburban House">
  </div>
  <div class="wrap split" style="margin-top:3rem">
    <img class="split-img" src="/assets/about-handshake.jpg" alt="Handshake">
    <div>
      <p>Like our furnished property management program, WCH offers a full-service program for managing your property as an unfurnished rental in most of our local markets. We handle all aspects of the rental process, including finding and screening tenants, marketing your property, and negotiating with tenants to maintain high occupancy rates. Owners can expect a hands-off service, meaning we take care of everything!</p>
    </div>
  </div>
</section>
""" + CTA
write("about-4/index.html", page("About Us | World Class Housing", about_body))

# ---------------- PROPERTIES ----------------
gallery_imgs = [
 ("g1.jpg","Living Room"),("g2.jpg","Office Area"),("g3.jpg","Backyard"),
 ("g4.jpg","Kitchen 3"),("g5.jpg","Dining Area"),("g6.jpg","Guest Bathroom"),
 ("h1.jpg","20220727_072738"),("h2.jpg","20220723_082514"),("h3.jpg","Master Down Bed (1)"),
 ("h4.jpg","Dining Room"),("h5.jpg","Living Room"),("h6.jpg","Backyard"),
]
gal = "\n".join(f'<img src="/assets/{f}" alt="{a}">' for f,a in gallery_imgs)
prop_body = hero("prop-kitchen.jpg", "", "Convenient Housing Solutions")
prop_body += f"""
<section class="light-band">
  <div class="wrap">
    <p class="narrow">For business travelers, relocating employees, and project teams requiring temporary housing, World Class Housing (WCH) provides fully-furnished homes that deliver an exceptional living experience. With flexible lease terms for short or long-term stays, WCH offers the best local housing options to meet your team's needs, whether you're arranging accommodations for mobile employees or seeking housing yourself. Our area experts know the neighborhoods and can identify the right solutions to fit your requirements.</p>
    <div class="gallery">{gal}</div>
  </div>
</section>
""" + CTA
write("general-6/index.html", page("Properties | World Class Housing", prop_body))

# ---------------- CONTACT ----------------
contact_body = hero("contact-bg.jpg", "", "Contact Us")
contact_body += """
<section class="light-band">
  <div class="wrap center">
    <p><a href="mailto:support@worldclasshousing.net">support@worldclasshousing.net</a></p>
    <form class="contact-form light" id="contactForm" onsubmit="return sendMail(this)">
      <div class="form-row">
        <input name="firstname" placeholder="First Name" required>
        <input name="lastname" placeholder="Last Name" required>
      </div>
      <div class="form-row">
        <input name="code" placeholder="Code">
        <input name="phone" placeholder="Phone">
      </div>
      <input name="email" type="email" placeholder="Email" required>
      <textarea name="message" placeholder="Message" rows="6" required></textarea>
      <button class="btn btn-gold" type="submit">Send</button>
    </form>
  </div>
</section>
<script>
function sendMail(f){
  var body = "Name: " + f.firstname.value + " " + f.lastname.value + "\\nPhone: " + (f.code.value + " " + f.phone.value) + "\\nEmail: " + f.email.value + "\\n\\n" + f.message.value;
  window.location.href = "mailto:support@worldclasshousing.net?subject=" + encodeURIComponent("Website inquiry from " + f.firstname.value + " " + f.lastname.value) + "&body=" + encodeURIComponent(body);
  return false;
}
</script>
"""
write("contact/index.html", page("Contact Us | World Class Housing", contact_body))

# ---------------- LIST A PROPERTY (contact-8) ----------------
lap_body = hero("contact-bg.jpg", "", "List A Property")
lap_body += """
<section class="light-band">
  <div class="wrap center">
    <h2>Let's Chat</h2>
    <p>Have a property you would like to list with World Class Housing? Reach out with any questions and we will get back to you.</p>
    <p><strong>Phone</strong><br><a href="tel:678-661-1746">678-661-1746</a></p>
    <p><strong>Email</strong><br><a href="mailto:support@worldclasshousing.net">support@worldclasshousing.net</a></p>
    <form class="contact-form light" id="contactForm" onsubmit="return sendMail(this)">
      <div class="form-row">
        <input name="firstname" placeholder="First Name" required>
        <input name="lastname" placeholder="Last Name" required>
      </div>
      <textarea name="message" placeholder="Message" rows="6" required></textarea>
      <button class="btn btn-gold" type="submit">Send</button>
    </form>
  </div>
</section>
<script>
function sendMail(f){
  var body = "Name: " + f.firstname.value + " " + f.lastname.value + "\\n\\n" + f.message.value;
  window.location.href = "mailto:support@worldclasshousing.net?subject=" + encodeURIComponent("List A Property inquiry from " + f.firstname.value + " " + f.lastname.value) + "&body=" + encodeURIComponent(body);
  return false;
}
</script>
"""
write("contact-8/index.html", page("List A Property | World Class Housing", lap_body))

# ---------------- PROGRAMS ----------------
challenges_body = hero("hero-home.png", "", "Programs")
challenges_body += """
<section class="light-band">
  <div class="wrap">
    <div class="program-card">
      <img src="/assets/program.png" alt="Rental Arbitrage and Corporate Housing Mastery">
      <div>
        <h3>Rental Arbitrage and Corporate Housing Mastery</h3>
        <p class="price">$5,000.00</p>
        <a class="btn btn-gold" href="/challenge-page/731b76e7-7627-42b3-a57c-32275073d657">Join</a>
      </div>
    </div>
  </div>
</section>
"""
write("challenges/index.html", page("Program List | World Class Housing", challenges_body))

prog_body = hero("hero-home.png", "", "Rental Arbitrage and Corporate Housing Mastery")
prog_body += """
<section class="light-band">
  <div class="wrap narrow-text">
    <p class="muted">2 Steps</p>
    <h2>About</h2>
    <p>A dynamic course designed to unlock the secrets of the lucrative world of rental arbitrage and corporate housing. Tailored for both beginners and seasoned professionals, this 2-hour, expert-led course offers a deep dive into the essential strategies for building a successful rental business without the need for property ownership. From selecting the right properties and mastering tenant screening to optimizing revenue and excelling on platforms like Airbnb, each module is crafted to equip you with practical knowledge and skills. Engage in interactive quizzes, actionable insights, and real-world applications that prepare you to navigate the market confidently and elevate your rental business to new heights. Join us, and transform your approach to real estate investment, leveraging the expertise of World Class Assets to generate significant returns and achieve long-term success in the evolving rental landscape.</p>
    <h3>Instructors</h3>
    <p>Kirtis Gibbs</p>
    <h3>Price</h3>
    <p class="price">$5,000.00</p>
    <a class="btn btn-gold" href="/contact">Join</a>
  </div>
</section>
"""
write("challenge-page/731b76e7-7627-42b3-a57c-32275073d657/index.html",
      page("Rental Arbitrage and Corporate Housing Mastery | World Class Housing", prog_body))

# ---------------- BLOG ----------------
NAVJUNK = {"top of page","bottom of page","Use tab to navigate through the menu items.","FIND YOUR STAY",
"Services","Properties","About Us","Contact Us","Program List","More","All Posts","Search","Recent Posts","See All",
"1445 Woodmont Lane #3062","Atlanta, GA 30318","678-661-1746","support@worldclasshouing.net","Quick Links",
"Home","About","Compliance","Privacy Policy","Terms & Conditions","©2024 by World Class Housing. Proudly created by","The Artice"}

postmeta = {
 "boosting-apartment-leasing-success-in-atlanta-with-spotless-leasing-offices": ("blog-leasing.png","Jul 16","4 min read"),
 "elevate-resident-satisfaction-how-clean-outdoor-spaces-transform-atlanta-apartment-communities": ("blog-outdoor.png","Jul 17","4 min read"),
 "how-clean-elevators-and-stairwells-improve-atlanta-apartment-operations": ("blog-elevators.png","Sep 18","8 min read"),
 "how-professional-cleaning-enhances-resident-events-for-apartment-communities-in-atlanta": ("blog-events.png","Jul 15","4 min read"),
}

def post_body_lines(lines):
    # find body start: after "<n> min read"
    start = 0
    for i,l in enumerate(lines):
        if re.match(r'^\d+ min read$', l):
            start = i+1; break
    body = []
    for l in lines[start:]:
        if l in ("Recent Posts",):
            break
        if l in NAVJUNK:
            continue
        body.append(l)
    # merge continuation fragments
    merged = []
    for l in body:
        if merged and re.match(r'^[,.;:!?]', l):
            merged[-1] += l
        elif merged and len(l) < 45 and not re.search(r'[.!?:"”]$', l) and merged[-1] and not re.search(r'[.!?"”]$', merged[-1]):
            merged[-1] += " " + l
        else:
            merged.append(l)
    return merged

def render_post_html(lines):
    out = []
    i = 0
    while i < len(lines):
        l = lines[i]
        words = len(l.split())
        if words <= 9 and not re.search(r'[.!?,"”]$', l):
            # possible heading or list item; look at following lines
            j = i
            items = []
            while j < len(lines):
                lj = lines[j]
                wj = len(lj.split())
                if wj <= 9 and not re.search(r'[.!?,"”]$', lj):
                    items.append(lj); j += 1
                else:
                    break
            if len(items) >= 3:
                out.append("<ul>" + "".join(f"<li>{html.escape(x)}</li>" for x in items) + "</ul>")
                i = j
                continue
            elif len(items) == 1 and j < len(lines) and len(lines[j].split()) > 9:
                out.append(f"<h3>{html.escape(l)}</h3>")
                i += 1
                continue
        out.append(f"<p>{html.escape(l)}</p>")
        i += 1
    return "\n".join(out)

cards = []
for slug,(img,date,read) in postmeta.items():
    title = posts[slug]["text"][0]
    teaser = ""
    lines = post_body_lines(posts[slug]["text"])
    teaser = lines[0][:160] + "..." if lines else ""
    cards.append(f"""
    <a class="blog-card" href="/post/{slug}">
      <img src="/assets/{img}" alt="{html.escape(title)}">
      <div class="blog-card-body">
        <h3>{html.escape(title)}</h3>
        <p class="muted">Jerome Asiado &middot; {date} &middot; {read}</p>
        <p>{html.escape(teaser)}</p>
      </div>
    </a>""")

blog_body = hero("contact-bg.jpg", "", "Blog") + f"""
<section class="light-band">
  <div class="wrap">
    <h2 class="center">All Posts</h2>
    <div class="blog-grid">{''.join(cards)}</div>
  </div>
</section>
"""
write("blog/index.html", page("Blog | World Class Housing", blog_body))

for slug,(img,date,read) in postmeta.items():
    title = posts[slug]["text"][0]
    lines = post_body_lines(posts[slug]["text"])
    body_html = render_post_html(lines)
    pbody = f"""
<section class="light-band post">
  <div class="wrap narrow-text">
    <p><a href="/blog">&larr; All Posts</a></p>
    <h1 class="post-title">{html.escape(title)}</h1>
    <p class="muted">Jerome Asiado &middot; {date} &middot; {read}</p>
    <img class="post-hero" src="/assets/{img}" alt="{html.escape(title)}">
    {body_html}
  </div>
</section>
"""
    write(f"post/{slug}/index.html", page(f"{title} | World Class Housing", pbody))

# ---------------- TERMS ----------------
terms_lines = [l for l in d["terms-conditions"]["text"] if l not in NAVJUNK and l != "Terms & Conditions | World Class Housing"]
t_html = []
for l in terms_lines:
    w = len(l.split())
    if w <= 7 and not re.search(r'[.!?,]$', l) and not l.startswith("Last updated"):
        t_html.append(f"<h3>{html.escape(l)}</h3>")
    else:
        t_html.append(f"<p>{html.escape(l)}</p>")
terms_body = hero("contact-bg.jpg", "", "Terms &amp; Conditions") + f"""
<section class="light-band"><div class="wrap narrow-text legal">{''.join(t_html)}</div></section>
"""
write("terms-conditions/index.html", page("Terms & Conditions | World Class Housing", terms_body))
write("blank-1/index.html", page("Terms & Conditions | World Class Housing", terms_body))

# ---------------- PRIVACY ----------------
p_html = []
for l in privacy_lines:
    w = len(l.split())
    if w <= 7 and not re.search(r'[.!?,]$', l) and not l.startswith("Last updated"):
        p_html.append(f"<h3>{html.escape(l)}</h3>")
    else:
        p_html.append(f"<p>{html.escape(l)}</p>")
priv_body = hero("contact-bg.jpg", "", "Privacy Policy") + f"""
<section class="light-band"><div class="wrap narrow-text legal">{''.join(p_html)}</div></section>
"""
write("privacy-policy/index.html", page("Privacy Policy | World Class Housing", priv_body))

print("built pages:", sum(len(files) for _,_,files in os.walk(OUT)))
