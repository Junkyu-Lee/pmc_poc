import sys
import os
import bs4

sys.stdout.reconfigure(encoding='utf-8')

def main():
    v4_path = r'd:\workspaces\PMC_POC\stage1_stage2_analysis_v4.html'
    out_path = r'd:\workspaces\PMC_POC\stage1_stage2_analysis_v4.html'
    
    with open(v4_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    # 1. Remove "PMBOK 8판" entirely
    # It might have spaces around it. Let's do exact replace first, then clean up double spaces.
    html_content = html_content.replace("PMBOK 8판 ", "")
    html_content = html_content.replace("PMBOK 8판", "")
    
    soup = bs4.BeautifulSoup(html_content, 'html.parser')
    
    # 2. Add images to the 5 problem analysis slides
    images = {
        "[문제 1]": "./images/problem1_governance_1787390103859.png",
        "[문제 2]": "./images/problem2_scopecreep_1787390118039.png",
        "[문제 3]": "./images/problem3_quality_1787390131864.png",
        "[문제 4]": "./images/problem4_compliance_1787390146452.png",
        "[문제 5]": "./images/problem5_conflict_1787390160094.png"
    }
    
    for slide in soup.find_all('div', class_='slide-card'):
        title_tag = slide.find('h2', class_='slide-title')
        if not title_tag: continue
        title = title_tag.get_text()
        
        if "(분석)" in title:
            # Determine which problem it is
            for key, img_path in images.items():
                if key in title:
                    # Append the image at the bottom of the slide-card
                    # Create an image container for aesthetic
                    img_container = soup.new_tag('div', style="margin-top: 1.5rem; flex: 1; display: flex; align-items: center; justify-content: center; overflow: hidden; border-radius: 8px; border: 1px solid var(--border); box-shadow: 0 4px 6px rgba(0,0,0,0.3);")
                    img = soup.new_tag('img', src=img_path, style="width: 100%; height: 100%; object-fit: cover; max-height: 380px; filter: brightness(0.9) contrast(1.1);")
                    img_container.append(img)
                    slide.append(img_container)
                    break

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print(f"Successfully modified {out_path}")

if __name__ == '__main__':
    main()
