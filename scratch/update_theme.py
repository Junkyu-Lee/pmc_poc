import re

def main():
    path = r"d:\workspaces\PMC_POC\stage1_stage2_analysis_v4.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_css = """<style>
  :root {
    --bg: #f8f9fa;
    --surface: #ffffff;
    --surface-alt: #f1f5f9;
    --primary: #0284c7;
    --primary-dark: #0369a1;
    --accent: #7e22ce;
    --accent-light: #9333ea;
    --red: #e11d48;
    --red-light: #fda4af;
    --orange: #ea580c;
    --yellow: #ca8a04;
    --green: #16a34a;
    --text: #1e293b;
    --text-muted: #64748b;
    --border: #cbd5e1;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background-color: var(--bg);
    color: var(--text);
    line-height: 1.6;
    padding: 2rem;
  }
  .container { max-width: 1400px; margin: 0 auto; }
  
  header {
    background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 50%, #e2e8f0 100%);
    padding: 2.5rem;
    border-radius: 16px;
    border: 1px solid rgba(147, 51, 234, 0.3);
    margin-bottom: 2.5rem;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
  }
  header h1 { font-size: 2.2rem; font-weight: 800; color: var(--text); margin-bottom: 0.5rem; }
  header .subtitle { font-size: 1.1rem; color: var(--primary); font-weight: 600; }
  .badge-deck { display: flex; gap: 0.8rem; flex-wrap: wrap; margin-top: 1.2rem; }
  .badge {
    padding: 0.35rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .badge-purple { background: rgba(147, 51, 234, 0.1); color: var(--accent); border: 1px solid var(--accent); }
  .badge-blue { background: rgba(2, 132, 199, 0.1); color: var(--primary); border: 1px solid var(--primary); }
  .badge-red { background: rgba(225, 29, 72, 0.1); color: var(--red); border: 1px solid var(--red); }
  .badge-orange { background: rgba(234, 88, 12, 0.1); color: var(--orange); border: 1px solid var(--orange); }
  .badge-green { background: rgba(22, 163, 74, 0.1); color: var(--green); border: 1px solid var(--green); }
  
  .slide-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
    min-height: 75vh;
    display: flex;
    flex-direction: column;
  }
  .slide-card:hover { border-color: var(--primary); }
  .slide-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid var(--border);
    padding-bottom: 1rem;
    margin-bottom: 1.5rem;
  }
  .slide-title { font-size: 1.4rem; font-weight: 700; color: var(--primary); display: flex; align-items: center; gap: 0.6rem; }
  .slide-num {
    background: var(--surface-alt);
    color: var(--text-muted);
    padding: 0.2rem 0.6rem;
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: 700;
  }
  
  .slide-summary {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text);
    background: rgba(2, 132, 199, 0.05);
    padding: 1rem 1.2rem;
    border-radius: 8px;
    margin-bottom: 1.5rem;
    border-left: 4px solid var(--primary);
  }

  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
  .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.5rem; }
  .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; }
  
  @media (max-width: 1024px) {
    .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    font-size: 0.92rem;
  }
  th, td {
    padding: 0.75rem 1rem;
    text-align: left;
    border-bottom: 1px solid var(--border);
  }
  th { background: var(--surface-alt); color: var(--primary); font-weight: 700; }
  tr:hover { background: rgba(0,0,0,0.02); }
  
  .card {
    background: rgba(248, 249, 250, 0.8);
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid var(--border);
    overflow-x: auto;
    flex: 1;
  }

  .card-title { font-size: 1.15rem; font-weight: 700; color: var(--accent); margin-bottom: 1rem; }
  .highlight-red { color: var(--red); font-weight: 700; }
  .highlight-green { color: var(--green); font-weight: 700; }
  .highlight-yellow { color: var(--yellow); font-weight: 700; }

  .progress-bar-bg { background: var(--border); height: 10px; border-radius: 5px; overflow: hidden; }
  .progress-bar-fill { height: 100%; background: linear-gradient(90deg, var(--primary), var(--accent)); }
  .progress-bar-fill.red { background: linear-gradient(90deg, var(--orange), var(--red)); }

  .annotation {
    background: rgba(147, 51, 234, 0.08);
    border-left: 4px solid var(--accent);
    padding: 0.9rem 1.2rem;
    margin: 1rem 0;
    border-radius: 0 8px 8px 0;
    font-size: 0.92rem;
    color: var(--text);
  }
  .annotation.warn {
    background: rgba(225, 29, 72, 0.08);
    border-left-color: var(--red);
  }

  .svg-container { overflow-x: auto; margin: 1rem 0; background: var(--surface-alt); border-radius: 8px; padding: 1rem; text-align: center; }
  .svg-container svg { max-width: 100%; height: auto; }

  .tool-tag-pill {
    display: inline-block;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 700;
    margin-right: 0.4rem;
  }
  .tag-critical { background: rgba(225,29,72,0.1); color: var(--red); border: 1px solid var(--red); }
  .tag-warning { background: rgba(234,88,12,0.1); color: var(--orange); border: 1px solid var(--orange); }
  .tag-info { background: rgba(2,132,199,0.1); color: var(--primary); border: 1px solid var(--primary); }
</style>"""

    # Use regex to replace everything between <style> and </style>
    new_content = re.sub(r'<style>.*?</style>', new_css, content, flags=re.DOTALL)
    
    # SVG font and stroke updates that might have been hardcoded for dark mode
    new_content = new_content.replace('fill="#fff"', 'fill="#1e293b"')
    new_content = new_content.replace('fill="#f8fafc"', 'fill="#1e293b"')
    new_content = new_content.replace('fill="#0f172a"', 'fill="#ffffff"') # if dark backgrounds in svg
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    main()
