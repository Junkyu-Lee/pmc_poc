import bs4
import copy
import os

def main():
    v4_source = r"d:\workspaces\PMC_POC\stage1_stage2_analysis_v4.html"
    v4_out = r"d:\workspaces\PMC_POC\output\NextGen_AutoCockpit_Mission_v4.html"
    v3_out = r"d:\workspaces\PMC_POC\output\NextGen_AutoCockpit_Mission_v3.html"

    with open(v4_source, "r", encoding="utf-8") as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')

    # 1. Update Title and Header to reflect Evaluation Criteria
    title = soup.find('title')
    if title: title.string = "NextGen AutoCockpit PM Competition — 심사기준(Stage 1&2) 반영 종합 진단 (v4)"
    
    header_title = soup.find('h1')
    if header_title: header_title.string = "❖ NextGen AutoCockpit 프로젝트 심층 진단 및 AI 에이전틱 리포트"

    # 2. Enrich Slide Summaries with Criteria Keywords
    summaries = soup.find_all('div', class_='slide-summary')
    
    s01_text = "요약: [Stage 1] 명확한 이상징후 식별 및 [Stage 2] Performance Domain 간 다차원적 파급효과 시뮬레이션을 통해, 단순 현상이 아닌 시스템 관점의 5대 핵심 근본 원인을 도출합니다."
    s02_text = "프로젝트 현황 (Identify): G3 릴리스 D-15 시점에서 소셜 로그인 기습 반영(Scope Creep) 및 SDK 지연이라는 징후를 명확하게 포착하고, 조직 거버넌스 붕괴라는 시스템적 결함을 도출했습니다."
    s04_text = "성과 및 파급효과 분석: 응답속도, 오류율 등 주요 KPI 미달이 [Delivery Domain]과 [Development Approach]에 미치는 파급효과(Ripple Effect)를 심층 분석했습니다."
    s05_text = "우선순위 (Impact-Urgency): 표면적 증상이 아닌 근본 원인(Root Causes)을 파악하고, Proactive(예방적) 마인드셋에 입각하여 억대 리콜 손실을 방어하기 위한 Top 5 과제를 식별합니다."
    s11_text = "결론 (Mindset Synthesis): Proactive, Ownership, Value-driven 3대 마인드셋을 적용하여, 임시방편(Reactive) 대응을 종식하고 AI 에이전트(Cognitive PM-Twin) 기반의 실현가능한 구조적 개선안을 제시합니다."

    summary_replacements = {
        "SLIDE 01": s01_text,
        "SLIDE 02": s02_text,
        "SLIDE 04": s04_text,
        "SLIDE 05": s05_text,
        "SLIDE 11": s11_text,
    }

    for slide in soup.find_all('div', class_='slide-card'):
        num_span = slide.find('span', class_='slide-num')
        if num_span:
            slide_id = num_span.text.strip()
            summary = slide.find('div', class_='slide-summary')
            if summary and slide_id in summary_replacements:
                summary.string = summary_replacements[slide_id]

    # 3. Enhance specific annotations and tables to reflect System Perspective and Logic
    # Update RACI Matrix to highlight System perspective
    for td in soup.find_all('td'):
        if "SDK 연기 책임을 벤더에게 전가" in td.text:
            td.string = "SDK 연기 책임을 벤더에게 전가 (Ownership 결여 및 시스템적 리스크 관리 부재)"
        if "보안부서는 GDPR 위반 우려만 제기" in td.text:
            td.string = "보안부서는 GDPR 위반 우려만 제기 (Silo 현상 - 시스템 관점 거버넌스 미비)"

    # Add Stage 2 Domain mapping to Risk Matrix
    for th in soup.find_all('th'):
        if th.text == "리스크 항목":
            th.string = "리스크 항목 (Performance Domain 매핑)"

    for td in soup.find_all('td'):
        if td.text == "NovaChip SDK 지연으로 인한 핵심 플랫폼 빌드 블락":
            td.string = "NovaChip SDK 지연으로 인한 빌드 블락 [Delivery & Vendor Domain]"
        if td.text == "REQ-045 기습 추가로 인한 기존 요건(UI) 통합 테스트 파손":
            td.string = "REQ-045 기습 추가로 통합 테스트 파손 [Planning & Work Domain]"

    # 4. Extract V3 tools before saving V4
    v3_html_content = [
        "<!DOCTYPE html><html lang='ko'><head><meta charset='utf-8'/><style>",
        soup.find('style').string if soup.find('style') else "",
        "</style></head><body><div class='container'>",
        "<h1>NextGen AutoCockpit Mission - Stage 1&2 Detailed Tools (v3)</h1>",
        "<p>본선 심사 기준(근본원인 논리성, 시스템 관점, 파급효과)을 적용하여 생성된 15개의 진단 도구 로우 데이터입니다.</p>"
    ]

    tool_count = 1
    for slide in soup.find_all('div', class_='slide-card'):
        title_el = slide.find('h2', class_='slide-title')
        if title_el and "디텍팅 도구" in title_el.text:
            card = slide.find('div', class_='card')
            if card:
                v3_html_content.append(f"<h2>Tool {tool_count}: {title_el.text}</h2>")
                v3_html_content.append(str(card))
                tool_count += 1
                
    v3_html_content.append("</div></body></html>")
    
    with open(v3_out, "w", encoding="utf-8") as f:
        f.write("\n".join(v3_html_content))
        
    # 5. Save V4
    with open(v4_out, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    print(f"Generated V3 at {v4_out}")
    print(f"Generated V4 at {v3_out}")

if __name__ == "__main__":
    main()
