---
name: generate-competition-report
description: Run the PMC final competition pipeline. Analyzes a given markdown project situation, generates v3 tool data (inventing raw data), and builds the polished v4 HTML report based on established logic.
---

# Instructions

When the user asks you to analyze a new project situation (usually provided as a markdown file) and generate the competition report, follow these exact steps:

1. **Analyze the Project Situation (Evaluate strictly against the Official Criteria):**
   - Read the provided markdown file carefully.
   - Apply the PMBOK 8th edition Mindset and the 4-step logic framework (Mindset -> Performance Domain -> AI Use Case -> Future State).
   - Identify the Top 5 **root causes** (not just symptoms) and 5 minor risks.
   - **MUST ensure analysis and final output meet the Stage 1 & 2 Evaluation Criteria** (as defined in `pm-competition-overview.md`):
     - Stage 1: 적절한 이상징후 식별, 깊이있는 근본원인 도출(논리성), 문제 간 인과관계(타당성), 시스템 관점의 분석.
     - Stage 2: Proactive/Ownership/Value-driven 마인드셋 적용, 정확한 Performance Domain 식별, 도메인 간 파급효과 연계, 실현 가능한 AI Use Case, 그리고 이 3개 관점의 종합적 스토리라인 구축.

2. **Generate `[ProjectName]_stage1_stage2_analysis_v3.html` (Detailed Tool Data):**
   - Create the detailed `[ProjectName]_stage1_stage2_analysis_v3.html` using the previously established formatting standards.
   - You must create **15 tools total** (3 tools per core problem).
   - **CRITICAL:** The situation file will likely lack specific numbers. You MUST invent realistic raw data (metrics, dates, stakeholder quotes, variance numbers) to fill in the tools (e.g., RACI matrix, Control Charts, Burndown) to make them look authentic.

3. **Generate `[ProjectName]_stage1_stage2_analysis_v4.html` (Final Polished Report):**
   - Use the exact structure of the latest `stage1_stage2_analysis_v4.html` we built.
   - Ensure the slide structure includes:
     - Executive Summary & Gap Analysis.
     - 10-row Impact-Urgency Prioritization matrix (Top 5 highlighted).
     - Individual problem slides (Slide 06~10) with abstract minimalist square images.
     - Detailed tool slides extracted from `[ProjectName]_stage1_stage2_analysis_v3.html` (e.g., 06-B1, 06-B2, 06-B3).
     - HTML5 SVG Causal Relationship Map (do not use ASCII).
     - The "Mindset Synthesis" page (SLIDE 11).
   - **Negative Constraints (CRITICAL):** Do NOT use the words "본선", "본선 과제", "PMBOK", "PMBOK 8th", or "PMBOK 8판" anywhere in the generated text. Replace them with generic terms like "프로젝트", "수행 임무", "Global Standard", or "글로벌 표준 프레임워크".
   - Output the final HTML file with all CSS, SVGs, and base64 embedded images properly formatted and visually stunning (Dynamic Tech style).

4. **Review & Handover:**
   - Write a Walkthrough artifact highlighting what was generated and asking the user to review the final `[ProjectName]_stage1_stage2_analysis_v4.html`.
   - Do NOT attempt to build the PPTX unless explicitly requested by the user.
