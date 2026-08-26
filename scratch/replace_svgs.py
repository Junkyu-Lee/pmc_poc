import codecs
import re

with codecs.open(r'd:\workspaces\PMC_POC\output\poc_ppt.html', 'r', 'utf-8') as f:
    content = f.read()

# Replace Slide 4 SVG
slide4_old_svg_pattern = r'<!-- Multi-Agent Node SVG to replace the 7 colored td block -->(.*?)</svg>'
slide4_new_svg = """<!-- Multi-Agent Node SVG (Circular Layout) -->
<svg width="850" height="380" viewBox="0 0 850 380" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="forgeGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </radialGradient>
  </defs>

  <!-- Connectors -->
  <g stroke="#cbd5e1" stroke-width="2" stroke-dasharray="4,4">
    <path d="M 425 190 L 425 40" />
    <path d="M 425 190 L 541 96" />
    <path d="M 425 190 L 571 223" />
    <path d="M 425 190 L 490 325" />
    <path d="M 425 190 L 360 325" />
    <path d="M 425 190 L 279 223" />
    <path d="M 425 190 L 309 96" />
  </g>
  
  <!-- Central Engine -->
  <circle cx="425" cy="190" r="75" fill="url(#forgeGlow)" stroke="#38bdf8" stroke-width="3" />
  <text x="425" y="185" fill="#38bdf8" font-size="20" font-weight="bold" text-anchor="middle">Signal Forge</text>
  <text x="425" y="210" fill="#94a3b8" font-size="13" text-anchor="middle">가치 통합 의사결정</text>

  <!-- 7 Nodes -->
  <g transform="translate(425, 40)">
    <circle r="40" fill="#5458ce" />
    <text y="-5" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">거버넌스</text>
    <text y="15" fill="#e0e2ff" font-size="10" text-anchor="middle">Watchdog</text>
  </g>
  <g transform="translate(541, 96)">
    <circle r="40" fill="#14b8a6" />
    <text y="-5" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">범위</text>
    <text y="15" fill="#ccfbf1" font-size="10" text-anchor="middle">Guardian</text>
  </g>
  <g transform="translate(571, 223)">
    <circle r="40" fill="#f97316" />
    <text y="-5" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">일정</text>
    <text y="15" fill="#ffedd5" font-size="10" text-anchor="middle">Sentinel</text>
  </g>
  <g transform="translate(490, 325)">
    <circle r="40" fill="#f59e0b" />
    <text y="-5" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">리스크</text>
    <text y="15" fill="#fef3c7" font-size="10" text-anchor="middle">Oracle</text>
  </g>
  <g transform="translate(360, 325)">
    <circle r="40" fill="#ec4899" />
    <text y="-5" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">관계자</text>
    <text y="15" fill="#fce7f3" font-size="10" text-anchor="middle">Pulse</text>
  </g>
  <g transform="translate(279, 223)">
    <circle r="40" fill="#22c55e" />
    <text y="-5" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">자원</text>
    <text y="15" fill="#dcfce7" font-size="10" text-anchor="middle">Radar</text>
  </g>
  <g transform="translate(309, 96)">
    <circle r="40" fill="#8b5cf6" />
    <text y="-5" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">재무</text>
    <text y="15" fill="#ede9fe" font-size="10" text-anchor="middle">Protector</text>
  </g>
</svg>"""
content = re.sub(slide4_old_svg_pattern, slide4_new_svg, content, flags=re.DOTALL)


# Replace Slide 5 Mindset Table
slide5_old_table_pattern = r'<table class="mindset-table" style="background:#fff;">(.*?)</table>'
slide5_new_svg = """<div class="svg-container" style="background:#fff; border:none; padding:1.5rem; margin-top:2rem;">
<svg width="850" height="380" viewBox="0 0 850 380" xmlns="http://www.w3.org/2000/svg">
  <!-- Boxes (background outlines) -->
  <!-- Top Left (선제적) -->
  <text x="30" y="32" fill="#172b4d" font-size="22" font-weight="900">선제적</text>
  <rect x="25" y="45" width="280" height="125" rx="6" fill="#fff" stroke="#e8d5e1" stroke-width="2" />
  
  <rect x="35" y="60" width="260" height="36" rx="18" fill="#fdf2f8" />
  <circle cx="280" cy="78" r="9" fill="#d6489e" />
  <text x="50" y="83" fill="#172b4d" font-size="14" font-weight="bold">전체론적 관점 채택</text>
  
  <rect x="35" y="110" width="260" height="48" rx="18" fill="#fdf2f8" />
  <circle cx="280" cy="134" r="9" fill="#d6489e" />
  <text x="50" y="130" fill="#172b4d" font-size="14" font-weight="bold">프로세스 및 인도물에</text>
  <text x="50" y="148" fill="#172b4d" font-size="14" font-weight="bold">품질 내재화</text>

  <!-- Top Right (소유권) -->
  <text x="825" y="32" fill="#172b4d" font-size="22" font-weight="900" text-anchor="end">소유권</text>
  <rect x="545" y="45" width="280" height="125" rx="6" fill="#fff" stroke="#d5e8f5" stroke-width="2" />
  
  <rect x="555" y="60" width="260" height="36" rx="18" fill="#f0f9ff" />
  <circle cx="570" cy="78" r="9" fill="#3b95d6" />
  <text x="590" y="83" fill="#172b4d" font-size="14" font-weight="bold">책임감 있는 리더 되기</text>
  
  <rect x="555" y="110" width="260" height="48" rx="18" fill="#f0f9ff" />
  <circle cx="570" cy="134" r="9" fill="#3b95d6" />
  <text x="590" y="130" fill="#172b4d" font-size="14" font-weight="bold">자율성과 권한이 강화된</text>
  <text x="590" y="148" fill="#172b4d" font-size="14" font-weight="bold">문화 구축</text>

  <!-- Bottom (가치 중심) -->
  <text x="425" y="365" fill="#172b4d" font-size="22" font-weight="900" text-anchor="middle">가치 중심</text>
  <rect x="25" y="195" width="800" height="130" rx="6" fill="#fff" stroke="#c4b5fd" stroke-width="2" />
  
  <rect x="35" y="270" width="260" height="36" rx="18" fill="#f5f3ff" />
  <circle cx="280" cy="288" r="9" fill="#7c3aed" />
  <text x="50" y="293" fill="#172b4d" font-size="14" font-weight="bold">가치에 대한 집중</text>
  
  <rect x="555" y="270" width="260" height="36" rx="18" fill="#f5f3ff" />
  <circle cx="570" cy="288" r="9" fill="#7c3aed" />
  <text x="590" y="293" fill="#172b4d" font-size="14" font-weight="bold">모든 프로젝트 영역에 지속가능성 통합</text>
  
  <!-- Connectors -->
  <!-- Left Side -->
  <line x1="290" y1="78" x2="350" y2="78" stroke="#172b4d" stroke-width="1.5" />
  <line x1="350" y1="78" x2="350" y2="160" stroke="#172b4d" stroke-width="1.5" />
  <polygon points="289,78 296,74 296,82" fill="#172b4d" />
  
  <line x1="290" y1="134" x2="350" y2="134" stroke="#172b4d" stroke-width="1.5" />
  <polygon points="289,134 296,130 296,138" fill="#172b4d" />
  
  <line x1="350" y1="160" x2="370" y2="160" stroke="#172b4d" stroke-width="1.5" />
  
  <!-- Left Bottom -->
  <line x1="290" y1="288" x2="400" y2="288" stroke="#172b4d" stroke-width="1.5" />
  <line x1="400" y1="288" x2="400" y2="230" stroke="#172b4d" stroke-width="1.5" />
  <polygon points="289,288 296,284 296,292" fill="#172b4d" />
  
  <!-- Right Side -->
  <line x1="560" y1="78" x2="500" y2="78" stroke="#172b4d" stroke-width="1.5" />
  <line x1="500" y1="78" x2="500" y2="160" stroke="#172b4d" stroke-width="1.5" />
  <polygon points="561,78 554,74 554,82" fill="#172b4d" />
  
  <line x1="560" y1="134" x2="500" y2="134" stroke="#172b4d" stroke-width="1.5" />
  <polygon points="561,134 554,130 554,138" fill="#172b4d" />
  
  <line x1="500" y1="160" x2="480" y2="160" stroke="#172b4d" stroke-width="1.5" />
  
  <!-- Right Bottom -->
  <line x1="560" y1="288" x2="450" y2="288" stroke="#172b4d" stroke-width="1.5" />
  <line x1="450" y1="288" x2="450" y2="230" stroke="#172b4d" stroke-width="1.5" />
  <polygon points="561,288 554,284 554,292" fill="#172b4d" />

  <!-- Center circle -->
  <circle cx="425" cy="190" r="75" fill="#0f113a" />
  <text x="425" y="197" fill="#fff" font-size="24" font-weight="900" text-anchor="middle">마인드셋</text>

</svg>
</div>"""
content = re.sub(slide5_old_table_pattern, slide5_new_svg, content, flags=re.DOTALL)

with codecs.open(r'd:\workspaces\PMC_POC\output\poc_ppt.html', 'w', 'utf-8') as f:
    f.write(content)