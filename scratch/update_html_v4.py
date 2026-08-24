import bs4
import re

v4_path = r'd:\workspaces\PMC_POC\output\NextGen_AutoCockpit_stage1_stage2_analysis_v4.html'

with open(v4_path, 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f.read(), 'html.parser')

# 1. Remove SLIDE ##: from titles and remove slide-num spans
for h2 in soup.find_all('h2', class_='slide-title'):
    text = h2.get_text()
    new_text = re.sub(r'SLIDE \d+(-[A-Z0-9]+)?:\s*', '', text)
    new_text = re.sub(r'\[문제 \d+\]\s*', '', new_text) # Also remove [문제 1] if it exists in the title
    if new_text != text:
        h2.string = new_text

for span in soup.find_all('span', class_='slide-num'):
    span.decompose()

# 2. Modify Task Flow 3,4,5
# Find the card with "본선 과제 5대 수행 임무"
task_card = None
for div in soup.find_all('div', class_='card-title'):
    if '5대 수행 임무' in div.get_text():
        task_card = div.parent
        break

if task_card:
    ul = task_card.find('ul')
    if ul:
        lis = ul.find_all('li')
        if len(lis) >= 5:
            # Modify 1, 2 slightly if needed, but user just said "1,2단계만 해당해"
            # So we can keep 1 and 2 as is, but maybe add a note.
            # Replace 3, 4, 5
            lis[2].decompose()
            lis[3].decompose()
            lis[4].decompose()
            
            new_li = soup.new_tag('li', style="margin-bottom: 0.8rem; color: var(--text-muted);")
            new_b = soup.new_tag('b')
            new_b.string = "③ [Design], ④ [Develop], ⑤ [Validate]: "
            new_li.append(new_b)
            new_li.append("추후 AI Agentic PoC를 개발하여 데모하는 단계에서 수행 예정")
            ul.append(new_li)

# 3. Create Cover Slide and remove header
header = soup.find('header')
if header:
    cover_div = soup.new_tag('div', **{'class': 'slide-card cover-slide', 'style': 'display:flex; flex-direction:column; justify-content:center; align-items:center; min-height: 80vh; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311b92 100%); border: 1px solid rgba(168, 85, 247, 0.4); text-align:center; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);'})
    
    h1 = soup.new_tag('h1', style="font-size: 3.5rem; font-weight: 900; color: #fff; margin-bottom: 2rem; line-height: 1.3;")
    h1.append("NextGen AutoCockpit 프로젝트 진단")
    h1.append(soup.new_tag('br'))
    h1.append("및 AI 에이전틱 종합 리포트")
    
    h2_team = soup.new_tag('h2', style="font-size: 2rem; color: var(--primary); font-weight: 700; letter-spacing: 2px;")
    h2_team.string = "PM Transformers"
    
    cover_div.append(h1)
    cover_div.append(h2_team)
    
    header.replace_with(cover_div)

with open(v4_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Modifications applied successfully.")
