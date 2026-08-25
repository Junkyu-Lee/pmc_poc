import os

html_content = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>PM Transformers — VALUE-DRIVEN AI AGENT</title>
<style>
  :root {
    --bg: #f8f9fa;
    --surface: #ffffff;
    --surface-alt: #f1f5f9;
    --primary: #0284c7;
    --primary-dark: #0369a1;
    --accent: #7e22ce;
    --accent-light: #9333ea;
    --red: #e11d48;
    --orange: #ea580c;
    --yellow: #ca8a04;
    --green: #16a34a;
    --text: #1e293b;
    --text-muted: #64748b;
    --border: #cbd5e1;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background-color: var(--bg);
    color: var(--text);
    line-height: 1.6;
    padding: 2rem;
  }
  .container { max-width: 1400px; margin: 0 auto; }
  
  header {
    background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 50%, #e2e8f0 100%);
    padding: 2.5rem;
    border-radius: 16px;
    border: 1px solid rgba(147, 51, 234, 0.3);
    margin-bottom: 2.5rem;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
  }
  header h1 { font-size: 2.2rem; font-weight: 800; color: var(--text); margin-bottom: 0.5rem; }
  header .subtitle { font-size: 1.1rem; color: var(--primary); font-weight: 600; }
  
  .slide-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
    min-height: 60vh;
    display: flex;
    flex-direction: column;
  }
  .slide-card:hover { border-color: var(--primary); }
  .slide-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid var(--border);
    padding-bottom: 1rem;
    margin-bottom: 1.5rem;
  }
  .slide-title { font-size: 1.4rem; font-weight: 700; color: var(--primary); }
  .slide-num { background: var(--surface-alt); color: var(--text-muted); padding: 0.2rem 0.6rem; border-radius: 6px; font-size: 0.85rem; font-weight: 700; }
  
  .slide-summary {
    font-size: 1.05rem; font-weight: 700; color: var(--text);
    background: rgba(2, 132, 199, 0.05); padding: 1rem 1.2rem; border-radius: 8px; margin-bottom: 1.5rem; border-left: 4px solid var(--primary);
  }

  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
  .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.5rem; }
  
  .card { background: rgba(248, 249, 250, 0.8); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border); flex: 1; }
  .card-title { font-size: 1.15rem; font-weight: 700; color: var(--accent); margin-bottom: 1rem; }
  ul { margin-left: 1.5rem; }
  li { margin-bottom: 0.5rem; }

  table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem; }
  th, td { padding: 1rem; text-align: left; border-bottom: 1px solid var(--border); }
  th { background: var(--surface-alt); color: var(--primary); font-weight: 700; }
  
  .svg-container { overflow-x: auto; margin: 1rem 0; background: #fafafa; border-radius: 8px; padding: 2.5rem; text-align: center; border: 1px dashed var(--border);}
  .svg-container svg { max-width: 100%; height: auto; display: inline-block;}
</style>
</head>
<body>
<div class="container">
<header>
<h1>VALUE-DRIVEN AI AGENT: PM Transformers</h1>
<div class="subtitle">PM의 인지를 확장하는 7개 도메인의 디지털 트윈 — 통합적 의사결정과 능동적 문제해결</div>
</header>

<!-- SLIDE 1 -->
<div class="slide-card">
<div class="slide-header">
<h2 class="slide-title">▪ 문제 정의 및 해결 방향 : 흩어진 신호, 따로 노는 판단</h2>
<span class="slide-num">SLIDE 01</span>
</div>
<div class="grid-2">
<div class="card">
    <div class="card-title" style="color: var(--red);">문제 (Symptom & Root Cause)</div>
    <ul>
        <li>이상징후가 <strong>흩어져 늦게 발견</strong>되어 초기 대응 실패</li>
        <li>도메인별(일정, 리스크 등)로 사일로화되어 <strong>따로 판단</strong></li>
        <li>PM 1인의 <strong>인지 대역폭 한계</strong>로 가치 기준 없는 독단 및 판단 지연 발생</li>
    </ul>
</div>
<div class="card" style="background: rgba(2, 132, 199, 0.05); border-color: var(--primary);">
    <div class="card-title" style="color: var(--primary);">해결 방향 (Solution)</div>
    <ul>
        <li>7개 도메인을 <strong>상시·동시 관측</strong>하는 멀티 에이전트 구축</li>
        <li>분산된 신호와 상충 사항을 <strong>프로젝트 가치(North Star) 기준</strong>으로 중재</li>
        <li>최종 결정 주체인 PM의 <strong>인지와 판단 능력을 전방위적으로 지원 및 확장</strong></li>
    </ul>
</div>
</div>
</div>

<!-- SLIDE 2 -->
<div class="slide-card">
<div class="slide-header">
<h2 class="slide-title">▪ 핵심 개념 : PM의 인지 루프(Cognitive Loop) 확장</h2>
<span class="slide-num">SLIDE 02</span>
</div>
<div class="slide-summary">PM이 실제로 수행하는 인지 루프(보고 → 듣고 → 판단하고 → 실행하는)를 AI가 동일하게 24시간 확장합니다. 주도권은 여전히 PM에게 있습니다.</div>
<div class="svg-container">
<!-- Loop Infographic SVG -->
<svg width="850" height="250" viewBox="0 0 850 250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="see" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#0ea5e9"/><stop offset="100%" stop-color="#0284c7"/></linearGradient>
    <linearGradient id="hear" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#06b6d4"/><stop offset="100%" stop-color="#0891b2"/></linearGradient>
    <linearGradient id="think" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#a855f7"/><stop offset="100%" stop-color="#9333ea"/></linearGradient>
    <linearGradient id="act" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#22c55e"/><stop offset="100%" stop-color="#16a34a"/></linearGradient>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 Z" fill="#94a3b8" />
    </marker>
  </defs>
  
  <rect x="30" y="50" width="160" height="110" rx="15" fill="url(#see)" />
  <text x="110" y="95" fill="#fff" font-size="22" font-weight="bold" text-anchor="middle">SEE (관측)</text>
  <text x="110" y="125" fill="#e0f2fe" font-size="13" text-anchor="middle">일정·리스크 상시 수집</text>
  <path d="M 190 105 L 245 105" stroke="#cbd5e1" stroke-width="4" marker-end="url(#arrow)" />
  
  <rect x="250" y="50" width="160" height="110" rx="15" fill="url(#hear)" />
  <text x="330" y="95" fill="#fff" font-size="22" font-weight="bold" text-anchor="middle">HEAR (수렴)</text>
  <text x="330" y="125" fill="#cffafe" font-size="13" text-anchor="middle">관계자 소통 신호 반영</text>
  <path d="M 410 105 L 465 105" stroke="#cbd5e1" stroke-width="4" marker-end="url(#arrow)" />
  
  <rect x="470" y="50" width="160" height="110" rx="15" fill="url(#think)" />
  <text x="550" y="95" fill="#fff" font-size="22" font-weight="bold" text-anchor="middle">THINK (판단)</text>
  <text x="550" y="125" fill="#f3e8ff" font-size="13" text-anchor="middle">가치 기반 상충 통합</text>
  <path d="M 630 105 L 685 105" stroke="#cbd5e1" stroke-width="4" marker-end="url(#arrow)" />
  
  <rect x="690" y="50" width="160" height="110" rx="15" fill="url(#act)" />
  <text x="770" y="95" fill="#fff" font-size="22" font-weight="bold" text-anchor="middle">ACT (실행)</text>
  <text x="770" y="125" fill="#dcfce7" font-size="13" text-anchor="middle">조치 연결 및 PM 승인</text>
  
  <path d="M 770 160 Q 770 230 440 230 Q 110 230 110 160" fill="none" stroke="#94a3b8" stroke-width="4" stroke-dasharray="8,8" />
  <text x="440" y="215" fill="#64748b" font-weight="bold" text-anchor="middle">루프 반환 (관측의 연속성 확보)</text>
</svg>
</div>
</div>

<!-- SLIDE 3 -->
<div class="slide-card">
<div class="slide-header">
<h2 class="slide-title">▪ 작동 방식 : 7개 도메인 에이전트의 합체(Signal Forge)</h2>
<span class="slide-num">SLIDE 03</span>
</div>
<div class="slide-summary">각 에이전트는 자기 도메인의 전문가 역할을 합니다. 상충하는 여러 신호는 거대한 통합 엔진(Signal Forge)으로 모여 하나의 결단으로 합쳐집니다.</div>
<div class="svg-container">
<!-- Multi-Agent Node SVG -->
<svg width="800" height="320" viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg">
  <!-- Connectors -->
  <line x1="200" y1="80" x2="400" y2="160" stroke="#cbd5e1" stroke-width="3"/>
  <line x1="400" y1="60" x2="400" y2="160" stroke="#cbd5e1" stroke-width="3"/>
  <line x1="600" y1="80" x2="400" y2="160" stroke="#cbd5e1" stroke-width="3"/>
  <line x1="120" y1="180" x2="400" y2="160" stroke="#cbd5e1" stroke-width="3"/>
  <line x1="300" y1="260" x2="400" y2="160" stroke="#cbd5e1" stroke-width="3"/>
  <line x1="500" y1="260" x2="400" y2="160" stroke="#cbd5e1" stroke-width="3"/>
  <line x1="680" y1="180" x2="400" y2="160" stroke="#cbd5e1" stroke-width="3"/>

  <!-- Agent Nodes -->
  <circle cx="200" cy="80" r="45" fill="#4f46e5"/> <text x="200" y="85" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">거버넌스</text>
  <circle cx="400" cy="60" r="45" fill="#0ea5e9"/> <text x="400" y="65" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">일정</text>
  <circle cx="600" cy="80" r="45" fill="#f59e0b"/> <text x="600" y="85" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">범위/품질</text>
  <circle cx="120" cy="180" r="45" fill="#ec4899"/> <text x="120" y="185" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">관계자</text>
  <circle cx="300" cy="260" r="45" fill="#22c55e"/> <text x="300" y="265" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">자원/역량</text>
  <circle cx="500" cy="260" r="45" fill="#8b5cf6"/> <text x="500" y="265" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">재무</text>
  <circle cx="680" cy="180" r="45" fill="#ef4444"/> <text x="680" y="185" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">리스크</text>

  <!-- Central Forge -->
  <circle cx="400" cy="160" r="60" fill="#0f172a" stroke="#38bdf8" stroke-width="4"/>
  <text x="400" y="155" fill="#38bdf8" font-size="18" font-weight="bold" text-anchor="middle">Signal</text>
  <text x="400" y="180" fill="#38bdf8" font-size="18" font-weight="bold" text-anchor="middle">Forge</text>
</svg>
</div>
</div>

<!-- SLIDE 4 -->
<div class="slide-card">
<div class="slide-header">
<h2 class="slide-title">▪ 상충을 '가치(North Star)'로 결단하는 프로세스</h2>
<span class="slide-num">SLIDE 04</span>
</div>
<div class="grid-2">
<div class="card">
    <div class="card-title">Mindset 3차원 &amp; 6원칙</div>
    <ul style="margin-bottom:1rem;">
        <li><strong style="color:var(--accent);">선제적 (Proactive):</strong> 전체론적 관점 및 품질 내재화</li>
        <li><strong style="color:var(--primary);">소유권 (Ownership):</strong> 책임감 확립 및 권한 강화 문화</li>
        <li><strong style="color:var(--green);">가치 중심 (Value-Driven):</strong> 집중과 지속가능성의 통합</li>
    </ul>
    <p>판단 기준: 상충하는 안건에 대해 <strong>프로젝트 최우선 가치서열(North Star)</strong>에 따라 심판합니다.</p>
</div>
<div class="card" style="background:#fff7ed; border-color:var(--orange);">
    <div class="card-title" style="color:var(--orange);">판단 시나리오 예시</div>
    <p><strong>[상충 발생]</strong> 일정 사수(Schedule) vs 범위 변경 요구(Scope) vs 이해관계자 수용(Stakeholder)</p>
    <br>
    <ul>
        <li><strong>Signal Forge 분석:</strong> 해당 변경 수용 시 주 경로(Critical Path) 2주 지연 위험 감지</li>
        <li><strong>가치 기반 중재(North Star):</strong> 품질 보장을 위해 변경통제위원회(CCB) 긴급 회부 유도</li>
        <li><strong>결과 실행:</strong> 대안 초안 자동 작성 후 PM 승인 대기</li>
    </ul>
</div>
</div>
</div>

<!-- SLIDE 5 -->
<div class="slide-card">
<div class="slide-header">
<h2 class="slide-title">▪ PM 통합 워크스페이스 기능 및 기대효과(KPI)</h2>
<span class="slide-num">SLIDE 05</span>
</div>
<table>
<thead>
<tr>
    <th style="width: 20%;">기능(화면)</th>
    <th style="width: 45%;">지원 역할</th>
    <th style="width: 35%;">기대효과 및 KPI 향상</th>
</tr>
</thead>
<tbody>
<tr>
    <td><strong>홈 대시보드</strong></td>
    <td>7개 에이전트 감지 종합 브리핑 및 프로젝트 건강도 모니터링</td>
    <td>이상징후 감지 리드타임 <strong>수일 → 1시간 이내(실시간)</strong></td>
</tr>
<tr>
    <td><strong>이슈 &amp; 리스크 관리</strong></td>
    <td>감지 신호 등재, AI 대응안 생성, Jira 시스템 자동 티켓 연동</td>
    <td>리스크 커버리지 전 도메인 확대 및 <strong>누락 제로(0)화</strong></td>
</tr>
<tr>
    <td><strong>거버넌스 &amp; 리포트</strong></td>
    <td>변경통제(CR/CCB) 절차 자동 유도 및 주간 리포트 자동 생성</td>
    <td>문서 작성 공수 <strong>2시간 → 10분</strong> 극적 절감</td>
</tr>
<tr>
    <td><strong>커뮤니케이션</strong></td>
    <td>이해관계자 기대 충돌 분석 및 소통/메일 가이드 초안 제시</td>
    <td>의사결정 및 가치서열 판정 기준의 <strong>일관성 100% 확보</strong></td>
</tr>
</tbody>
</table>
</div>

</div>
</body>
</html>
"""

with open(r"d:\workspaces\PMC_POC\output\poc_ppt.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML update successfully applied!")