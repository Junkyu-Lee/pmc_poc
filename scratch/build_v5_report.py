import sys
import os
import base64

sys.stdout.reconfigure(encoding='utf-8')

def generate_svg_image(title, subtitle, icon, bg_color1, bg_color2):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_color1}"/>
      <stop offset="100%" stop-color="{bg_color2}"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="15" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="600" height="600" rx="30" fill="url(#bg)"/>
  <circle cx="300" cy="240" r="120" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="8"/>
  <circle cx="300" cy="240" r="80" fill="rgba(255,255,255,0.05)"/>
  <text x="300" y="270" font-family="'Segoe UI', sans-serif" font-size="90" text-anchor="middle" fill="#ffffff" filter="url(#glow)">{icon}</text>
  <text x="300" y="420" font-family="'Inter', sans-serif" font-size="26" font-weight="bold" text-anchor="middle" fill="#ffffff">{title}</text>
  <text x="300" y="465" font-family="'Inter', sans-serif" font-size="18" text-anchor="middle" fill="rgba(255,255,255,0.7)">{subtitle}</text>
</svg>"""
    b64 = base64.b64encode(svg.encode('utf-8')).decode('utf-8')
    return f"data:image/svg+xml;base64,{b64}"

img1 = generate_svg_image("Vendor Governance Failure", "NovaChip SDK Delay & License Escalation", "🤝", "#1e1b4b", "#4338ca")
img2 = generate_svg_image("Uncontrolled Scope Creep", "REQ-045 AI Voice & Baseline Erosion", "📋", "#312e81", "#6366f1")

causal_map_svg = """
<div class="svg-container" style="background: rgba(15, 23, 42, 0.4); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
<svg viewbox="0 0 800 500" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="arrow" markerheight="6" markerwidth="6" orient="auto-start-reverse" refx="9" refy="5" viewbox="0 0 10 10">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#8a8780"></path>
</marker>
</defs>
<path d="M 300 75 Q 150 75 150 190" fill="none" marker-end="url(#arrow)" stroke="#8a8780" stroke-dasharray="5,5" stroke-width="2"></path>
<text fill="#a8a5a0" font-size="12" font-weight="500" x="180" y="110">Vendor SLA Absence</text>
<path d="M 500 75 Q 650 75 650 190" fill="none" marker-end="url(#arrow)" stroke="#8a8780" stroke-dasharray="5,5" stroke-width="2"></path>
<text fill="#a8a5a0" font-size="12" font-weight="500" x="600" y="110">Scope Creep (REQ-045)</text>
<path d="M 550 225 L 260 225" fill="none" marker-end="url(#arrow)" stroke="#dc3545" stroke-width="2.5"></path>
<text fill="#f87171" font-size="12" font-weight="700" text-anchor="middle" x="400" y="215">Quality Crisis (Cold Boot 3.5s)</text>
<rect fill="#1e293b" height="50" rx="6" stroke="#475569" width="200" x="200" y="50"></rect>
<text fill="#e2e8f0" font-size="14" font-weight="700" text-anchor="middle" x="300" y="80">1. Governance Collapse</text>
<rect fill="#1e293b" height="50" rx="6" stroke="#475569" width="180" x="60" y="190"></rect>
<text fill="#e2e8f0" font-size="14" font-weight="700" text-anchor="middle" x="150" y="220">2. Tech Debt Accumulation</text>
<rect fill="#1e293b" height="50" rx="6" stroke="#475569" width="180" x="550" y="190"></rect>
<text fill="#e2e8f0" font-size="14" font-weight="700" text-anchor="middle" x="640" y="220">3. Organization Silo</text>
<rect fill="#dc3545" height="50" rx="6" stroke="#f87171" stroke-width="2" width="220" x="290" y="320"></rect>
<text fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle" x="400" y="350">4. ASIL-B / SOP Failure (G4/G5)</text>
</svg>
</div>
"""

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>NextGen AutoCockpit PM Competition — Agentic Presentation (v4)</title>
<style>
  :root {{
    --bg: #0f172a;
    --surface: #1e293b;
    --surface-alt: #334155;
    --primary: #38bdf8;
    --primary-dark: #0284c7;
    --accent: #a855f7;
    --accent-light: #c084fc;
    --red: #f43f5e;
    --red-light: #fda4af;
    --orange: #f97316;
    --yellow: #eab308;
    --green: #22c55e;
    --text: #f8fafc;
    --text-muted: #94a3b8;
    --border: #475569;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background-color: var(--bg);
    color: var(--text);
    line-height: 1.6;
    padding: 2rem;
  }}
  .container {{ max-width: 1400px; margin: 0 auto; }}
  
  header {{
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311b92 100%);
    padding: 2.5rem;
    border-radius: 16px;
    border: 1px solid rgba(168, 85, 247, 0.4);
    margin-bottom: 2.5rem;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
  }}
  header h1 {{ font-size: 2.2rem; font-weight: 800; color: #fff; margin-bottom: 0.5rem; }}
  header .subtitle {{ font-size: 1.1rem; color: var(--primary); font-weight: 600; }}
  
  .slide-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3);
    min-height: 75vh;
    display: flex;
    flex-direction: column;
  }}
  .slide-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid var(--surface-alt);
    padding-bottom: 1rem;
    margin-bottom: 1.5rem;
  }}
  .slide-title {{ font-size: 1.4rem; font-weight: 700; color: var(--primary); display: flex; align-items: center; gap: 0.6rem; }}
  .slide-num {{ background: var(--surface-alt); color: var(--text-muted); padding: 0.2rem 0.6rem; border-radius: 6px; font-size: 0.85rem; font-weight: 700; }}
  
  .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }}
  .grid-3 {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.5rem; }}
  .grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; }}
  
  table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.92rem; }}
  th, td {{ padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid var(--border); }}
  th {{ background: var(--surface-alt); color: var(--primary); font-weight: 700; }}
  
  .card {{ background: rgba(15, 23, 42, 0.6); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border); overflow-x: auto; flex: 1; }}
  .card-title {{ font-size: 1.15rem; font-weight: 700; color: var(--accent-light); margin-bottom: 1rem; }}
  .highlight-red {{ color: var(--red); font-weight: 700; }}
  
  .agent-tag {{
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    background: rgba(168, 85, 247, 0.2);
    color: var(--accent-light);
    border: 1px solid var(--accent);
    margin-bottom: 1rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .agent-tag::before {{ content: '🤖 '; }}
  
  .red-zone {{ border: 2px solid var(--red); box-shadow: 0 0 15px rgba(244,63,94,0.3); }}
  .red-zone-title {{ color: var(--red); }}
</style>
</head>
<body>

<div class="container">
  <header>
    <h1>🚗 NextGen AutoCockpit: Agentic Stage ① & ② Presentation</h1>
    <div class="subtitle">Storytelling Flow: The Crisis ➔ The Insight ➔ The Deep-Dive</div>
  </header>

  <!-- STAGE 1: HOOK (The Crisis) -->
  <div class="slide-card red-zone">
    <div class="slide-header">
      <h2 class="slide-title red-zone-title">🚨 SLIDE 01 [Hook]: The Crisis - G3 실차 테스트 붕괴 직전</h2>
      <span class="slide-num">SLIDE 01</span>
    </div>
    <div class="grid-2">
      <div class="card">
        <div class="card-title">📉 KPI Target vs Actual</div>
        <table>
          <thead><tr><th>Metric</th><th>Target</th><th>Actual (Oct 5)</th></tr></thead>
          <tbody>
            <tr><td>Cold Boot Time</td><td>2.0s</td><td><span class="highlight-red">3.5s (Critical)</span></td></tr>
            <tr><td>CI Test Pass Rate</td><td>95%</td><td><span class="highlight-red">58% (300 broken)</span></td></tr>
            <tr><td>NovaChip SDK</td><td>Sep 30</td><td><span class="highlight-red">Delayed 3 Weeks</span></td></tr>
          </tbody>
        </table>
      </div>
      <div class="card">
        <div class="card-title">🗣️ Voices of Crisis (Stakeholders)</div>
        <ul style="padding-left:1.5rem; line-height:1.8;">
          <li><b>박태산 전무 (Sponsor):</b> "내일 아침 8시까지 리스크 복구 계획서 올려놔!!"</li>
          <li><b>블라인드 (Team):</b> "진짜 침몰하는 타이타닉 같네요. 탈출이 지능순."</li>
          <li><b>문해인 (QA):</b> "어제 밤새 돌린 CI 자동화 300개가 다 깨졌습니다."</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- STAGE 1: INSIGHT (The Root Cause) -->
  <div class="slide-card">
    <div class="slide-header">
      <h2 class="slide-title">💡 SLIDE 02 [Insight]: 현상은 5개, 하지만 진범(Root of Roots)은 1개입니다.</h2>
      <span class="slide-num">SLIDE 02</span>
    </div>
    <div class="agent-tag">Generated by Root Cause Advisor Agent</div>
    {causal_map_svg}
    <p style="margin-top:1rem; font-size:1.1rem;"><b>분석:</b> 부팅 지연, CI 파손, SDK 지연은 모두 '결과'입니다. 이 모든 위기는 <b>① 벤더 통제 부재</b>와 <b>② 무검토 Scope Creep(REQ-045) 수용</b>이라는 단 2개의 '거버넌스 붕괴'에서 촉발되었습니다. 이에 Top 2 Root Cause에 딥다이브합니다.</p>
  </div>

  <!-- STAGE 2: DEEP DIVE (Root 1) -->
  <div class="slide-card">
    <div class="slide-header">
      <h2 class="slide-title">🔍 SLIDE 03 [Deep-dive 1]: 벤더 통제 실패 및 스폰서 에스컬레이션 부재</h2>
      <span class="slide-num">SLIDE 03</span>
    </div>
    <div class="agent-tag">Root Cause Advisor / Comm Orchestrator Agent</div>
    <div class="grid-2">
      <div><img src="{img1}" alt="Vendor" style="width: 100%; border-radius: 12px;"/></div>
      <div class="card">
        <div class="card-title">🧠 4-Step Analysis Framework</div>
        <ul>
          <li><b>Mindset:</b> 벤더 계약 시 SLA 페널티 미설정 및 PM의 리스크 은폐 (Reactive).</li>
          <li><b>Domain:</b> Stakeholder & Supplier Domain 붕괴.</li>
          <li><b>AI Use Case:</b> 스마트 컨트랙트 감지 Agent를 통한 SLA 모니터링 자동화.</li>
          <li><b>Future State:</b> 이슈 지연 1주일 내 스폰서 자동 에스컬레이션 체계 (Proactive).</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- STAGE 2: DEEP DIVE (Root 2) -->
  <div class="slide-card">
    <div class="slide-header">
      <h2 class="slide-title">🔍 SLIDE 04 [Deep-dive 2]: 무검토 Scope Creep (REQ-045)</h2>
      <span class="slide-num">SLIDE 04</span>
    </div>
    <div class="agent-tag">Plan Optimizer / Change Guardian Agent</div>
    <div class="grid-2">
      <div><img src="{img2}" alt="Scope Creep" style="width: 100%; border-radius: 12px;"/></div>
      <div class="card">
        <div class="card-title">🧠 4-Step Analysis Framework</div>
        <ul>
          <li><b>Mindset:</b> 고객사 Top-down 요구에 대한 무조건적 수용 (Value & Safety 위협).</li>
          <li><b>Domain:</b> Scope & Planning Domain 붕괴.</li>
          <li><b>AI Use Case:</b> Change Guardian Agent를 통한 변경 요구사항 정량 Impact 평가.</li>
          <li><b>Future State:</b> Data-driven CCB 회의체 운영 및 기술부채 방어.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- STAGE 3: BRIDGE -->
  <div class="slide-card">
    <div class="slide-header">
      <h2 class="slide-title">🚀 SLIDE 05 [Bridge to Stage 3]: Agentic Workflow 도입</h2>
      <span class="slide-num">SLIDE 05</span>
    </div>
    <div class="card">
      <div class="card-title">임시방편(Reactive)에서 예측/방어형(Proactive)으로의 전환</div>
      <p>단순한 도구 도입이 아닙니다. PM을 보조하는 <b>Cognitive PM-Twin (Synapse)</b>가 벤더 리스크 감지, 일정 딜레이 예측, CCB 영향도를 사전 분석하여 인간 PM이 '결정'에만 집중하도록 하는 <b>Value-Driven Agentic System</b>을 Stage 3에서 설계합니다.</p>
    </div>
  </div>

</div>
</body>
</html>
"""

os.makedirs(r'd:\workspaces\PMC_POC\output', exist_ok=True)
with open(r'd:\workspaces\PMC_POC\output\NextGen_AutoCockpit_stage1_stage2_analysis_v4.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated NextGen_AutoCockpit_stage1_stage2_analysis_v4.html successfully with Agentic Presentation flow.")
