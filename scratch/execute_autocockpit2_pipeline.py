import os
import bs4

def generate_htmls():
    v4_template = r"d:\workspaces\PMC_POC\stage1_stage2_analysis_v4.html"
    poc_ppt = r"d:\workspaces\PMC_POC\output\poc_ppt.html"
    
    out_v3 = r"d:\workspaces\PMC_POC\output\AutoCockpit2_stage1_stage2_analysis_v3.html"
    out_v4 = r"d:\workspaces\PMC_POC\output\AutoCockpit2_stage1_stage2_analysis_v4.html"
    out_v5 = r"d:\workspaces\PMC_POC\output\AutoCockpit2_stage1_stage2_analysis_v5.html"

    os.makedirs(os.path.dirname(out_v3), exist_ok=True)

    # --- 1. Read v4 template ---
    with open(v4_template, "r", encoding="utf-8") as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')

    # --- 2. Create V3 Data (20 Tools) ---
    v3_content = [
        "<!DOCTYPE html><html lang='ko'><head><meta charset='utf-8'/><style>",
        soup.find('style').string if soup.find('style') else "",
        "</style></head><body><div class='container'>",
        "<h1>AutoCockpit2 - Detailed Tools (v3)</h1>",
        "<p>20 PMBOK Problem Detecting & Analysis Tools</p>"
    ]
    
    tools = [
        "KPI Gap Analysis", "RTM", "RACI", "Risk Matrix", "Symptom Mapping",
        "Impact-Urgency Matrix", "EVM", "Variance Analysis", "5 Whys", "Fishbone",
        "Mindset Mapping", "Performance Domain Mapping", "Stakeholder Matrix", "Feedback Loop",
        "Causal Map", "Quant Risk", "Control Chart", "Burndown", "Pareto", "Trend Analysis"
    ]
    
    for i, tool in enumerate(tools, 1):
        v3_content.append(f"<div class='slide-card'><h2 class='slide-title'>Tool {i}: {tool}</h2>")
        v3_content.append(f"<div class='card'><p>Detailed generated mock data for {tool} in AutoCockpit2 context.</p></div></div>")
        
    v3_content.append("</div></body></html>")
    
    with open(out_v3, "w", encoding="utf-8") as f:
        f.write("\n".join(v3_content))

    # --- 3. Modify V4 template for AutoCockpit2 ---
    title = soup.find('title')
    if title: title.string = "AutoCockpit2 — 종합 진단 보고서 (v4)"
    
    header_title = soup.find('h1')
    if header_title: header_title.string = "❖ AutoCockpit2 프로젝트 심층 진단"

    summaries = {
        "SLIDE 01": "요약: [Stage 1] 명확한 이상징후 식별 및 [Stage 2] Performance Domain 간 다차원적 파급효과 시뮬레이션을 통해, 시스템 관점의 5대 핵심 근본 원인을 도출합니다.",
        "SLIDE 02": "프로젝트 현황: 소셜 로그인 기습 반영(Scope Creep) 및 SDK 지연이라는 징후를 명확하게 포착하고, 거버넌스 붕괴라는 시스템적 결함을 도출했습니다.",
        "SLIDE 04": "파급효과 분석: 응답속도, 오류율 등 주요 KPI 미달이 [Delivery Domain]과 [Development Approach]에 미치는 파급효과를 심층 분석했습니다.",
        "SLIDE 05": "우선순위: 표면적 증상이 아닌 근본 원인을 파악하고, Proactive 마인드셋에 입각하여 리콜 손실을 방어하기 위한 Top 5 과제를 식별합니다.",
        "SLIDE 11": "결론: Proactive, Ownership, Value-driven 3대 마인드셋을 적용하여, 실현가능한 구조적 개선안을 제시합니다."
    }

    for slide in soup.find_all('div', class_='slide-card'):
        num_span = slide.find('span', class_='slide-num')
        if num_span:
            slide_id = num_span.text.strip()
            summary = slide.find('div', class_='slide-summary')
            if summary and slide_id in summaries:
                summary.string = summaries[slide_id]

    with open(out_v4, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    # --- 4. Generate V5 (V4 + POC) ---
    with open(poc_ppt, "r", encoding="utf-8") as f:
        poc_soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        
    v4_body = soup.find('body')
    v4_container = v4_body.find('div', class_='container')
    
    # Extract poc content
    poc_container = poc_soup.find('div', class_='container')
    if poc_container:
        # Create a visual separator
        separator = poc_soup.new_tag("div")
        separator['style'] = "margin: 4rem 0; border-top: 4px dashed #38bdf8; text-align: center; padding-top: 2rem;"
        h1 = poc_soup.new_tag("h1")
        h1['style'] = "color: #38bdf8; font-size: 2.5rem;"
        h1.string = "🔽 Stage ③ & ④ : Agentic POC Integration 🔽"
        separator.append(h1)
        v4_container.append(separator)
        
        for element in poc_container.find_all('div', class_='slide-card', recursive=False):
            v4_container.append(element)
            
    v5_title = soup.find('title')
    if v5_title: v5_title.string = "AutoCockpit2 — 통합 보고서 (v5)"
            
    with open(out_v5, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"Generated V3 at {out_v3}")
    print(f"Generated V4 at {out_v4}")
    print(f"Generated V5 at {out_v5}")

if __name__ == "__main__":
    generate_htmls()
