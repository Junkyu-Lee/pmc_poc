import sys
import bs4

sys.stdout.reconfigure(encoding='utf-8')

def main():
    v4_path = r'd:\workspaces\PMC_POC\stage1_stage2_analysis_v4.html'
    
    with open(v4_path, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        
    span = soup.find(lambda tag: tag.name == 'span' and 'SLIDE 05' in tag.text)
    if not span:
        print("SLIDE 05 not found")
        return
        
    slide = span.find_parent('div', class_='slide-card')
    table = slide.find('table')
    
    # Let's create a new table body
    tbody = table.find('tbody')
    tbody.clear()
    
    rows_data = [
        # Rank 1-5 (Core Problems)
        ("Rank 1", "거버넌스 붕괴 & 권한/스폰서십 비공식 변경", "High", "Critical", "RACI Matrix, Stakeholder Matrix, 5 Whys", True),
        ("Rank 2", "요구사항 변경 통제 미비 & Scope Creep", "High", "Critical", "RTM Matrix, Burndown Chart, Mindset Mapping", True),
        ("Rank 3", "검증/품질 보증 파이프라인 붕괴", "High", "High", "Control Chart, Variance Analysis, Fishbone", True),
        ("Rank 4", "법무/보안 규제 준수(Compliance) 리스크", "High", "High", "Risk P-I Matrix, Quant Risk Impact, Feedback Loop", True),
        ("Rank 5", "팀 간 R&R 대립 및 조직 사기 저하", "Medium", "High", "Causal Map, Pareto Chart, Trend Analysis", True),
        # Rank 6-10 (Minor Problems)
        ("Rank 6", "외부 파트너(NebulaWorks) 인증 연동 협업 및 소통 지연", "Medium", "Medium", "Communication Plan (본 보고서 범위 외)", False),
        ("Rank 7", "마케팅 캠페인 일정과 개발 마일스톤 간의 인식 미스얼라인", "Medium", "Low", "Milestone Roadmap (본 보고서 범위 외)", False),
        ("Rank 8", "개발팀 및 QA팀 잦은 야근으로 인한 단기 피로도 누적", "Low", "Medium", "Resource Histogram (본 보고서 범위 외)", False),
        ("Rank 9", "초기 애자일 테일러링 미흡에 따른 산출물(문서화) 부채", "Low", "Medium", "Tech Debt Log (본 보고서 범위 외)", False),
        ("Rank 10", "일부 비핵심 UI 컴포넌트에 대한 테스트 자동화 커버리지 저조", "Low", "Low", "Test Coverage Report (본 보고서 범위 외)", False),
    ]
    
    # Also change table header "선정된 핵심 문제명" to "식별된 문제명 (Problem Statement)"
    thead = table.find('thead')
    th_title = thead.find_all('th')[1]
    th_title.string = "식별된 문제명 (Problem Statement)"
    
    for rank, title, urgency, impact, tools, is_core in rows_data:
        tr = soup.new_tag('tr')
        
        # Rank
        td_rank = soup.new_tag('td')
        if is_core:
            strong = soup.new_tag('strong')
            strong.string = rank
            td_rank.append(strong)
        else:
            td_rank.string = rank
            td_rank['style'] = "color: var(--text-muted);"
            
        # Title
        td_title = soup.new_tag('td')
        td_title.string = title
        if is_core:
            td_title['style'] = "color: var(--orange); font-weight: 700;"
        else:
            td_title['style'] = "color: var(--text-muted);"
            
        # Urgency
        td_urgency = soup.new_tag('td')
        td_urgency.string = urgency
        if not is_core: td_urgency['style'] = "color: var(--text-muted);"
        
        # Impact
        td_impact = soup.new_tag('td')
        td_impact.string = impact
        if not is_core: td_impact['style'] = "color: var(--text-muted);"
        
        # Tools
        td_tools = soup.new_tag('td')
        if is_core:
            strong_tools = soup.new_tag('strong')
            strong_tools.string = tools
            td_tools.append(strong_tools)
        else:
            td_tools.string = tools
            td_tools['style'] = "color: var(--text-muted); font-size: 0.85em;"
            
        tr.append(td_rank)
        tr.append(td_title)
        tr.append(td_urgency)
        tr.append(td_impact)
        tr.append(td_tools)
        
        tbody.append(tr)
        
    with open(v4_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Successfully updated SLIDE 05")

if __name__ == '__main__':
    main()
