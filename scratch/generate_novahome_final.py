# coding: utf-8
import os
import codecs

def create_v3():
    html = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8"/>
<title>NovaHome Connect — Stage 1 & 2 Detailed Tool Data (v3)</title>
<style>
  body { font-family: 'Inter', sans-serif; padding: 2rem; background: #f8f9fa; color: #1e293b; }
  .tool-section { background: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
  h1 { color: #0f2743; }
  h2 { color: #0284c7; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; }
  h3 { color: #0369a1; }
  table { width: 100%; border-collapse: collapse; margin-bottom: 1rem; }
  th, td { border: 1px solid #cbd5e1; padding: 0.75rem; text-align: left; }
  th { background: #f1f5f9; }
</style>
</head>
<body>
<h1>NovaHome Connect — PMBOK Tool Data (v3)</h1>
<p>Detailed analysis tools for 5 core problems identified in the NovaHome Connect project.</p>

<!-- Problem 1 -->
<div class="tool-section" id="prob1">
  <h2>1. 독단적 범위 결정 및 협의 부재 (Scope Creep/Cut)</h2>
  
  <h3>Tool 1-A: Stakeholder Register (이해관계자 등록부)</h3>
  <table>
    <tr><th>이해관계자</th><th>영향력/관심도</th><th>주요 기대사항</th><th>이슈</th></tr>
    <tr><td>이현수 (Sponsor)</td><td>High / High</td><td>11/15 글로벌 론칭, 비즈니스 가치 창출</td><td>소셜 로그인 제외 결정 미보고로 인한 분노</td></tr>
    <tr><td>최서린 (PO)</td><td>High / High</td><td>캠페인 연계를 위한 소셜 로그인(REQ-017) 포함</td><td>PM의 일방적 제외 통보로 인한 마찰</td></tr>
  </table>

  <h3>Tool 1-B: Change Log (변경 기록부)</h3>
  <table>
    <tr><th>CR ID</th><th>변경 항목</th><th>요청자</th><th>상태</th><th>비고</th></tr>
    <tr><td>CR-012</td><td>소셜 로그인(REQ-017) 베타 제외</td><td>이도윤 PM</td><td>Rejected/Bypassed</td><td>CCB 미승인 상태로 PM 임의 결정</td></tr>
  </table>

  <h3>Tool 1-C: Requirements Traceability Matrix (요구사항 추적 매트릭스)</h3>
  <table>
    <tr><th>Req ID</th><th>요구사항 설명</th><th>비즈니스 목표</th><th>현재 상태</th></tr>
    <tr><td>REQ-017</td><td>소셜 로그인 추가</td><td>분기 캠페인 핵심 메시지, 사용자 유입</td><td>내부 데모만 허용 (외부 미노출)</td></tr>
  </table>

  <h3>Tool 1-D: Responsibility Assignment Matrix (RACI)</h3>
  <table>
    <tr><th>Activity</th><th>PM</th><th>PO</th><th>Sponsor</th></tr>
    <tr><td>베타 기능 범위 확정</td><td>R, A (문제발생점)</td><td>C (무시됨)</td><td>I (누락됨)</td></tr>
  </table>
</div>

<!-- Problem 2 -->
<div class="tool-section" id="prob2">
  <h2>2. 외부 벤더 의존성 관리 실패 (Vendor Dependency)</h2>
  
  <h3>Tool 2-A: Critical Path Method (CPM)</h3>
  <table>
    <tr><th>Activity</th><th>Duration</th><th>Predecessors</th><th>Slack</th></tr>
    <tr><td>Nebula SDK 2.4 Upgrade</td><td>2d (10/5-6)</td><td>-</td><td>0 (Critical)</td></tr>
    <tr><td>Geo-IP Allowlist Request</td><td>7d</td><td>SDK Upgrade</td><td>-5d (Delayed)</td></tr>
  </table>

  <h3>Tool 2-B: Vendor SLA Tracking</h3>
  <table>
    <tr><th>Vendor</th><th>Metric</th><th>Target</th><th>Current</th></tr>
    <tr><td>NebulaWorks</td><td>SDK Support Response</td><td>&lt; 24h</td><td>Compliant</td></tr>
    <tr><td>NebulaWorks</td><td>Geo-IP Lead Time</td><td>5-7 days</td><td>Warning (Past experience: 14 days)</td></tr>
  </table>

  <h3>Tool 2-C: Milestone Chart</h3>
  <table>
    <tr><th>Milestone</th><th>Planned Date</th><th>Actual/Forecast</th><th>Status</th></tr>
    <tr><td>Integration Test (Vendor)</td><td>10/07 - 10/12</td><td>Not scheduled</td><td>Blocked</td></tr>
  </table>

  <h3>Tool 2-D: Risk Register (Vendor)</h3>
  <table>
    <tr><th>Risk ID</th><th>Description</th><th>Probability</th><th>Impact</th></tr>
    <tr><td>RSK-008</td><td>Geo-IP enforcement (11/01) blocks EU users</td><td>High (80%)</td><td>Critical (Launch Failure)</td></tr>
  </table>
</div>

<!-- Problem 3 -->
<div class="tool-section" id="prob3">
  <h2>3. 변경 통제 부재로 인한 품질 불안정 (Quality/CR)</h2>
  
  <h3>Tool 3-A: Control Chart (성능 지표)</h3>
  <table>
    <tr><th>Metric</th><th>UCL (Upper Control Limit)</th><th>Average</th><th>Latest Point</th></tr>
    <tr><td>/me/devices Response p95</td><td>300ms</td><td>220ms</td><td>410ms (Out of Control)</td></tr>
  </table>

  <h3>Tool 3-B: Defect Density & CI Metrics</h3>
  <table>
    <tr><th>Metric</th><th>Target</th><th>Current</th></tr>
    <tr><td>CI Build Success Rate</td><td>&gt;= 85%</td><td>78%</td></tr>
    <tr><td>RTM Reconnect Failures</td><td>0%</td><td>5.2% (Intermittent)</td></tr>
  </table>

  <h3>Tool 3-C: Root Cause Analysis (Fishbone output)</h3>
  <ul>
    <li>Method: Environment -&gt; Code Cache Policy change without CR -&gt; Test cases invalidated.</li>
  </ul>

  <h3>Tool 3-D: Quality Metrics Status</h3>
  <table>
    <tr><th>Req ID</th><th>Feature</th><th>Error Rate Goal</th><th>Current Error Rate</th></tr>
    <tr><td>REQ-003</td><td>Device Registration</td><td>&lt;= 0.2%</td><td>0.35% (Blocked by Cache)</td></tr>
  </table>
</div>

<!-- Problem 4 -->
<div class="tool-section" id="prob4">
  <h2>4. 보안 및 규제 요구사항 식별 지연 (Compliance)</h2>
  
  <h3>Tool 4-A: Compliance Checklist</h3>
  <table>
    <tr><th>Item</th><th>Requirement</th><th>Status</th></tr>
    <tr><td>EU Privacy Mode</td><td>Keepalive interval adjustment</td><td>Pending Action</td></tr>
    <tr><td>RTM Consent Terms</td><td>Update user terms</td><td>Draft Missing (CRB Delayed)</td></tr>
  </table>

  <h3>Tool 4-B: Issue Log</h3>
  <table>
    <tr><th>Issue ID</th><th>Description</th><th>Owner</th><th>Due Date</th></tr>
    <tr><td>ISS-014</td><td>Security terms lacking RTM wording</td><td>윤세라 (Security)</td><td>10/10 (Draft)</td></tr>
  </table>

  <h3>Tool 4-C: Prompt List (Risk Categories)</h3>
  <ul>
    <li>Legal/Regulatory: Potential penalty for EU GDPR violation if RTM consent is missed.</li>
  </ul>

  <h3>Tool 4-D: Probability and Impact Matrix</h3>
  <table>
    <tr><th>Risk</th><th>P</th><th>I</th><th>Score</th></tr>
    <tr><td>CRB Rejection of Terms</td><td>Medium (3)</td><td>High (5)</td><td>15 (Red)</td></tr>
  </table>
</div>

<!-- Problem 5 -->
<div class="tool-section" id="prob5">
  <h2>5. 문서화 지연에 따른 도메인 파급효과 (Team/Schema)</h2>
  
  <h3>Tool 5-A: Resource Histogram</h3>
  <table>
    <tr><th>Role</th><th>Planned Allocation</th><th>Actual (Due to rework)</th></tr>
    <tr><td>QA (문해인)</td><td>100%</td><td>140% (Overloaded)</td></tr>
    <tr><td>FE (강민재)</td><td>100%</td><td>130% (Overloaded)</td></tr>
  </table>

  <h3>Tool 5-B: Communications Management Plan</h3>
  <table>
    <tr><th>Information</th><th>Sender</th><th>Receiver</th><th>Frequency</th></tr>
    <tr><td>Schema v3 Docs</td><td>Device Lead</td><td>FE, BE, QA</td><td>Ad-hoc (Delayed to 18:00 today)</td></tr>
  </table>

  <h3>Tool 5-C: Sprint Burndown Chart Data</h3>
  <table>
    <tr><th>Day</th><th>Planned Remaining (pts)</th><th>Actual Remaining</th></tr>
    <tr><td>Day 8</td><td>40</td><td>65 (Stagnant)</td></tr>
  </table>

  <h3>Tool 5-D: Team Morale Survey (Proxy)</h3>
  <ul>
    <li>Blind Post Sentiment: Highly Negative (Burnout, Siloed info, Unplanned rework)</li>
  </ul>
</div>

</body>
</html>
"""
    with codecs.open(r"d:\workspaces\PMC_POC\NovaHome_Connect_stage1_stage2_analysis_v3.html", "w", "utf-8") as f:
        f.write(html)

def create_v4():
    html = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>NovaHome Connect — 분석 및 AI 에이전트 적용 리포트 (v4)</title>
<style>
  :root {
    --bg: #0f172a;
    --surface: #1e293b;
    --surface-alt: #334155;
    --primary: #38bdf8;
    --primary-dark: #0284c7;
    --accent: #a855f7;
    --red: #f43f5e;
    --text: #f8fafc;
    --border: #475569;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', sans-serif;
    background-color: var(--bg);
    color: var(--text);
    line-height: 1.6;
    padding: 2rem;
  }
  .container { max-width: 1400px; margin: 0 auto; }
  header {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    padding: 2.5rem;
    border-radius: 16px;
    border: 1px solid rgba(56, 189, 248, 0.3);
    margin-bottom: 2.5rem;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
  }
  header h1 { font-size: 2.2rem; font-weight: 800; color: var(--primary); margin-bottom: 0.5rem; }
  .slide-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 2.5rem;
    margin-bottom: 2.5rem;
  }
  .slide-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid var(--border);
    padding-bottom: 1rem;
    margin-bottom: 1.5rem;
  }
  .slide-title { font-size: 1.4rem; font-weight: 700; color: var(--text); }
  .slide-num { background: var(--primary-dark); color: #fff; padding: 0.2rem 0.6rem; border-radius: 6px; font-weight: 700; font-size: 0.85rem;}
  table { width: 100%; border-collapse: collapse; margin-bottom: 1rem; font-size: 0.95rem; }
  th, td { border-bottom: 1px solid var(--border); padding: 0.8rem; text-align: left; }
  th { background: var(--surface-alt); color: var(--primary); }
  .svg-container { background: var(--surface-alt); padding: 2rem; border-radius: 12px; text-align: center; margin: 1.5rem 0;}
  .flex-row { display: flex; gap: 2rem; align-items: stretch; }
  .flex-col { flex: 1; }
  .alert-box { background: rgba(244, 63, 94, 0.1); border-left: 4px solid var(--red); padding: 1rem; border-radius: 4px; margin-bottom: 1rem;}
</style>
</head>
<body>
<div class="container">

<header>
  <h1>NovaHome Connect 프로젝트 종합 진단 보고서</h1>
  <div class="subtitle">글로벌 표준 프레임워크 기반의 Root Cause 분석 및 AI Agent 적용 방안</div>
</header>

<!-- SLIDE 01 -->
<div class="slide-card">
  <div class="slide-header">
    <h2 class="slide-title">Executive Summary & Gap Analysis</h2>
    <span class="slide-num">SLIDE 01</span>
  </div>
  <p>NovaHome Connect 프로젝트는 11월 15일 글로벌 론칭을 앞두고 있으나, 일정 지연, 성능 저하(p95 410ms), 외부 벤더 통제력 상실 등 치명적인 위기에 직면해 있습니다.</p>
  <p>이는 단순한 기술적 결함이 아니라 <strong>거버넌스 부재, 사일로화된 소통, 협력사 관리 실패</strong>라는 구조적(Systemic) 원인에서 비롯되었습니다. 글로벌 표준 프레임워크 관점에서 핵심 원인을 분석하고, AI Agent를 활용한 미래 지향적 통제 방안을 제안합니다.</p>
</div>

<!-- SLIDE 02 -->
<div class="slide-card">
  <div class="slide-header">
    <h2 class="slide-title">Impact-Urgency Prioritization Matrix</h2>
    <span class="slide-num">SLIDE 02</span>
  </div>
  <table>
    <tr><th>우선순위</th><th>문제 영역</th><th>영향도(Impact)</th><th>시급성(Urgency)</th><th>Risk Level</th></tr>
    <tr style="background:rgba(244, 63, 94, 0.1);"><td>1</td><td>독단적 범위 결정 (소셜 로그인 제외)</td><td>High</td><td>High</td><td>Critical</td></tr>
    <tr style="background:rgba(244, 63, 94, 0.1);"><td>2</td><td>외부 벤더 의존성 파악 누락 (Geo-IP)</td><td>High</td><td>High</td><td>Critical</td></tr>
    <tr style="background:rgba(244, 63, 94, 0.1);"><td>3</td><td>변경 통제 부재 및 품질/성능 저하</td><td>High</td><td>High</td><td>Critical</td></tr>
    <tr style="background:rgba(244, 63, 94, 0.1);"><td>4</td><td>보안 및 규제 약관 갱신 지연</td><td>High</td><td>Medium</td><td>High</td></tr>
    <tr style="background:rgba(244, 63, 94, 0.1);"><td>5</td><td>스키마 문서화 지연 (도메인 파급)</td><td>Medium</td><td>High</td><td>High</td></tr>
  </table>
</div>

<!-- SLIDE 03 -->
<div class="slide-card">
  <div class="slide-header">
    <h2 class="slide-title">Core Problem 1: 독단적 범위 결정 및 가치 충돌</h2>
    <span class="slide-num">SLIDE 03</span>
  </div>
  <div class="flex-row">
    <div class="flex-col" style="flex: 0 0 200px; display:flex; align-items:center; justify-content:center;">
      <svg viewBox="0 0 100 100" width="150" height="150">
        <rect width="100" height="100" fill="#1e293b" rx="10"/>
        <circle cx="50" cy="50" r="30" fill="none" stroke="#38bdf8" stroke-width="4" stroke-dasharray="10 5"/>
        <path d="M50 20 L50 80 M20 50 L80 50" stroke="#a855f7" stroke-width="4"/>
      </svg>
    </div>
    <div class="flex-col">
      <div class="alert-box"><strong>증상:</strong> 스폰서와 마케팅이 중시하는 '소셜 로그인' 기능을 PM이 단독으로 베타에서 제외하여 비즈니스 가치 훼손 및 스폰서 분노 유발.</div>
      <p><strong>근본 원인 (Mindset):</strong> Value-driven(가치 중심) 마인드셋 부재. 프로젝트의 North Star(캠페인 유입)보다 단기적 일정(Delivery)만을 우선시함.</p>
      <p><strong>도메인 매핑:</strong> Stakeholder Domain (이해관계자 기대 불일치), Delivery Domain (범위 통제 실패).</p>
      <p><strong>AI Use Case (Change Guardian):</strong> 회의록/메신저를 분석하여 잠재적 Scope Cut 감지 시, 비즈니스 목표와의 충돌 여부를 계산하고 스폰서 승인 프로세스(CCB)를 강제 에스컬레이션함.</p>
    </div>
  </div>
</div>

<!-- SLIDE 04 -->
<div class="slide-card">
  <div class="slide-header">
    <h2 class="slide-title">Core Problem 2: 외부 벤더 의존성 관리 실패</h2>
    <span class="slide-num">SLIDE 04</span>
  </div>
  <div class="flex-row">
    <div class="flex-col" style="flex: 0 0 200px; display:flex; align-items:center; justify-content:center;">
      <svg viewBox="0 0 100 100" width="150" height="150">
        <rect width="100" height="100" fill="#1e293b" rx="10"/>
        <path d="M30 30 h40 v40 h-40 z" fill="none" stroke="#f43f5e" stroke-width="4"/>
        <circle cx="30" cy="30" r="8" fill="#38bdf8"/>
        <circle cx="70" cy="70" r="8" fill="#38bdf8"/>
        <path d="M30 30 L70 70" stroke="#f8fafc" stroke-width="2" stroke-dasharray="4"/>
      </svg>
    </div>
    <div class="flex-col">
      <div class="alert-box"><strong>증상:</strong> Nebula SDK 2.4 및 Geo-IP 차단(11/1) 등 벤더의 치명적 마일스톤이 내부 캘린더에 누락됨.</div>
      <p><strong>근본 원인 (Mindset):</strong> Ownership(소유권) 부족. 외부 리소스를 프로젝트 시스템의 일부로 편입시키지 못하고 사일로(Silo) 상태로 방치.</p>
      <p><strong>도메인 매핑:</strong> Planning Domain (통합 계획 누락), Project Work Domain (공급업체 조율 실패).</p>
      <p><strong>AI Use Case (Schedule Sentinel):</strong> 벤더 이메일 수신 즉시 핵심 날짜(Geo-IP, SLA)를 추출하여 프로젝트 통합 CPM(임계경로) 매트릭스와 교차 검증하고 누락 시 경고 알림.</p>
    </div>
  </div>
</div>

<!-- SLIDE 05 -->
<div class="slide-card">
  <div class="slide-header">
    <h2 class="slide-title">Core Problem 3: 변경 통제 부재 및 품질 저하</h2>
    <span class="slide-num">SLIDE 05</span>
  </div>
  <div class="flex-row">
    <div class="flex-col" style="flex: 0 0 200px; display:flex; align-items:center; justify-content:center;">
      <svg viewBox="0 0 100 100" width="150" height="150">
        <rect width="100" height="100" fill="#1e293b" rx="10"/>
        <path d="M20 50 Q 50 20 80 50 T 20 50" fill="none" stroke="#22c55e" stroke-width="4"/>
        <line x1="50" y1="20" x2="50" y2="80" stroke="#f97316" stroke-width="4"/>
      </svg>
    </div>
    <div class="flex-col">
      <div class="alert-box"><strong>증상:</strong> 임의의 캐시 정책 변경(CR 미등록)으로 인해 p95 410ms 지연 및 CI 테스트 케이스 무효화 발생.</div>
      <p><strong>근본 원인 (Mindset):</strong> Proactive(선제적) 품질 내재화 마인드셋 부족. 개발 편의를 위해 형상관리 및 변경통제 프로세스를 우회함.</p>
      <p><strong>도메인 매핑:</strong> Quality Domain (테스트 오염), Delivery Domain (아키텍처 변경 관리 실패).</p>
      <p><strong>AI Use Case (Governance Watchdog):</strong> 코드 저장소 커밋과 Jira CR 티켓을 실시간 대조. 미등록 CR로 인한 핵심 로직 변경 감지 시 CI 빌드를 중단하고 PM에게 리뷰 요청.</p>
    </div>
  </div>
</div>

<!-- SLIDE 06 -->
<div class="slide-card">
  <div class="slide-header">
    <h2 class="slide-title">Core Problem 4: 규제(Compliance) 요구사항 식별 지연</h2>
    <span class="slide-num">SLIDE 06</span>
  </div>
  <div class="flex-row">
    <div class="flex-col" style="flex: 0 0 200px; display:flex; align-items:center; justify-content:center;">
      <svg viewBox="0 0 100 100" width="150" height="150">
        <rect width="100" height="100" fill="#1e293b" rx="10"/>
        <polygon points="50,15 85,35 85,75 50,95 15,75 15,35" fill="none" stroke="#eab308" stroke-width="4"/>
        <circle cx="50" cy="55" r="10" fill="#eab308"/>
      </svg>
    </div>
    <div class="flex-col">
      <div class="alert-box"><strong>증상:</strong> EU 프라이버시 및 RTM 약관 추가가 지연되어 CRB(보안심의) 통과 불투명, 론칭 중단 리스크 도래.</div>
      <p><strong>근본 원인 (Mindset):</strong> Proactive 리스크 식별 부재. 기능 구현에만 집중하여 비기능적(법규/보안) 요구사항 관리에 소홀함.</p>
      <p><strong>도메인 매핑:</strong> Risk Domain (컴플라이언스 위협), Planning Domain.</p>
      <p><strong>AI Use Case (Risk Oracle):</strong> 기능 스펙(RTM) 문서를 스캔하여 글로벌 규제 DB(GDPR 등)와 대조, 법무 검토 필요성을 조기 식별 및 마일스톤에 강제 할당.</p>
    </div>
  </div>
</div>

<!-- SLIDE 07 -->
<div class="slide-card">
  <div class="slide-header">
    <h2 class="slide-title">Core Problem 5: 문서화 지연에 따른 도메인 파급</h2>
    <span class="slide-num">SLIDE 07</span>
  </div>
  <div class="flex-row">
    <div class="flex-col" style="flex: 0 0 200px; display:flex; align-items:center; justify-content:center;">
      <svg viewBox="0 0 100 100" width="150" height="150">
        <rect width="100" height="100" fill="#1e293b" rx="10"/>
        <path d="M30 20 h40 v60 h-40 z" fill="none" stroke="#38bdf8" stroke-width="4"/>
        <line x1="40" y1="40" x2="60" y2="40" stroke="#a855f7" stroke-width="3"/>
        <line x1="40" y1="60" x2="60" y2="60" stroke="#a855f7" stroke-width="3"/>
      </svg>
    </div>
    <div class="flex-col">
      <div class="alert-box"><strong>증상:</strong> 스키마 v3 문서가 배포되지 않아 파서가 꼬이고, QA/FE 팀이 불필요한 재작업 및 야근에 시달림.</div>
      <p><strong>근본 원인 (Mindset):</strong> Ownership 부족. "내 모듈 개발만 끝나면 완료"라는 시각으로, 후속 공정(QA/FE)에 대한 배려 결여.</p>
      <p><strong>도메인 매핑:</strong> Team Domain (협업 저하), Project Work Domain.</p>
      <p><strong>AI Use Case (Resource Radar):</strong> 선행 산출물(API 문서)의 배포 지연 시, 의존성이 걸린 후행 작업자(FE/QA)의 초과 근무(Overload) 가능성을 시뮬레이션하여 지표로 가시화.</p>
    </div>
  </div>
</div>

<!-- SLIDE 08 -->
<div class="slide-card">
  <div class="slide-header">
    <h2 class="slide-title">Causal Relationship Map (원인-결과 구조도)</h2>
    <span class="slide-num">SLIDE 08</span>
  </div>
  <div class="svg-container">
    <svg width="800" height="400" viewBox="0 0 800 400">
      <rect width="800" height="400" fill="#1e293b" rx="12"/>
      
      <!-- Nodes -->
      <g transform="translate(100, 50)"><rect width="160" height="60" rx="8" fill="#f43f5e"/><text x="180" y="85" fill="#fff" text-anchor="middle" font-size="14">독단적 범위 통제</text></g>
      <g transform="translate(100, 200)"><rect width="160" height="60" rx="8" fill="#38bdf8"/><text x="180" y="235" fill="#fff" text-anchor="middle" font-size="14">임의의 캐시 변경</text></g>
      <g transform="translate(500, 50)"><rect width="160" height="60" rx="8" fill="#a855f7"/><text x="580" y="85" fill="#fff" text-anchor="middle" font-size="14">이해관계자 신뢰 하락</text></g>
      <g transform="translate(500, 200)"><rect width="160" height="60" rx="8" fill="#22c55e"/><text x="580" y="235" fill="#fff" text-anchor="middle" font-size="14">CI 품질 붕괴 / 장애</text></g>
      <g transform="translate(300, 300)"><rect width="160" height="60" rx="8" fill="#eab308"/><text x="380" y="335" fill="#fff" text-anchor="middle" font-size="14">문서화/소통 지연</text></g>

      <!-- Edges -->
      <path d="M 260 80 L 500 80" stroke="#94a3b8" stroke-width="3" marker-end="url(#arrow)"/>
      <path d="M 260 230 L 500 230" stroke="#94a3b8" stroke-width="3" marker-end="url(#arrow)"/>
      <path d="M 380 300 L 540 260" stroke="#94a3b8" stroke-width="3" stroke-dasharray="5" marker-end="url(#arrow)"/>

      <!-- Marker -->
      <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="#94a3b8" />
        </marker>
      </defs>
    </svg>
  </div>
</div>

<!-- SLIDE 09 -->
<div class="slide-card">
  <div class="slide-header">
    <h2 class="slide-title">Mindset Synthesis (미래 지향적 해결 방안)</h2>
    <span class="slide-num">SLIDE 09</span>
  </div>
  <table>
    <tr><th>Mindset Dimension</th><th>Current State (As-Is)</th><th>Future State with AI Agent (To-Be)</th></tr>
    <tr>
      <td><strong>Proactive (선제적)</strong></td>
      <td>결함 발생 후 야근, CRB 거절 시점에 일정 수정</td>
      <td>Risk Oracle &amp; Watchdog을 통한 <strong>사전 인지 및 자동 방어 체계</strong> 구축 (이슈 예방)</td>
    </tr>
    <tr>
      <td><strong>Ownership (소유권)</strong></td>
      <td>내 모듈만 완수하면 끝, 외부 벤더 관리는 방치</td>
      <td>Schedule Sentinel로 전체 밸류체인(벤더 포함)을 모니터링하여 <strong>통합된 하나의 프로젝트</strong>로 통제</td>
    </tr>
    <tr>
      <td><strong>Value-Driven (가치 중심)</strong></td>
      <td>단기 납기(Delivery)를 위해 비즈니스 가치(소셜 로그인) 희생</td>
      <td>Change Guardian의 'North Star' 가치서열 판정에 따라, 상충 시 <strong>비즈니스 가치 최적화</strong>를 PM에게 유도</td>
    </tr>
  </table>
</div>

</div>
</body>
</html>
"""
    with codecs.open(r"d:\workspaces\PMC_POC\NovaHome_Connect_stage1_stage2_analysis_v4.html", "w", "utf-8") as f:
        f.write(html)

def create_v5():
    with codecs.open(r"d:\workspaces\PMC_POC\NovaHome_Connect_stage1_stage2_analysis_v4.html", "r", "utf-8") as f:
        v4_html = f.read()
        
    poc_path = r"d:\workspaces\PMC_POC\output\poc_ppt.html"
    poc_html = ""
    if os.path.exists(poc_path):
        with codecs.open(poc_path, "r", "utf-8") as f:
            poc_html = f.read()
            
    import re
    slides_match = re.search(r'<div class="container">(.*?)</div>\s*</body>', poc_html, re.DOTALL)
    if slides_match:
        poc_slides = slides_match.group(1)
        poc_slides = "\n<!-- POC SECTION APPENDED -->\n" + "<div style='margin-top: 5rem; border-top: 4px dashed #38bdf8; padding-top: 3rem;'><h1 style='color:#38bdf8; text-align:center; font-size: 2.5rem; margin-bottom: 2rem;'>Appendix: PM Transformers POC</h1></div>\n" + poc_slides
        v5_html = v4_html.replace('</div>\n</body>\n</html>', poc_slides + '\n</div>\n</body>\n</html>')
    else:
        v5_html = v4_html + "\n<!-- Could not extract slides -->"
        
    with codecs.open(r"d:\workspaces\PMC_POC\NovaHome_Connect_stage1_stage2_analysis_v5.html", "w", "utf-8") as f:
        f.write(v5_html)

if __name__ == "__main__":
    create_v3()
    create_v4()
    create_v5()
    print("Generation complete.")
