import markdown
import sys
import codecs

def convert_md_to_html(md_path, html_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    html_content = markdown.markdown(md_text, extensions=['tables', 'fenced_code', 'nl2br'])
    
    template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HERMES 프로젝트 진단 및 AI Agent 개선안</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #f4f7fb;
            --container-bg: #ffffff;
            --text-main: #334155;
            --text-light: #64748b;
            --primary: #3b82f6;
            --primary-light: #eff6ff;
            --danger: #ef4444;
            --danger-light: #fef2f2;
            --warning: #f59e0b;
            --warning-light: #fffbeb;
            --success: #10b981;
            --success-light: #ecfdf5;
            --border: #e2e8f0;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            line-height: 1.7;
            padding: 40px 20px;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            background-color: var(--container-bg);
            padding: 50px 60px;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        }

        h1, h2, h3, h4 {
            color: #0f172a;
            margin-top: 2em;
            margin-bottom: 0.8em;
            line-height: 1.3;
        }

        h1 {
            font-size: 2.2rem;
            text-align: center;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 20px;
            margin-top: 0;
        }

        h2 {
            font-size: 1.7rem;
            color: var(--primary);
            border-left: 5px solid var(--primary);
            padding-left: 15px;
        }

        h3 {
            font-size: 1.3rem;
            color: #1e293b;
            background-color: var(--primary-light);
            padding: 8px 15px;
            border-radius: 8px;
            display: inline-block;
        }

        p {
            margin-bottom: 1.2em;
        }

        ul, ol {
            margin-bottom: 1.5em;
            padding-left: 25px;
        }

        li {
            margin-bottom: 0.5em;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 2em 0;
            background: #fff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.03);
            border-radius: 8px;
            overflow: hidden;
        }

        th, td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }

        th {
            background-color: #f8fafc;
            font-weight: 600;
            color: #475569;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 0.05em;
        }

        tr:last-child td {
            border-bottom: none;
        }

        tr:nth-child(even) {
            background-color: #fcfcfc;
        }

        /* Infographic styled code blocks */
        pre {
            background-color: #1e293b;
            color: #f8fafc;
            padding: 20px;
            border-radius: 12px;
            overflow-x: auto;
            margin: 1.5em 0;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9rem;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
            border: 1px solid #334155;
        }

        code {
            font-family: 'Courier New', Courier, monospace;
            background-color: #f1f5f9;
            color: #ef4444;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.9em;
        }

        pre code {
            background-color: transparent;
            color: inherit;
            padding: 0;
        }

        blockquote {
            background-color: var(--warning-light);
            border-left: 4px solid var(--warning);
            padding: 15px 20px;
            margin: 1.5em 0;
            border-radius: 0 8px 8px 0;
            color: #92400e;
            font-weight: 500;
        }

        hr {
            border: 0;
            height: 1px;
            background: var(--border);
            margin: 3em 0;
        }

        /* Status colors for tables text parsing */
        .status-danger {
            color: var(--danger);
            font-weight: bold;
        }

        .status-warning {
            color: var(--warning);
            font-weight: bold;
        }

        .status-success {
            color: var(--success);
            font-weight: bold;
        }
        
        /* Infographic Badges */
        td:contains('위반'), td:contains('치명'), td:contains('심각') {
            font-weight: bold;
            color: var(--danger);
        }

        @media (max-width: 768px) {
            .container {
                padding: 30px 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Markdown Content Inserted Here -->
        CONTENT_PLACEHOLDER
    </div>
    
    <script>
        // Simple JS to parse table cells and add infographic badges based on keywords
        document.addEventListener('DOMContentLoaded', () => {
            const cells = document.querySelectorAll('td');
            cells.forEach(cell => {
                const text = cell.innerText;
                if (text.includes('위반') || text.includes('치명적') || text.includes('주범') || text.includes('심각') || text.includes('❌') || text.includes('🔴')) {
                    cell.style.color = 'var(--danger)';
                    cell.style.fontWeight = 'bold';
                    cell.style.backgroundColor = 'var(--danger-light)';
                } else if (text.includes('문제') || text.includes('주의') || text.includes('⚠️') || text.includes('🟠')) {
                    cell.style.color = 'var(--warning)';
                    cell.style.fontWeight = 'bold';
                    cell.style.backgroundColor = 'var(--warning-light)';
                } else if (text.includes('건강') || text.includes('정상') || text.includes('✅') || text.includes('🟢')) {
                    cell.style.color = 'var(--success)';
                    cell.style.fontWeight = 'bold';
                    cell.style.backgroundColor = 'var(--success-light)';
                }
            });
        });
    </script>
</body>
</html>"""
    
    final_html = template.replace("CONTENT_PLACEHOLDER", html_content)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"Successfully converted {md_path} to {html_path}")

if __name__ == "__main__":
    convert_md_to_html("HERMES_분석_완결본 1.md", "HERMES_분석_완결본_1_Infographic.html")
