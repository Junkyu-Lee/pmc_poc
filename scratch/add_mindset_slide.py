import sys
import bs4

sys.stdout.reconfigure(encoding='utf-8')

def main():
    v4_path = r'd:\workspaces\PMC_POC\stage1_stage2_analysis_v4.html'
    
    with open(v4_path, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        
    # Find current SLIDE 11 (Bridge)
    bridge_slide = None
    for slide in soup.find_all('div', class_='slide-card'):
        num = slide.find('span', class_='slide-num')
        if num and 'SLIDE 11' in num.text:
            bridge_slide = slide
            break
            
    if not bridge_slide:
        print("Could not find SLIDE 11")
        return
        
    # Change current SLIDE 11 to SLIDE 12
    bridge_num = bridge_slide.find('span', class_='slide-num')
    bridge_num.string = 'SLIDE 12'
    
    # Create new SLIDE 11 (Mindset Summary)
    new_slide_html = """
    <div class="slide-card" style="min-height: 75vh; display: flex; flex-direction: column;">
        <div class="slide-header">
            <h2 class="slide-title">4. Mindset 기반 근본 원인 종합 분석 (Synthesis)</h2>
            <span class="slide-num">SLIDE 11</span>
        </div>
        <div class="slide-summary">
            종합: 단순히 표면적 증상을 나열하는 것에 그치지 않고, 5대 문제의 기저에 깔린 핵심 Mindset 결핍을 식별했습니다.
        </div>
        
        <div style="flex: 1; display: flex; flex-direction: column; gap: 1rem;">
            <!-- Grid for Mindset Mapping -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                
                <div class="card" style="border-top: 4px solid var(--orange);">
                    <h3 style="color: var(--orange); margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
                        <span style="font-size: 1.5rem;">⚖️</span> Stewardship & Systems Thinking
                    </h3>
                    <p style="font-size: 0.95rem; margin-bottom: 1rem; color: var(--text-light);">
                        [문제 1] 거버넌스 붕괴
                    </p>
                    <p style="font-size: 0.9rem;">
                        개별 기능(소셜 로그인)의 단기적 구현에 매몰되어 전체 시스템 아키텍처와 통합 일정에 미치는 파급 효과를 간과했습니다. 
                        스폰서십과 책임 의식(Stewardship)의 부재가 공식적인 변경 통제 시스템의 마비로 이어졌습니다.
                    </p>
                </div>

                <div class="card" style="border-top: 4px solid var(--blue);">
                    <h3 style="color: var(--blue); margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
                        <span style="font-size: 1.5rem;">🤝</span> Stakeholder & Collaborative Leadership
                    </h3>
                    <p style="font-size: 0.95rem; margin-bottom: 1rem; color: var(--text-light);">
                        [문제 2, 5] Scope Creep & 팀 간 갈등
                    </p>
                    <p style="font-size: 0.9rem;">
                        마케팅(AdVantage)과 개발/QA 간의 목표 불일치 현상입니다. 
                        이해관계자의 요구를 투명하게 조율하는 협업적 리더십이 부재하여, 부서 간 R&R 핑퐁 게임과 사기 저하라는 구조적 갈등으로 번졌습니다.
                    </p>
                </div>

                <div class="card" style="border-top: 4px solid var(--red);">
                    <h3 style="color: var(--red); margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
                        <span style="font-size: 1.5rem;">⚙️</span> Quality & Complexity
                    </h3>
                    <p style="font-size: 0.95rem; margin-bottom: 1rem; color: var(--text-light);">
                        [문제 3] 품질 보증 파이프라인 붕괴
                    </p>
                    <p style="font-size: 0.9rem;">
                        일정 압박 속에서 품질(Quality)을 타협 가능한 트레이드오프로 취급했습니다. 
                        결과적으로 코드 병합 충돌과 테스트 매트릭스의 폭발적 증가라는 시스템 복잡성(Complexity)을 통제하지 못하게 되었습니다.
                    </p>
                </div>

                <div class="card" style="border-top: 4px solid var(--green);">
                    <h3 style="color: var(--green); margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
                        <span style="font-size: 1.5rem;">🛡️</span> Risk & Adaptability
                    </h3>
                    <p style="font-size: 0.95rem; margin-bottom: 1rem; color: var(--text-light);">
                        [문제 4] Compliance 리스크
                    </p>
                    <p style="font-size: 0.9rem;">
                        기능 출시에 눈이 멀어 법적/보안적 규제 환경에 대한 리스크 인식이 결여되었습니다. 
                        초기 기획 변경에 유연하게 대응(Adaptability)하면서도 필수적인 컴플라이언스 게이트를 지켜내는 프로세스 복원력이 부족했습니다.
                    </p>
                </div>

            </div>
            
            <div class="annotation" style="border-left-color: var(--accent); background: rgba(30, 64, 175, 0.2); margin-top: auto;">
                <strong>💡 최종 시사점:</strong> 위 5가지 문제는 독립적으로 발생한 것이 아닙니다. 
                결국 <strong>'테일러링(Tailoring)된 거버넌스의 부재'</strong>라는 하나의 거대한 뿌리에서 파생된 증상들이며, 
                이러한 복합적 위기를 타개하기 위해서는 단편적 조치가 아닌 <strong>AI Agentic 시스템을 통한 구조적 통제망 복원(Stage 3)</strong>이 필수적입니다.
            </div>
        </div>
    </div>
    """
    
    new_slide = bs4.BeautifulSoup(new_slide_html, 'html.parser')
    bridge_slide.insert_before(new_slide)
    
    with open(v4_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Successfully added Mindset Synthesis slide (SLIDE 11)")

if __name__ == '__main__':
    main()
