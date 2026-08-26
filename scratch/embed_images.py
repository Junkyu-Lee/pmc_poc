import sys
import base64
import bs4

sys.stdout.reconfigure(encoding='utf-8')

def get_base64(filepath):
    with open(filepath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/png;base64,{encoded_string}"

def main():
    v4_path = r'd:\workspaces\PMC_POC\stage1_stage2_analysis_v4.html'
    
    with open(v4_path, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and src.startswith('./images/'):
            # Path is relative to d:\workspaces\PMC_POC
            actual_path = r'd:\workspaces\PMC_POC' + src[1:].replace('/', '\\')
            try:
                b64_src = get_base64(actual_path)
                img['src'] = b64_src
            except Exception as e:
                print(f"Failed to process {actual_path}: {e}")

    with open(v4_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print(f"Successfully embedded images as base64 in {v4_path}")

if __name__ == '__main__':
    main()
