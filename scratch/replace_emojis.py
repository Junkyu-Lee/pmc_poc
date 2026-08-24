import re

def main():
    path = r"d:\workspaces\PMC_POC\stage1_stage2_analysis_v4.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Dictionary mapping colorful emojis to monochrome/simple symbols
    replacements = {
        "🚗": "❖",
        "📌": "▪",
        "🎯": "▸",
        "📊": "▪",
        "🕸️": "⛆",
        "🕸": "⛆",
        "🧠": "◈",
        "🚨": "⚠",
        "⚡": "⌁",
        "🔍": "⌕",
        "⚠️": "⚠",
        "✅": "✔",
        "❌": "✘",
        "🤖": "⚙",
        "💡": "⚲",
        "💬": "🗨",
        "🤝": "⟠",
        "📈": "◿",
        "📉": "◺",
        "🛡️": "⛨",
        "🛡": "⛨",
        "🔥": "⏣",
        "🛠️": "⚒",
        "🛠": "⚒",
        "💼": "⧉",
        "🧑‍💻": "👤",
        "👤": "👤",
        "🏆": "⛫",
        "⭐": "★",
        "✨": "✧",
        "📻": "⍾",
    }

    # First explicit replacements
    for k, v in replacements.items():
        content = content.replace(k, v)

    # General fallback for any remaining characters in the emoji blocks
    # Emoticons (1F600-1F64F)
    # Misc Symbols and Pictographs (1F300-1F5FF)
    # Transport and Map (1F680-1F6FF)
    # Supplemental Symbols (1F900-1F9FF)
    
    emoji_pattern = re.compile(r'[\U0001F300-\U0001FAFF]')
    content = emoji_pattern.sub('▪', content)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Emojis replaced successfully.")

if __name__ == "__main__":
    main()
