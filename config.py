"""LLM API 설정 모듈"""
import os
from dotenv import load_dotenv

load_dotenv()

# LLM Provider: "claude", "openai", or "gemini"
PROVIDER = os.getenv("LLM_PROVIDER", "claude")

# Claude
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY", "")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-20250514")

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", os.getenv("GOOGLE_API_KEY", ""))
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# Analysis settings
MAX_TOKENS = 8000
TEMPERATURE = 0.3

