import re

# Read v4 to get the SVG
with open(r'd:\workspaces\PMC_POC\output\NovaHome_stage1_stage2_analysis_v4.html', 'r', encoding='utf-8') as f:
    v4_text = f.read()

svg_match = re.search(r'(<svg viewbox=\"0 0 800 500\".*?</svg>)', v4_text, re.IGNORECASE | re.DOTALL)
if not svg_match:
    print('Could not find SVG in v4')
    exit(1)
svg_code = svg_match.group(1)

# Read v3
v3_path = r'd:\workspaces\PMC_POC\output\NovaHome_stage1_stage2_analysis_v3.html'
with open(v3_path, 'r', encoding='utf-8') as f:
    v3_text = f.read()

# Find the SECTION 10 block
start_tag = '<!-- SECTION 10: Causal Relationship Map -->'
end_tag = '</div>\n</div>'
idx = v3_text.find(start_tag)
if idx == -1:
    print('Could not find SECTION 10 in v3')
    exit(1)
end_idx = v3_text.find(end_tag, idx) + len(end_tag)

# Replace
new_block = f'''<!-- SECTION 10: Causal Relationship Map -->
<h2><span class="section-num">10.</span> Causal Relationship Map</h2>
<div class="card">
  <div class="svg-container" style="background: rgba(15, 23, 42, 0.4); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
    {svg_code}
  </div>
  <div class="annotation warn" style="margin-top:1rem;">
    <strong>진단:</strong> #1 거버넌스 붕괴가 Root of Roots로서 연쇄적인 파급 효과를 발생시킴
  </div>
</div>'''

v3_new_text = v3_text[:idx] + new_block + v3_text[end_idx:]

with open(v3_path, 'w', encoding='utf-8') as f:
    f.write(v3_new_text)
print('Successfully replaced text causal map with SVG in v3.html')
