import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace CSS variables to make the theme match the logo
html = html.replace("--accent:   #1C2B3C;", "--accent:   #1F1F1F;")
html = html.replace("--accent-h: #2C3E52;", "--accent-h: #000000;")
html = html.replace("--dark:     #0D0C0A;", "--dark:     #050505;")

# Replace Nav logo SVG with the new logo image
nav_logo_pattern = r'<svg xmlns="http://www.w3.org/2000/svg" width="175" height="24" viewBox="0 0 175 24" aria-label="Ediz &amp; Co." style="display:block">\s*<text x="0" y="19" style="[^"]*">EDIZ &amp; CO.</text>\s*</svg>'
nav_logo_img = '<img src="logo_new.png" alt="Ediz &amp; Co." style="height: 32px; width: auto; filter: invert(1); mix-blend-mode: screen;">'
html = re.sub(nav_logo_pattern, nav_logo_img, html, flags=re.IGNORECASE)

# Replace Footer logo SVG with the new logo image
footer_logo_pattern = r'<svg xmlns="http://www.w3.org/2000/svg" width="160" height="20" viewBox="0 0 160 20" aria-label="Ediz &amp; Co." style="display:block">\s*<text x="0" y="17" style="[^"]*">EDIZ &amp; CO.</text>\s*</svg>'
footer_logo_img = '<img src="logo_new.png" alt="Ediz &amp; Co." style="height: 28px; width: auto; filter: invert(1); mix-blend-mode: screen;">'
html = re.sub(footer_logo_pattern, footer_logo_img, html, flags=re.IGNORECASE)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Website updated successfully!")
