import importlib
import streamlit as st
import streamlit.components.v1 as components
from jinja2 import Environment, FileSystemLoader
import os
import traceback

import config
import core.file_reader
import core.analyzer
import core.data_generator

importlib.reload(config)
importlib.reload(core.file_reader)
importlib.reload(core.analyzer)
importlib.reload(core.data_generator)

from core.file_reader import read_file
from core.analyzer import analyze_project
from core.data_generator import ensure_quantitative_data


st.set_page_config(
    page_title="PM Analysis Report Generator",
    layout="wide",
)

# --- Sidebar ---
with st.sidebar:
    st.header("⚙️ 설정")

    llm_provider = st.selectbox("LLM Provider", ["Claude", "OpenAI", "Gemini"])

    api_key = st.text_input("API Key", type="password", help="미입력 시 .env 파일의 API 키를 사용합니다.")

    if llm_provider == "Claude":
        default_model = getattr(config, "CLAUDE_MODEL", "claude-sonnet-4-20250514")
    elif llm_provider == "OpenAI":
        default_model = getattr(config, "OPENAI_MODEL", "gpt-4o")
    else:
        default_model = getattr(config, "GEMINI_MODEL", "gemini-2.5-flash")

    if "last_provider" not in st.session_state or st.session_state["last_provider"] != llm_provider:
        st.session_state["last_provider"] = llm_provider
        st.session_state["model_name_input"] = default_model

    if st.session_state.get("model_name_input") in ["gemini-3.1-pro", "gemini-3.1"]:
        st.session_state["model_name_input"] = default_model

    model_name = st.text_input("Model Name", key="model_name_input")

    st.divider()
    st.caption("💡 `.env.example` 파일을 참고하여 API 키를 설정하세요.")

# --- Main Area ---
st.title("🎯 PM 프로젝트 분석 리포트 생성기")
st.markdown("프로젝트 시나리오를 입력하면 PMBOK 8판 기반 20개 분석 도구를 적용한 종합 리포트를 생성합니다.")

tab1, tab2 = st.tabs(["텍스트 입력", "파일 업로드"])

with tab1:
    scenario_text = st.text_area(
        "프로젝트 시나리오를 입력하세요",
        height=400,
        placeholder="여기에 프로젝트 시나리오를 붙여넣으세요...",
    )

with tab2:
    uploaded_file = st.file_uploader(
        "파일을 업로드하세요",
        type=["txt", "md", "pdf"],
    )


def render_html(analysis_result: dict) -> str:
    """Jinja2 템플릿을 사용하여 HTML 리포트를 렌더링합니다."""
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("base.html")
    
    full_result = ensure_quantitative_data(analysis_result or {})
    
    # Extra safety guarantee for Jinja2 template rendering
    if not isinstance(full_result.get("project"), dict):
        full_result["project"] = {}
    
    project_dict = full_result["project"]
    if not project_dict.get("project_name"):
        project_dict["project_name"] = "프로젝트 분석 리포트"
    if not project_dict.get("project_goal"):
        project_dict["project_goal"] = "시나리오 기반 PMBOK 8판 분석"
    if not project_dict.get("duration"):
        project_dict["duration"] = "-"
    if not project_dict.get("launch_date"):
        project_dict["launch_date"] = "-"
    if not project_dict.get("methodology"):
        project_dict["methodology"] = "하이브리드"
    if not project_dict.get("partners"):
        project_dict["partners"] = "-"
        
    return template.render(**full_result)


if st.button("🚀 분석 시작", type="primary"):
    effective_api_key = api_key.strip() or getattr(config, f"{llm_provider.upper()}_API_KEY", "") or getattr(config, "API_KEY", "")
    if not effective_api_key:
        st.error("API 키를 입력하거나 .env 파일에 설정해 주세요.")
    else:
        # Determine input text
        input_text = None

        if uploaded_file is not None:
            try:
                input_text = read_file(uploaded_file)
            except Exception as e:
                st.error(f"파일 읽기 실패: {e}")
        elif scenario_text.strip():
            input_text = scenario_text.strip()

        if not input_text:
            st.error("분석할 시나리오 텍스트를 입력하거나 파일을 업로드해주세요.")
        else:
            try:
                progress_bar = st.progress(0)
                status = st.status("분석 진행 중...", expanded=True)

                status.write("📋 프로젝트 시나리오 분석 중...")
                progress_bar.progress(20)

                analysis_result = analyze_project(
                    scenario_text=input_text,
                    provider=llm_provider.lower(),
                    api_key=effective_api_key,
                    model=model_name,
                )
                progress_bar.progress(60)

                status.write("📊 정량 데이터 생성 중...")
                analysis_result = ensure_quantitative_data(analysis_result)
                progress_bar.progress(80)

                status.write("📝 HTML 리포트 렌더링 중...")
                html_report = render_html(analysis_result)
                progress_bar.progress(100)

                status.update(label="✅ 분석 완료!", state="complete")

                st.success("리포트가 성공적으로 생성되었습니다!")

                st.subheader("📄 리포트 미리보기")
                components.html(html_report, height=800, scrolling=True)

                st.download_button(
                    label="📥 HTML 리포트 다운로드",
                    data=html_report,
                    file_name="pm_analysis_report.html",
                    mime="text/html",
                )

            except Exception as e:
                st.error(f"분석 중 오류가 발생했습니다: {e}")
                st.expander("상세 오류 정보").code(traceback.format_exc())
