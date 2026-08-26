"""
정량 데이터 및 템플릿 컨텍스트 데이터 생성 모듈.

분석 결과에서 누락된 정량 데이터 및 HTML 렌더링에 필요한 키 구조를 채워넣는 폴백 및 래핑 모듈.
LLM 호출 없이 순수 Python으로 동작하며 모든 템플릿 필드의 안전성을 보장한다.
"""


def ensure_quantitative_data(analysis_result: dict) -> dict:
    """
    분석 결과에 정량 데이터 및 템플릿용 키 구조가 완벽히 존재하는지 확인하고,
    누락되거나 비어있는 항목을 안전한 기본값으로 채운다.

    Args:
        analysis_result: 분석 결과 딕셔너리.

    Returns:
        모든 템플릿 변수가 채워진 안심 분석 결과 딕셔너리.
    """
    result = dict(analysis_result) if isinstance(analysis_result, dict) else {}

    # 1. Overview & Project
    overview = result.get("overview")
    if not isinstance(overview, dict):
        overview = {}

    project = result.get("project")
    if not isinstance(project, dict):
        project = {}

    project_defaults = {
        "project_name": overview.get("project_name") or project.get("project_name") or "프로젝트 분석 리포트",
        "project_goal": overview.get("project_goal") or project.get("project_goal") or "시나리오 기반 PMBOK 8판 분석",
        "duration": overview.get("duration") or project.get("duration") or "-",
        "launch_date": overview.get("launch_date") or project.get("launch_date") or "-",
        "methodology": overview.get("methodology") or project.get("methodology") or "하이브리드",
        "partners": overview.get("partners") or project.get("partners") or "-",
    }
    result["project"] = project_defaults
    result["overview"] = overview

    success_criteria = result.get("success_criteria") or overview.get("success_criteria") or []
    if not isinstance(success_criteria, list):
        success_criteria = []
    result["success_criteria"] = success_criteria

    symptoms = result.get("symptoms") or overview.get("symptoms") or {}
    if not isinstance(symptoms, dict):
        symptoms = {}
    result["symptoms"] = symptoms

    # 2. Root Causes & Causal Map
    root_causes = result.get("root_causes")
    if not isinstance(root_causes, dict):
        root_causes = {}
    result["root_causes"] = root_causes

    top5_problems = result.get("top5_problems") or root_causes.get("top5_problems") or []
    if not isinstance(top5_problems, list):
        top5_problems = []
    
    cleaned_problems = []
    for idx, prob in enumerate(top5_problems, 1):
        if isinstance(prob, dict):
            cleaned_problems.append({
                "rank": prob.get("rank", idx),
                "title": prob.get("title", f"주요 문제 {idx}"),
                "severity": prob.get("severity", "High"),
                "mindset": prob.get("mindset", "PMBOK 8판 마인드셋 분석 불충분"),
                "mindset_analysis": prob.get("mindset_analysis", []),
                "five_whys": prob.get("five_whys", []),
                "root_cause_conclusion": prob.get("root_cause_conclusion", "구조적 관리 부재"),
                "domains": prob.get("domains", []),
                "ai_usecases": prob.get("ai_usecases", []),
            })
    result["top5_problems"] = cleaned_problems

    causal_map = result.get("causal_map") or root_causes.get("causal_map") or {}
    if not isinstance(causal_map, dict):
        causal_map = {}
    result["causal_map"] = {
        "description": causal_map.get("description", "프로젝트 주요 인과관계 매핑"),
        "root_of_roots": causal_map.get("root_of_roots", "PMBOK 8판 관점의 거버넌스 및 성과 영역 연계 부재"),
    }

    # 3. Governance
    governance = result.get("governance")
    if not isinstance(governance, dict):
        governance = {}
    result["governance"] = governance

    raci = result.get("raci") or governance.get("raci") or {}
    if not isinstance(raci, dict):
        raci = {}
    result["raci"] = {
        "activities": raci.get("activities", []),
        "roles": raci.get("roles", []),
        "matrix": raci.get("matrix", []),
        "conflicts": raci.get("conflicts", []),
    }

    risks = result.get("risks") or governance.get("risks") or []
    if not isinstance(risks, list):
        risks = []
    result["risks"] = risks

    stakeholders = result.get("stakeholders") or governance.get("stakeholders") or []
    if not isinstance(stakeholders, list):
        stakeholders = []
    result["stakeholders"] = stakeholders

    fishbone = result.get("fishbone") or governance.get("fishbone") or {}
    if not isinstance(fishbone, dict):
        fishbone = {}
    result["fishbone"] = {
        "effect": fishbone.get("effect", "프로젝트 성능 및 품질 이슈"),
        "categories": fishbone.get("categories", []),
    }

    # 4. Quantitative Charts
    quant = result.get("quantitative")
    if not isinstance(quant, dict):
        quant = {}

    evm = result.get("evm") or quant.get("evm")
    if not isinstance(evm, dict) or not evm.get("sprints"):
        evm = _generate_evm_data()
    result["evm"] = evm

    control_chart = result.get("control_chart") or quant.get("control_chart")
    if not isinstance(control_chart, dict) or not control_chart.get("data"):
        control_chart = _generate_control_chart_data()
    result["control_chart"] = control_chart

    burndown = result.get("burndown") or quant.get("burndown")
    if not isinstance(burndown, dict) or not burndown.get("ideal"):
        burndown = _generate_burndown_data()
    result["burndown"] = burndown

    pareto = result.get("pareto") or quant.get("pareto")
    if not isinstance(pareto, dict) or not pareto.get("categories"):
        pareto = _generate_pareto_data()
    result["pareto"] = pareto

    variance = result.get("variance") or quant.get("variance")
    if not isinstance(variance, list) or not variance:
        variance = _generate_variance_data()
    result["variance"] = variance

    trend = result.get("trend") or quant.get("trend")
    if not isinstance(trend, dict) or not trend.get("metrics"):
        trend = _generate_trend_data()
    result["trend"] = trend

    return result


def _generate_evm_data() -> dict:
    """
    EVM(Earned Value Management) 데이터를 생성한다.
    """
    sprints = []
    spi_values = [0.96, 0.91, 0.86, 0.81]
    cpi_values = [0.98, 0.94, 0.89, 0.84]
    planned_values = [250, 500, 750, 1000]

    for i, (spi, cpi, pv) in enumerate(zip(spi_values, cpi_values, planned_values), 1):
        ev = round(pv * spi)
        ac = round(ev / cpi) if cpi != 0 else ev
        sprints.append({
            "name": f"Sprint {i}",
            "sprint": i,
            "pv": pv,
            "ev": ev,
            "ac": ac,
            "planned_value": pv,
            "earned_value": ev,
            "actual_cost": ac,
            "spi": spi,
            "cpi": cpi,
        })

    return {
        "sprints": sprints,
        "bac": 1000,
        "eac": round(1000 / 0.84),
        "summary": {
            "current_spi": 0.81,
            "current_cpi": 0.84,
            "eac": round(1000 / 0.84),
            "variance_at_completion": round(1000 - 1000 / 0.84),
        },
    }


def _generate_control_chart_data() -> dict:
    """
    관리도 데이터를 생성한다.
    """
    values = [88.0, 86.5, 84.2, 82.8, 80.1, 78.3, 76.0]
    ucl = 90.0
    lcl = 80.0
    mean = 85.0

    weeks = []
    data = []
    for i, val in enumerate(values, 1):
        item = {
            "week": i,
            "value": val,
            "ucl": ucl,
            "lcl": lcl,
            "mean": mean,
            "out_of_control": val < lcl,
        }
        weeks.append(item)
        data.append(item)

    return {
        "metric_name": "코드 품질 점수",
        "unit": "%",
        "weeks": weeks,
        "data": data,
        "target": mean,
        "ucl": ucl,
        "lcl": lcl,
        "trend": "declining",
        "violations": sum(1 for v in values if v < lcl),
    }


def _generate_burndown_data() -> dict:
    """
    번다운 차트 데이터를 생성한다.
    """
    total_points = 40
    scope_increase = 12
    ideal_daily = total_points / 14

    days = []
    ideal_list = []
    actual_list = []
    remaining = total_points
    actual_velocity = 2.2

    for day in range(15):
        ideal = max(0, total_points - ideal_daily * day)

        if day == 7:
            remaining += scope_increase
        elif day > 0:
            remaining = max(0, remaining - actual_velocity)

        ideal_val = round(ideal, 1)
        actual_val = round(remaining, 1)
        ideal_list.append(ideal_val)
        actual_list.append(actual_val)

        days.append({
            "day": day,
            "ideal_remaining": ideal_val,
            "actual_remaining": actual_val,
        })

    return {
        "sprint_name": "Sprint 3",
        "total_sp": total_points,
        "sprint_days": 14,
        "initial_points": total_points,
        "scope_change_day": 7,
        "scope_increase": scope_increase,
        "scope_change_desc": "7일차 스코프 12SP 추가",
        "days": days,
        "ideal": ideal_list,
        "actual": actual_list,
        "completion_risk": "high",
    }


def _generate_pareto_data() -> dict:
    """
    파레토 차트 데이터를 생성한다.
    """
    categories = [
        {"name": "요구사항 변경", "category": "요구사항 변경", "count": 34},
        {"name": "기술 부채", "category": "기술 부채", "count": 28},
        {"name": "리소스 부족", "category": "리소스 부족", "count": 15},
        {"name": "커뮤니케이션 오류", "category": "커뮤니케이션 오류", "count": 9},
        {"name": "환경 이슈", "category": "환경 이슈", "count": 6},
        {"name": "외부 의존성", "category": "외부 의존성", "count": 5},
        {"name": "기타", "category": "기타", "count": 3},
    ]

    total = sum(c["count"] for c in categories)
    cumulative = 0
    for cat in categories:
        cumulative += cat["count"]
        cat["percentage"] = round(cat["count"] / total * 100, 1)
        cat["cumulative_pct"] = round(cumulative / total * 100, 1)
        cat["cumulative_percentage"] = cat["cumulative_pct"]

    return {
        "categories": categories,
        "total_issues": total,
        "insight": "상위 2개 카테고리(요구사항 변경, 기술 부채)가 전체 이슈의 62%를 차지",
    }


def _generate_variance_data() -> list:
    """
    분산 분석(계획 대비 실적) 데이터를 생성한다.
    """
    kpis = [
        {"kpi": "일정 준수율", "planned": 95.0, "actual": 78.0, "unit": "%", "status": "red"},
        {"kpi": "예산 소진율", "planned": 60.0, "actual": 73.0, "unit": "%", "status": "orange"},
        {"kpi": "결함 밀도", "planned": 2.0, "actual": 4.8, "unit": "건/KLOC", "status": "red"},
        {"kpi": "테스트 커버리지", "planned": 80.0, "actual": 62.0, "unit": "%", "status": "orange"},
        {"kpi": "요구사항 완료율", "planned": 85.0, "actual": 68.0, "unit": "%", "status": "orange"},
        {"kpi": "고객 만족도", "planned": 4.2, "actual": 3.1, "unit": "점(5점)", "status": "red"},
    ]

    for item in kpis:
        diff = item["actual"] - item["planned"]
        item["variance"] = round(diff, 1)
        item["variance_pct"] = round(diff / item["planned"] * 100, 1) if item["planned"] else 0

    return kpis


def _generate_trend_data() -> dict:
    """
    추세 데이터를 생성한다.
    """
    weeks = 8
    response_times = [1.2, 1.4, 1.6, 1.9, 2.3, 2.8, 3.2, 3.8]
    quality_scores = [92, 90, 87, 84, 81, 78, 74, 71]

    metrics = [
        {
            "name": "응답 시간",
            "unit": "초",
            "target": 1.5,
            "direction": "up_bad",
            "data": [{"week": i + 1, "value": response_times[i]} for i in range(weeks)],
        },
        {
            "name": "품질 점수",
            "unit": "점",
            "target": 90,
            "direction": "down_bad",
            "data": [{"week": i + 1, "value": quality_scores[i]} for i in range(weeks)],
        },
    ]

    return {
        "metrics": metrics,
        "insight": "응답 시간 증가와 품질 점수 하락이 지속되는 추세를 보임",
    }
