import sys
import base64
import bs4
import glob
import os

sys.stdout.reconfigure(encoding='utf-8')

def get_base64(filepath):
    with open(filepath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/png;base64,{encoded_string}"

def main():
    v4_path = r'd:\workspaces\PMC_POC\output\NextGen_AutoCockpit_stage1_stage2_analysis_v4.html'
    
    with open(v4_path, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        
    # Get the latest generated images from the brain directory
    brain_dir = r"C:\Users\user\.gemini\antigravity-ide\brain\b10f93f8-4606-487a-80a6-6a0451f7c31c"
    
    def get_latest_img(prefix):
        files = glob.glob(os.path.join(brain_dir, f"{prefix}_*.png"))
        if not files: return None
        return max(files, key=os.path.getmtime)
        
    images = [
        get_latest_img("prob1_abstract"),
        get_latest_img("prob2_abstract"),
        get_latest_img("prob3_abstract"),
        get_latest_img("prob4_abstract"),
        get_latest_img("prob5_abstract"),
    ]
    
    img_tags = soup.find_all('img')
    
    if len(img_tags) != 5:
        print(f"Expected 5 images, found {len(img_tags)}")
        return
        
    for i, img in enumerate(img_tags):
        if not images[i]:
            print(f"Missing image for problem {i+1}")
            continue
            
        # Update Base64 Source
        img['src'] = get_base64(images[i])
        
        # Update Image Style (Square, Fixed Size)
        img['style'] = "width: 400px; height: 400px; max-width: 100%; object-fit: cover; border-radius: 12px; border: 1px solid var(--border); box-shadow: 0 4px 12px rgba(0,0,0,0.4);"
        
        # Update Parent Div Style (Centered, No background stretching)
        parent = img.parent
        if parent and parent.name == 'div':
            parent['style'] = "margin-top: 2.5rem; display: flex; align-items: center; justify-content: center; padding-bottom: 2rem;"

    with open(v4_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Successfully replaced with abstract square images.")

if __name__ == '__main__':
    main()
