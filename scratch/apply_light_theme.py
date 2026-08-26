import bs4
import re
import os

v4_path = r'd:\workspaces\PMC_POC\output\NextGen_AutoCockpit_stage1_stage2_analysis_v4.html'

with open(v4_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. Update CSS Variables using regex for precision without touching the rest of the style tag
new_root = """:root {
    --bg: #f8fafc;
    --surface: #ffffff;
    --surface-alt: #f1f5f9;
    --primary: #0284c7;
    --primary-dark: #0369a1;
    --accent: #8b5cf6;
    --accent-light: #a78bfa;
    --red: #e11d48;
    --red-light: #f43f5e;
    --orange: #ea580c;
    --yellow: #ca8a04;
    --green: #16a34a;
    --text: #1e293b;
    --text-muted: #64748b;
    --border: #e2e8f0;
  }"""
html_content = re.sub(r':root\s*\{[^}]+\}', new_root, html_content)

# Update body background to have a faint dot pattern for an elegant look
body_css = r"""body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background-color: var(--bg);
    background-image: radial-gradient(#cbd5e1 1px, transparent 1px);
    background-size: 20px 20px;
    color: var(--text);
    line-height: 1.6;
    padding: 2rem;
  }"""
html_content = re.sub(r'body\s*\{[^}]+\}', body_css, html_content)

# Parse with BeautifulSoup
soup = bs4.BeautifulSoup(html_content, 'html.parser')

# Update Cover Slide
cover = soup.find('div', class_='cover-slide')
if cover:
    # Change cover background to a bright elegant gradient
    cover['style'] = cover['style'].replace(
        'background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311b92 100%)',
        'background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 50%, #e0f2fe 100%)'
    )
    # Make text dark on the cover
    h1 = cover.find('h1')
    if h1:
        h1['style'] = h1['style'].replace('color: #fff;', 'color: #0f172a;')

# Update .card classes which might have dark rgba hardcoded
for card in soup.find_all('div', class_='card'):
    # Usually in the CSS or inline. Wait, in V4 the classic version, .card is defined in CSS:
    pass

# We should also update CSS `.card` definition
for style_tag in soup.find_all('style'):
    css_text = style_tag.string
    if css_text:
        # Replace dark card background
        css_text = css_text.replace('background: rgba(15, 23, 42, 0.6);', 'background: #ffffff;')
        css_text = css_text.replace('background: rgba(15, 23, 42, 0.4);', 'background: #ffffff;')
        # Box shadow for light theme cards
        css_text = css_text.replace('box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3);', 'box-shadow: 0 10px 20px rgba(0,0,0,0.05);')
        style_tag.string = css_text

# Update any inline dark backgrounds
for div in soup.find_all(style=True):
    style_str = div['style']
    if 'rgba(15, 23, 42, 0.6)' in style_str:
        div['style'] = style_str.replace('rgba(15, 23, 42, 0.6)', '#ffffff')
    if 'rgba(15, 23, 42, 0.4)' in style_str:
        div['style'] = style_str.replace('rgba(15, 23, 42, 0.4)', '#f8fafc')
    # Update text colors in tables if they are too light
    if 'color: #e2e8f0' in style_str:
        div['style'] = style_str.replace('color: #e2e8f0', 'color: #1e293b')
    if 'color: #ffffff' in style_str:
        div['style'] = style_str.replace('color: #ffffff', 'color: #0f172a')
        
# Add pictograms to card titles that don't have emojis yet
# Define some fallback emojis based on text
emoji_map = {
    '원인': '🔍',
    '결과': '🎯',
    '전략': '♟️',
    '해결': '🛠️',
    '목표': '🚩',
    '위험': '⚠️',
    '도구': '🧰',
    '진단': '🩺',
    '현상': '👁️',
    '요약': '📑',
    '분석': '📊',
    'Mindset': '🧠',
    'Domain': '🏛️',
    'AI': '🤖',
    'Metric': '📐',
    '통제': '🔒',
    '에스컬레이션': '📈'
}

for title in soup.find_all(class_='card-title'):
    text = title.get_text()
    # Check if text already has an emoji by checking character ranges or just simple string check
    # Emojis are usually above \u2600.
    has_emoji = any(ord(c) > 0x2500 for c in text)
    if not has_emoji:
        for key, emoji in emoji_map.items():
            if key in text:
                title.string = f"{emoji} {text}"
                break
        else:
            # Default pictogram
            title.string = f"📌 {text}"

# Let's also wrap the card titles with a nicer styled container
for title in soup.find_all(class_='card-title'):
    # Ensure they have nice margins in light theme
    title['style'] = title.get('style', '') + " border-bottom: 2px solid var(--surface-alt); padding-bottom: 0.5rem;"

# Inject an elegant AI-themed watermark or decoration if desired (we won't add large images to avoid clutter, but faint CSS decorations are fine)

with open(v4_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully applied light beige/white theme and added pictograms.")
