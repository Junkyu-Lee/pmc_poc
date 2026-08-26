"""
핵심 분석 모듈 - LLM을 활용한 프로젝트 시나리오 분석

4단계 체인 LLM 호출을 통해 프로젝트 시나리오를 분석하고 구조화된 JSON을 생성합니다.
"""

import json
import re
import sys
import time
from pathlib import Path

# 부모 디렉토리에서 config 임포트
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config


def _extract_json(text: str) -> dict:
    """LLM 응답에서 JSON을 추출합니다. 마크다운 코드블록 래핑도 처리합니다."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # 마크다운 코드블록에서 JSON 추출 시도
    match = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    # 중괄호 기반 추출
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group(0))
    raise ValueError(f"JSON 파싱 실패: {text[:200]}")


def call_llm(system_prompt: str, user_prompt: str, provider: str = None, api_key: str = None, model: str = None) -> str:
    """LLM API를 호출합니다. Claude, OpenAI, 또는 Gemini를 지원합니다.

    Args:
        system_prompt: 시스템 프롬프트
        user_prompt: 사용자 프롬프트
        provider: 'claude', 'openai', 또는 'gemini' (None이면 config에서 결정)
        api_key: API 키 (None이면 config에서 결정)
        model: 모델명 (None이면 config에서 결정)

    Returns:
        LLM 응답 텍스트
    """
    provider = provider or getattr(config, "PROVIDER", getattr(config, "LLM_PROVIDER", "claude"))
    provider = provider.lower()

    if provider == "claude":
        import anthropic
        api_key = api_key or getattr(config, "CLAUDE_API_KEY", getattr(config, "API_KEY", None))
        model = model or getattr(config, "CLAUDE_MODEL", getattr(config, "MODEL", "claude-sonnet-4-20250514"))
        client = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()
        response = client.messages.create(
            model=model,
            max_tokens=4096,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return response.content[0].text
    elif provider == "openai":
        import openai
        api_key = api_key or getattr(config, "OPENAI_API_KEY", getattr(config, "API_KEY", None))
        model = model or getattr(config, "OPENAI_MODEL", getattr(config, "MODEL", "gpt-4o"))
        client = openai.OpenAI(api_key=api_key) if api_key else openai.OpenAI()
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.choices[0].message.content
    elif provider == "gemini":
        api_key = api_key or getattr(config, "GEMINI_API_KEY", getattr(config, "API_KEY", None))
        model = model or getattr(config, "GEMINI_MODEL", getattr(config, "MODEL", "gemini-2.5-flash"))
        
        # Sanitize invalid model names
        if model in ["gemini-3.1-pro", "gemini-3.1", "gemini-3-pro"]:
            model = "gemini-2.5-flash"

        try:
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=api_key) if api_key else genai.Client()
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        temperature=getattr(config, "TEMPERATURE", 0.3),
                    ),
                )
                return response.text
            except Exception as e:
                # If specified model is invalid (404) or quota exceeded (429), fallback to gemini-2.5-flash
                if model != "gemini-2.5-flash" and ("404" in str(e) or "429" in str(e) or "NOT_FOUND" in str(e)):
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=user_prompt,
                        config=types.GenerateContentConfig(
                            system_instruction=system_prompt,
                            temperature=getattr(config, "TEMPERATURE", 0.3),
                        ),
                    )
                    return response.text
                raise e
        except ImportError:
            import google.generativeai as genai
            if api_key:
                genai.configure(api_key=api_key)
            try:
                model_obj = genai.GenerativeModel(
                    model_name=model,
                    system_instruction=system_prompt,
                )
                response = model_obj.generate_content(user_prompt)
                return response.text
            except Exception as e:
                if model != "gemini-2.5-flash":
                    model_obj = genai.GenerativeModel(
                        model_name="gemini-2.5-flash",
                        system_instruction=system_prompt,
                    )
                    response = model_obj.generate_content(user_prompt)
                    return response.text
                raise e
    else:
        raise ValueError(f"지원하지 않는 provider: {provider}")


def _call_with_retry(system_prompt: str, user_prompt: str, provider: str = None, api_key: str = None, model: str = None, max_retries: int = 2) -> dict:
    """재시도 로직이 포함된 LLM 호출 및 JSON 파싱"""
    last_error = None
    for attempt in range(max_retries + 1):
        try:
            raw = call_llm(system_prompt, user_prompt, provider, api_key, model)
            return _extract_json(raw)
        except Exception as e:
            last_error = e
            if attempt < max_retries:
                time.sleep(1 * (attempt + 1))
    raise RuntimeError(f"LLM 호출 실패 (재시도 {max_retries}회 후): {last_error}")


_BASE_SYSTEM = (
    "You are an expert PM analyst following PMBOK 8th edition. "
    "Analyze from Mindset → Performance Domain → AI Use Case perspective. "
    "Focus on root causes, not symptoms. "
    "Response must be valid JSON only, no markdown."
)


def analyze_project(scenario_text: str, provider: str = None, api_key: str = None, model: str = None) -> dict:
    """프로젝트 시나리오를 4단계 체인 LLM 호출로 분석합니다.

    Args:
        scenario_text: 분석할 프로젝트 시나리오 텍스트
        provider: LLM 제공자
        api_key: API 키
        model: 모델명

    Returns:
        overview, root_causes, governance, quantitative 키를 포함하는 분석 결과 딕셔너리
    """
    kwargs = {"provider": provider, "api_key": api_key, "model": model}

    # Call 1: 개요 및 증상 추출
    system1 = (
        f"{_BASE_SYSTEM}\n\n"
        "Extract project overview and symptoms. Return JSON with keys: "
        "project_name, project_goal, duration, launch_date, methodology, partners, "
        "success_criteria (array of {kpi, target, actual, status: fail/warn/ok}), "
        "symptoms (object with keys: scope, schedule, stakeholder, risk_quality, governance - "
        "each an array of {id, symptom, evidence})."
    )
    overview = _call_with_retry(system1, scenario_text, **kwargs)

    # Call 2: 근본 원인 분석
    system2 = (
        f"{_BASE_SYSTEM}\n\n"
        "Using the PMBOK 8th edition Mindset → Performance Domain → AI Use Case framework, "
        "analyze root causes. Return JSON with keys: "
        "top5_problems (array of {rank, title, severity: Critical/High, related_symptoms, "
        "mindset, mindset_analysis (array), five_whys (array of {q, a}), root_cause_conclusion, "
        "domains (array of {name, relation: direct/indirect, impact}), "
        "ai_usecases (array of {name, description})}), "
        "causal_map ({description, root_of_roots})."
    )
    user2 = f"Scenario:\n{scenario_text}\n\nPrevious analysis (overview):\n{json.dumps(overview, ensure_ascii=False)}"
    root_causes = _call_with_retry(system2, user2, **kwargs)

    # Call 3: 거버넌스 및 이해관계자 평가
    system3 = (
        f"{_BASE_SYSTEM}\n\n"
        "Assess governance and stakeholders. Return JSON with keys: "
        "raci ({activities, roles, matrix (2D array), conflicts (array of {activity, issue, description})}), "
        "risks (array of {id, name, probability: 1-5, impact: 1-5, score, grade, response}), "
        "stakeholders (array of {name, role, current_level: 1-5, desired_level: 1-5, gap}), "
        "fishbone ({effect, categories (array of {name, causes})})."
    )
    user3 = (
        f"Scenario:\n{scenario_text}\n\n"
        f"Overview:\n{json.dumps(overview, ensure_ascii=False)}\n\n"
        f"Root causes:\n{json.dumps(root_causes, ensure_ascii=False)}"
    )
    governance = _call_with_retry(system3, user3, **kwargs)

    # Call 4: 정량적 데이터 생성
    system4 = (
        f"{_BASE_SYSTEM}\n\n"
        "Based on the project situation, generate realistic quantitative monitoring data. "
        "Return JSON with keys: "
        "evm ({sprints (array of {name, pv, ev, ac, spi, cpi}), bac, eac}), "
        "control_chart ({metric_name, target, ucl, lcl, data (array of {week, value})}), "
        "burndown ({sprint_name, total_sp, ideal (array), actual (array), scope_change_day, scope_change_desc}), "
        "pareto ({categories (array of {name, count, cumulative_pct})}), "
        "variance (array of {kpi, planned, actual, variance, variance_pct, status: red/orange/green}), "
        "trend ({metrics (array of {name, unit, target, data (array of {week, value}), direction: up_bad/down_bad})})."
    )
    user4 = (
        f"Scenario:\n{scenario_text}\n\n"
        f"Overview:\n{json.dumps(overview, ensure_ascii=False)}\n\n"
        f"Root causes:\n{json.dumps(root_causes, ensure_ascii=False)}\n\n"
        f"Governance:\n{json.dumps(governance, ensure_ascii=False)}"
    )
    quantitative = _call_with_retry(system4, user4, **kwargs)

    return {
        "overview": overview,
        "root_causes": root_causes,
        "governance": governance,
        "quantitative": quantitative,
    }
