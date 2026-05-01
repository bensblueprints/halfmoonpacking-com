import os
import re
import glob

TEMPLATE = '''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" href="{img_prefix}images/06ae721a_981216548.png" type="image/png">
<link rel="stylesheet" href="{css_path}">
</head>
<body>
<div class="bg-texture"></div>

<header class="site-header">
  <div class="header-inner">
    <div class="site-logo">
      <a href="{root_prefix}index.html"><img src="{img_prefix}images/c301fa09_logo.png" alt="Halfmoon Packing & Outfitting"></a>
    </div>
    <div class="phone-tag"><span>For Booking: (719) 486-4570</span></div>
    <button class="nav-toggle" aria-label="Toggle navigation">&#9776;</button>
  </div>
</header>

<nav class="main-nav">
  <div class="nav-inner">
    <ul class="nav-list">
      <li><a href="{root_prefix}index.html">Home</a></li>
      <li class="has-dropdown"><a href="{root_prefix}stagecoach.html">Stagecoach</a><ul class="dropdown depth-0">
        <li><a href="{root_prefix}rides/wagon-rides.html">Wagon Rides</a></li>
      </ul></li>
      <li class="has-dropdown"><a href="{root_prefix}rides.html">Riding</a><ul class="dropdown depth-0">
        <li><a href="{root_prefix}rides/full-day-horseback-rides.html">Full Day Horseback Rides</a></li>
        <li><a href="{root_prefix}rides/hourly-to-half-day.html">Hourly To Half Day</a></li>
        <li><a href="{root_prefix}rides/cavecreek-horseback-rides.html">Winter Horseback Rides</a></li>
      </ul></li>
      <li class="has-dropdown"><a href="{root_prefix}camping.html">Camping</a><ul class="dropdown depth-0">
        <li><a href="{root_prefix}camping/guided-horse-camping.html">Guided Horse Camping</a></li>
        <li><a href="{root_prefix}camping/horse-camping.html">Horse Camping</a></li>
        <li><a href="{root_prefix}camping/pack-service-summer.html">Pack Service</a></li>
        <li><a href="{root_prefix}camping/summer-drop-camps.html">Summer Drop Camps</a></li>
      </ul></li>
      <li class="has-dropdown"><a href="{root_prefix}hunting.html">Hunting</a><ul class="dropdown depth-0">
        <li><a href="{root_prefix}hunting/colorado-hunting-units.html">Colorado Hunting Units</a></li>
        <li><a href="{root_prefix}hunting/hunting-services.html">Hunting Services</a></li>
        <li class="has-dropdown has-submenu"><a href="{root_prefix}hunting/game.html">Game</a><ul class="dropdown depth-1">
          <li><a href="{root_prefix}hunting/game/antelope-hunt.html">Antelope Hunt</a></li>
          <li><a href="{root_prefix}hunting/game/bear-hunt-2.html">Bear Hunt</a></li>
          <li><a href="{root_prefix}hunting/game/elk-hunt-2.html">Elk Hunt</a></li>
          <li><a href="{root_prefix}hunting/game/moose-hunt-2.html">Moose Hunt</a></li>
          <li><a href="{root_prefix}hunting/game/mountain-lion-hunts.html">Mountain Lion Hunts</a></li>
          <li><a href="{root_prefix}hunting/game/mule-deer-hunt.html">Mule Deer Hunt</a></li>
        </ul></li>
      </ul></li>
      <li class="has-dropdown"><a href="{root_prefix}fishing.html">Fishing</a><ul class="dropdown depth-0">
        <li><a href="{root_prefix}fishing/alpine-lakes.html">Alpine Lakes</a></li>
        <li><a href="{root_prefix}fishing/eagle-river.html">Eagle River</a></li>
        <li><a href="{root_prefix}fishing/lake-fishing.html">Lake Fishing</a></li>
      </ul></li>
      <li><a href="{root_prefix}training-center.html">Training Center</a></li>
      <li class="has-dropdown"><a href="{root_prefix}gallery.html">Gallery</a><ul class="dropdown depth-0">
        <li><a href="{root_prefix}gallery/fishing-photos.html">Fishing Photos</a></li>
        <li><a href="{root_prefix}gallery/hunting-photos.html">Hunting Photos</a></li>
        <li><a href="{root_prefix}gallery/horseback-riding-photos.html">Horseback Riding Photos</a></li>
        <li><a href="{root_prefix}gallery/summer-camp-photos.html">Summer Camp Photos</a></li>
        <li><a href="{root_prefix}gallery/videos.html">Videos</a></li>
      </ul></li>
      <li class="has-dropdown"><a href="{root_prefix}about.html">About</a><ul class="dropdown depth-0">
        <li><a href="{root_prefix}about/tom-burch.html">Tom Burch</a></li>
        <li><a href="{root_prefix}about/anita-percifield.html">Anita Percifield</a></li>
        <li><a href="{root_prefix}about/ben-roehrs.html">Ben Roehrs</a></li>
        <li><a href="{root_prefix}about/charlie-howard.html">Charlie Howard</a></li>
        <li><a href="{root_prefix}about/jake-skobel.html">Jake Skobel</a></li>
        <li><a href="{root_prefix}about/keiley-smith.html">Keiley Smith</a></li>
        <li><a href="{root_prefix}about/luke-talley.html">Luke Talley</a></li>
      </ul></li>
      <li class="has-dropdown"><a href="#">Booking</a><ul class="dropdown depth-0">
        <li><a href="{root_prefix}user-registration.html">Employee</a></li>
        <li><a href="{root_prefix}reservations.html">Reservation</a></li>
        <li><a href="{root_prefix}pay-at-checkin.html">Pay at checkin</a></li>
      </ul></li>
      <li><a href="{root_prefix}contact.html">Contact</a></li>
    </ul>
  </div>
</nav>

<div class="page-header-banner" style="background-image:url('{banner_image}');">
  <div class="header-overlay"></div>
  <div class="header-content">
    <h1 class="page-title">{banner_title}</h1>
  </div>
  <div class="scroll-indicator">Scroll</div>
</div>

<main class="main-content">
  <div class="content-card">
    <div>
{content}
    </div>
  </div>
</main>

<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <img src="{img_prefix}images/c301fa09_logo.png" alt="Halfmoon Packing & Outfitting">
      <p>Colorado's premier outfitter for horseback riding, camping, hunting, and fishing adventures in the Rocky Mountains.</p>
      <div class="footer-social">
        <a href="https://www.facebook.com/halfmoonpacking" target="_blank" aria-label="Facebook">FB</a>
        <a href="https://www.instagram.com/halfmoonpacking/" target="_blank" aria-label="Instagram">IG</a>
      </div>
    </div>
    <div class="footer-col">
      <h4>Adventures</h4>
      <a href="{root_prefix}rides.html">Horseback Riding</a>
      <a href="{root_prefix}camping.html">Camping</a>
      <a href="{root_prefix}hunting.html">Hunting</a>
      <a href="{root_prefix}fishing.html">Fishing</a>
      <a href="{root_prefix}stagecoach.html">Stagecoach</a>
    </div>
    <div class="footer-col">
      <h4>Company</h4>
      <a href="{root_prefix}about.html">About Us</a>
      <a href="{root_prefix}gallery.html">Gallery</a>
      <a href="{root_prefix}training-center.html">Training Center</a>
      <a href="{root_prefix}contact.html">Contact</a>
      <a href="{root_prefix}reservations.html">Book Now</a>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; Halfmoon Packing & Outfitting, LLC. All rights reserved.</p>
    <p>1100 East Tennessee Rd, Leadville, CO 80461 | <a href="tel:7194864570">(719) 486-4570</a></p>
  </div>
</footer>

<script src="{js_path}"></script>
</body>
</html>
'''

def extract_from_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    title = title_match.group(1).strip() if title_match else 'Halfmoon Packing & Outfitting'
    banner_match = re.search(r"background-image:url\(['\"](.*?)['\"]\)", html)
    banner_image = banner_match.group(1) if banner_match else 'images/55dfeea6_halfmoonbanner11.png'
    banner_title_match = re.search(r'<h1 class="page-title">(.*?)</h1>', html, re.DOTALL)
    banner_title = re.sub(r'<.*?>', '', banner_title_match.group(1)).strip() if banner_title_match else 'Halfmoon Packing & Outfitting'
    content_match = re.search(r'<main class="main-content">\s*<div class="content-card">\s*<div>(.*?)\s*</div>\s*</div>\s*</main>', html, re.DOTALL)
    if content_match:
        content = content_match.group(1).strip()
    else:
        content_match = re.search(r'<div class="content-card">\s*<div>(.*?)\s*</div>\s*</div>', html, re.DOTALL)
        content = content_match.group(1).strip() if content_match else '<section><h1>Content Coming Soon</h1></section>'
    return {'title': title, 'banner_image': banner_image, 'banner_title': banner_title, 'content': content}

def get_prefixes(filepath, base_dir):
    rel = os.path.relpath(filepath, base_dir)
    depth = rel.count(os.sep)
    if depth == 0:
        return '', ''
    prefix = '../' * depth
    return prefix, prefix

def rebuild_page(filepath, base_dir, data):
    img_prefix, root_prefix = get_prefixes(filepath, base_dir)
    css_path = img_prefix + 'style.css'
    js_path = img_prefix + 'script.js'
    new_html = TEMPLATE.format(
        title=data['title'], banner_image=data['banner_image'], banner_title=data['banner_title'],
        content=data['content'], css_path=css_path, js_path=js_path, img_prefix=img_prefix, root_prefix=root_prefix
    )
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_files = [f for f in glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True) if not os.path.basename(f).startswith('_')]
    for filepath in sorted(html_files):
        data = extract_from_html(filepath)
        rebuild_page(filepath, base_dir, data)
    print(f'Rebuilt {len(html_files)} files with fixed image paths.')

if __name__ == '__main__':
    main()
