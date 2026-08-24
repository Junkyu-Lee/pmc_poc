import sys
import bs4

sys.stdout.reconfigure(encoding='utf-8')

svg_code = """
<div class="svg-container" style="background: rgba(15, 23, 42, 0.4); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
    <svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 0 L 10 5 L 0 10 z" fill="#8a8780" />
            </marker>
            <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
                <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.3"/>
            </filter>
        </defs>

        <!-- Edges -->
        <!-- N1 to N3 -->
        <path d="M 300 75 Q 150 75 150 190" fill="none" stroke="#8a8780" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#arrow)" />
        <text x="180" y="110" font-size="12" fill="#a8a5a0" font-weight="500">변경 통제 없이 범위 증가</text>

        <!-- N1 to N2 -->
        <path d="M 500 75 Q 650 75 650 190" fill="none" stroke="#8a8780" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#arrow)" />
        <text x="600" y="110" font-size="12" fill="#a8a5a0" font-weight="500">의사결정 체계 붕괴</text>

        <!-- N2 to N3 -->
        <path d="M 550 225 L 260 225" fill="none" stroke="#dc3545" stroke-width="2.5" marker-end="url(#arrow)" />
        <text x="400" y="215" font-size="12" fill="#f87171" text-anchor="middle" font-weight="700">품질 저하 유발</text>

        <!-- N3 to N4 -->
        <path d="M 150 250 L 150 340" fill="none" stroke="#8a8780" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#arrow)" />
        <text x="160" y="300" font-size="12" fill="#a8a5a0" font-weight="500">벤더 연동 지연</text>

        <!-- N4 to N5 -->
        <path d="M 250 375 Q 250 425 290 425" fill="none" stroke="#8a8780" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#arrow)" />
        <text x="210" y="410" font-size="12" fill="#a8a5a0" font-weight="500">과부하 누적</text>

        <!-- N2 to N5 -->
        <path d="M 650 250 Q 650 425 510 425" fill="none" stroke="#8a8780" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#arrow)" />
        <text x="610" y="360" font-size="12" fill="#a8a5a0" font-weight="500">책임 전가 및 갈등</text>

        <!-- Nodes -->
        <!-- N1 -->
        <rect x="300" y="50" width="200" height="50" rx="8" fill="#d97706" filter="url(#shadow)" />
        <text x="400" y="80" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="700">#1 거버넌스 부재 (Root)</text>

        <!-- N2 -->
        <rect x="550" y="200" width="200" height="50" rx="8" fill="#2563eb" filter="url(#shadow)" />
        <text x="650" y="230" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="700">#2 이해관계자 정렬 실패</text>

        <!-- N3 -->
        <rect x="50" y="200" width="200" height="50" rx="8" fill="#dc3545" filter="url(#shadow)" />
        <text x="150" y="230" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="700">#3 기술 부채/품질 미달</text>

        <!-- N4 -->
        <rect x="50" y="350" width="200" height="50" rx="8" fill="#16a34a" filter="url(#shadow)" />
        <text x="150" y="380" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="700">#4 벤더 컴플라이언스 실패</text>

        <!-- N5 -->
        <rect x="300" y="400" width="200" height="50" rx="8" fill="#7c3aed" filter="url(#shadow)" />
        <text x="400" y="430" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="700">#5 팀 사기/신뢰 붕괴</text>
    </svg>
</div>
"""

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = bs4.BeautifulSoup(f.read(), 'html.parser')
            
        # Find the Causal Relationship Map section
        # In v3 it's an <h2> containing "Causal Relationship Map"
        # In v4 it's an <h2> containing "Causal Relationship Map" inside a slide
        target = None
        for h2 in soup.find_all('h2'):
            if 'Causal Relationship Map' in h2.get_text():
                target = h2
                break
                
        if not target:
            print(f"Target not found in {filepath}")
            return False
            
        container = target.find_parent('div', class_='slide-card')
        if not container:
            container = target.find_next_sibling('div', class_='card')
            
        if container:
            pre_div = container.find('pre')
            if pre_div:
                wrapper_div = pre_div.find_parent('div')
                if wrapper_div and 'overflow-x:auto' in wrapper_div.get('style', ''):
                    # Replace the wrapper div with the new SVG
                    new_svg = bs4.BeautifulSoup(svg_code, 'html.parser')
                    wrapper_div.replace_with(new_svg)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                    print(f"Successfully updated Causal Map in {filepath}")
                    return True
        print(f"Could not find <pre> block in {filepath}")
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    v3_path = r'd:\workspaces\PMC_POC\output\stage1_stage2_analysis_v3.html'
    v4_path = r'd:\workspaces\PMC_POC\stage1_stage2_analysis_v4.html'
    
    update_file(v3_path)
    update_file(v4_path)

if __name__ == '__main__':
    main()
