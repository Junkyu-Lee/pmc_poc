import sys
import os
import bs4
import copy

sys.stdout.reconfigure(encoding='utf-8')

def main():
    v3_path = r'd:\workspaces\PMC_POC\output\stage1_stage2_analysis_v3.html'
    v4_path = r'd:\workspaces\PMC_POC\stage1_stage2_analysis_v4.html'
    out_path = r'd:\workspaces\PMC_POC\stage1_stage2_analysis_v4.html' # Overwrite as requested
    
    with open(v3_path, 'r', encoding='utf-8') as f:
        v3 = bs4.BeautifulSoup(f.read(), 'html.parser')
        
    with open(v4_path, 'r', encoding='utf-8') as f:
        v4 = bs4.BeautifulSoup(f.read(), 'html.parser')
        
    # --- 1. CSS Updates ---
    style_tag = v4.find('style')
    extra_css = """
  /* Slide height increase */
  .slide-card { min-height: 75vh; display: flex; flex-direction: column; }
  
  /* Slide summary banner */
  .slide-summary {
    font-size: 1.05rem;
    font-weight: 700;
    color: #fff;
    background: rgba(56, 189, 248, 0.1);
    padding: 1rem 1.2rem;
    border-radius: 8px;
    margin-bottom: 1.5rem;
    border-left: 4px solid var(--primary);
  }
  
  /* Missing CSS from v3 */
  .conflict-row { background: rgba(220,53,69,0.08) !important; }
  .conflict-row td { border-color: var(--red); }
  .missing-a { background: rgba(217,119,6,0.08) !important; }
  .legend { display: flex; flex-wrap: wrap; gap: 1rem; margin: 1rem 0; font-size: 0.85rem; }
  .legend-item { display: flex; align-items: center; gap: 0.4rem; }
  .legend-swatch { width: 14px; height: 14px; border-radius: 3px; }
  .annotation { background: var(--accent-light); border-left: 3px solid var(--accent); padding: 0.8rem 1rem; margin: 1rem 0; border-radius: 0 8px 8px 0; font-size: 0.9rem; color: #fff; }
  .annotation.warn { background: rgba(220,53,69,0.15); border-left-color: var(--red); }
  .svg-container { overflow-x: auto; margin: 1rem 0; background: var(--surface-alt); border-radius: 8px; padding: 1rem; text-align: center; }
  .svg-container svg { max-width: 100%; height: auto; }
  
  /* Fix tool card internal bg to match dark theme */
  .card { background: rgba(15, 23, 42, 0.6); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border); overflow-x: auto; flex: 1; }
  .tool-tag-pill { margin-right: 0.5rem; }
"""
    style_tag.append(extra_css)
    
    # --- 2. Add slide summaries to non-problem slides ---
    summaries = {
        "SLIDE 01": "요약: 프로젝트 위기 현황과 5대 핵심 문제의 근본 원인을 식별하고 15개의 실물 도구로 증명합니다.",
        "SLIDE 02": "프로젝트 현황: G3 릴리스 D-15 시점에서 소셜 로그인 기습 반영으로 인한 기술, 품질, 법무적 갈등이 동시다발적으로 발생했습니다.",
        "SLIDE 04": "성과 분석: 응답속도, 오류율, 빌드 성공률 등 주요 KPI가 목표치를 심각하게 미달하고 있습니다.",
        "SLIDE 05": "우선순위: 영향도와 긴급도를 바탕으로 거버넌스 붕괴 및 Scope Creep 등 5대 핵심 문제를 도출했습니다.",
        "SLIDE 11": "결론: PMBOK 8판 체계 미비라는 근본 원인을 확인했으며, 이제 이를 해결할 AI Agentic 시스템(Stage 3) 설계로 넘어갑니다."
    }
    
    for slide in v4.find_all('div', class_='slide-card'):
        num_span = slide.find('span', class_='slide-num')
        if num_span and num_span.text in summaries:
            header = slide.find('div', class_='slide-header')
            summary_div = v4.new_tag('div', **{'class': 'slide-summary'})
            summary_div.string = summaries[num_span.text]
            header.insert_after(summary_div)
            
    # --- 3. Merge Slide 3 (Unexpected Issue) into Slide 2 ---
    s2 = None
    s3 = None
    for slide in v4.find_all('div', class_='slide-card'):
        n = slide.find('span', class_='slide-num')
        if n and n.text == "SLIDE 02": s2 = slide
        if n and n.text == "SLIDE 03": s3 = slide
        
    if s2 and s3:
        # Change S2 Title
        s2_title = s2.find('h2', class_='slide-title')
        s2_title.string = "1. 프로젝트 개요 및 돌발 이슈 (Identify)"
        
        # Move S3 content to S2 (excluding header)
        for child in s3.find_all(recursive=False):
            if 'slide-header' not in child.get('class', []):
                s2.append(child)
        s3.decompose() # Remove slide 3
        
    # --- 4. Replace Abstract Tools with Detailed Tools from v3 ---
    h2s = v3.find_all('h2')
    v3_tools = {
        'raci': h2s[2].find_next_sibling('div', class_='card'),
        'stakeholder': h2s[7].find_next_sibling('div', class_='card'),
        'p1_cause': h2s[6].find_next_sibling('div', class_='card'), # Problem 1 card (5 Whys)
        
        'rtm': h2s[4].find_next_sibling('div', class_='card'),
        'burndown': h2s[13].find_next_sibling('div', class_='card'),
        'p2_cause': h2s[6].find_next_siblings('div', class_='card')[1], # Problem 2 card (Mindset)
        
        'control_chart': h2s[12].find_next_sibling('div', class_='card'),
        'variance': h2s[15].find_next_sibling('div', class_='card'),
        'fishbone': h2s[5].find_next_sibling('div', class_='card'),
        
        'risk_pi': h2s[3].find_next_sibling('div', class_='card'),
        'quant_risk': h2s[10].find_next_sibling('div', class_='card'), # Summary Matrix
        'feedback': h2s[8].find_next_sibling('div', class_='card'),
        
        'causal': h2s[9].find_next_sibling('div', class_='card'),
        'pareto': h2s[14].find_next_sibling('div', class_='card'),
        'trend': h2s[16].find_next_sibling('div', class_='card'),
    }

    problem_mapping = [
        ("SLIDE 06-B", "[문제 1]", [
            ("디텍팅 도구 1 - RACI Matrix", v3_tools['raci']),
            ("디텍팅 도구 2 - Stakeholder Matrix", v3_tools['stakeholder']),
            ("디텍팅 도구 3 - 5 Whys (근본 원인 분석)", v3_tools['p1_cause'])
        ]),
        ("SLIDE 07-B", "[문제 2]", [
            ("디텍팅 도구 1 - 요구사항 의존성 그래프 (RTM)", v3_tools['rtm']),
            ("디텍팅 도구 2 - Sprint 4 Burndown Chart", v3_tools['burndown']),
            ("디텍팅 도구 3 - Mindset Mapping", v3_tools['p2_cause'])
        ]),
        ("SLIDE 08-B", "[문제 3]", [
            ("디텍팅 도구 1 - Control Chart (관리도)", v3_tools['control_chart']),
            ("디텍팅 도구 2 - Variance Analysis", v3_tools['variance']),
            ("디텍팅 도구 3 - Fishbone Diagram", v3_tools['fishbone'])
        ]),
        ("SLIDE 09-B", "[문제 4]", [
            ("디텍팅 도구 1 - Risk P-I Matrix", v3_tools['risk_pi']),
            ("디텍팅 도구 2 - Summary Matrix (Quant Risk)", v3_tools['quant_risk']),
            ("디텍팅 도구 3 - Feedback Loop", v3_tools['feedback'])
        ]),
        ("SLIDE 10-B", "[문제 5]", [
            ("디텍팅 도구 1 - Causal Relationship Map", v3_tools['causal']),
            ("디텍팅 도구 2 - Pareto Chart", v3_tools['pareto']),
            ("디텍팅 도구 3 - Trend Analysis", v3_tools['trend'])
        ])
    ]

    for slide_id, prob_title, tools in problem_mapping:
        # Find the original B slide
        orig_slide = None
        for slide in v4.find_all('div', class_='slide-card'):
            num_span = slide.find('span', class_='slide-num')
            if num_span and num_span.text == slide_id:
                orig_slide = slide
                break
                
        if not orig_slide: continue
        
        # Create 3 new slides to replace it
        new_slides = []
        for idx, (tool_title, tool_html) in enumerate(tools, 1):
            new_slide = v4.new_tag('div', **{'class': 'slide-card'})
            
            header = v4.new_tag('div', **{'class': 'slide-header'})
            title = v4.new_tag('h2', **{'class': 'slide-title'})
            title.string = f"📊 {prob_title} {tool_title}"
            num = v4.new_tag('span', **{'class': 'slide-num'})
            num.string = f"{slide_id.split('-')[0]}-B{idx}"
            
            header.append(title)
            header.append(num)
            new_slide.append(header)
            
            if tool_html:
                # Need to copy it so we don't move the original reference
                tool_clone = copy.copy(tool_html)
                new_slide.append(tool_clone)
            
            new_slides.append(new_slide)
            
        # Insert new slides after original, then remove original
        curr = orig_slide
        for ns in new_slides:
            curr.insert_after(ns)
            curr = ns
        orig_slide.decompose()
        
    # --- 5. Save the updated v4 ---
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(str(v4))
        
    print(f"Successfully updated {out_path}")

if __name__ == '__main__':
    main()
