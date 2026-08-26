import codecs
import markdownify

def html_to_md(html_file, md_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    md = markdownify.markdownify(html, heading_style="ATX", default_title=True)

    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md.strip() + "\n")

if __name__ == "__main__":
    html_to_md("output/poc_ppt.html", "output/poc_ppt.md")
