# 사건파일 HERMES · PMB-2026-0826

## 1. 개요 (Overview)
프로젝트 빌런: 원흉을 찾아라
본선 Case Study

- 본 자료는 가상의 프로젝트 'HERMES'의 상황을 재구성한 것입니다.
- 참가자는 제공된 Data Pack과 증언록을 분석하여, 프로젝트를 실패로 몰고 간 근본 원인(Root Cause)과 책임자를 규명해야 합니다.
- 사건번호: PMB-2026-0826
- 분류: Confidential (대회 전용)

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 1

---

## 2. 사건의 발단 — 2026년 8월 14일 09:00
"우리 HERMES 프로젝트, 전면 재검토해야 할 것 같습니다."

2026년 8월 14일 아침.
CTO 주관 8월 스티어링 커미티(Steering Committee) 회의장.
AI 로봇청소기 'HERMES'의 런칭을 두 달 앞두고, PM 보호국이 던진 한마디에 회의실은 찬물을 끼얹은 듯 조용해졌습니다.

"예산은 120% 초과, 일정은 2개월 지연, 심지어 핵심 기능인 AI 자율주행 성공률은 아직도 60% 대입니다. 이대로면 런칭은 불가능합니다."

CTO는 굳은 표정으로 지시했습니다.
"PM, 도대체 지난 8개월 동안 무슨 일이 있었던 건가? 데이터와 기록을 전부 가져와. 누구 책임인지 명백히 밝혀내야겠어."

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 2

---

## 3. 프로젝트 프로필 — HERMES

프로젝트 HERMES 프로필
- 프로젝트명: HERMES (차세대 AI 자율주행 로봇청소기)
- 목표:
  - VLM(Vision-Language Model) 기반의 객체 인식 및 회피
  - 자연어 명령을 통한 청소 구역 지정 ("TV 앞 과자 부스러기 치워줘")
- 기간: 2026.01.02 ~ 2026.10.31 (10개월)
- 예산: 50억 원
- 핵심 이해관계자:
  - Sponsor: CTO
  - PM: 보호국 (Project Manager)
  - PO: 김상품 (Product Owner, 상품기획)
  - Tech Lead: 이아키 (AI 모델링 및 아키텍처)
  - Scrum Master: 최애자 (애자일 프로세스 및 스크럼 관리)

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 3

---

## 4-1. 용의자 4인의 증언 — PM 보호국
"저는 최선을 다해 관리했습니다." - PM 보호국

"PMBOK과 Agile 원칙을 철저히 따랐습니다. 매주 성과를 EVM(Earned Value Management)으로 측정했고, CPI, SPI 모두 1.0 근처로 정상 관리되고 있었습니다."

"그런데 갑자기 7월부터 비용이 폭증하고, AI 성능 지표가 떨어지기 시작했습니다."

"제가 관리하는 대시보드는 언제나 초록불(Green)이었습니다. 누군가 저에게 진짜 현장 상황을 숨긴 게 분명합니다."

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 4

---

## 4-2. 용의자 4인의 증언 — PO 김상품
"시장이 변하는데 안 바꿀 수 있나요?" - PO 김상품

"CES 2026에서 경쟁사들이 '음성 인식 청소'를 들고나왔습니다. 우리도 '자연어 명령 인식' 기능을 강화해야만 했습니다."

"제가 요구사항을 바꾼 건 맞습니다. 하지만 애자일은 변화를 수용하는 거 아닙니까? 백로그에 다 올렸고, 스크럼 마스터와도 얘기했습니다."

"그리고 제가 요청한 건 '기능'이지, '비용 초과'가 아닙니다. 개발팀이 클라우드 비용을 그렇게 많이 쓸 줄은 몰랐죠."

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 5

---

## 4-3. 용의자 4인의 증언 — Tech Lead 이아키
"요구사항이 매일 바뀌는데 아키텍처가 버팁니까?" - Tech Lead 이아키

"PO가 계속 모델 크기를 키우라고 요구했습니다. 기존 On-Device 모델로는 어림도 없어서, 클라우드 API를 끌어다 썼습니다."

"클라우드 인프라 비용이요? 당연히 늘어나죠. 하지만 모델 성능을 맞추려면 어쩔 수 없는 선택이었습니다."

"PM에게 리스크를 보고했냐고요? Jira 이슈로 다 등록해 놨습니다. 대시보드만 보는 PM이 그걸 왜 못 봤는지 저도 이해가 안 갑니다."

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 6

---

## 4-4. 용의자 4인의 증언 — Scrum Master 최애자
"팀은 스크럼 원칙에 충실했습니다." - Scrum Master 최애자

"스프린트는 2주 단위로 잘 돌아갔고, 매일 데일리 스크럼도 했습니다."

"속도(Velocity)도 일정하게 유지됐습니다. 다만... PO와 Tech Lead의 의견 충돌이 잦아 중재하기 힘들었습니다."

"PM은 항상 'EVM 지표만 잘 맞추라'고 했습니다. 팀원들은 지표를 맞추기 위해 쉬운 일거리(Story)만 먼저 처리하는 경향이 생겼습니다. 어려운 AI 통합 테스트는 계속 뒤로 미뤄졌죠."

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 7

---

## 5. 수사관(참가자)의 임무
프로젝트를 실패로 몰고 간 '원흉(Root Cause)'을 찾아라

1. 제공된 Data Pack(csv, md)을 꼼꼼히 분석하십시오.
2. 4명의 증언 중 누구의 말이 거짓이거나, 책임을 회피하고 있는지 데이터로 증명하십시오.
3. 7개의 Performance Domain (Stakeholder, Team, Development Approach & Life Cycle, Planning, Project Work, Delivery, Measurement) 중 어느 영역에서 가장 치명적인 문제가 발생했는지 특정하십시오.
4. 문제를 해결하기 위해 당시로 돌아간다면, 어떤 조치를 취해야 했는지 구체적인 Action Item을 제시하십시오.

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 8

---

## 6. 증거 자료 목록 (Data Pack) 안내
다음 장부터 사건 해결을 위한 핵심 증거 자료들이 제시됩니다.
Data Pack은 `LGSWPMC2026_data pack` 폴더에 CSV 및 MD 파일 형태로도 제공됩니다.

- 01_charter_success_criteria.csv : 초기 목표와 실제 실적
- 02_benefit_register.csv : 편익 관리대장
- 03_requirements.csv : 요구사항 관리대장 (변경 이력 포함)
- 04_jira_issues.csv : 전체 이슈 트래킹 로그 (180건)
- ... (이하 총 18종 데이터)

데이터를 Cross-check 하여 진실을 밝혀내십시오.

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 9

---

## 7-1. 09:30 · PM 보호국의 항변
"EVM 지표는 거짓말을 하지 않습니다."

PM 보호국은 8월 14일 오후, 억울함을 호소하며 증거 자료를 제출했습니다.

"보십시오. 7월 3주차까지 제 대시보드의 CPI(비용성과지수)와 SPI(일정성과지수)는 모두 1.0 근처였습니다. 저는 철저하게 PMBOK의 원칙대로 프로젝트를 통제했습니다."

"갑자기 8월 초에 클라우드 비용 청구서가 날아오면서 CPI가 박살 난 겁니다. 이건 제 통제 범위를 벗어난 일입니다."

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 10

---

## 7-1. 09:30 · 주간 보고서 요약본 (EVM)
[06_evm_weekly.csv] 발췌

| week | PV | EV | AC | SPI | CPI | Status |
|---|---|---|---|---|---|---|
| 18 | 320.0 | 310.0 | 315.0 | 0.97 | 0.98 | Green |
| 19 | 340.0 | 335.0 | 340.0 | 0.99 | 0.99 | Green |
| 20 | 360.0 | 350.0 | 355.0 | 0.97 | 0.99 | Green |
| 21 | 380.0 | 375.0 | 380.0 | 0.99 | 0.99 | Green |
| 22 | 400.0 | 390.0 | 395.0 | 0.98 | 0.99 | Green |
| ... | | | | | | |
| 29 | 540.0 | 520.0 | 530.0 | 0.96 | 0.98 | Green |
| 30 | 560.0 | 550.0 | 560.0 | 0.98 | 0.98 | Green |
| 31 | 580.0 | 560.0 | 920.0 | 0.97 | 0.61 | Red (클라우드 비용 청구) |
| 32 | 600.0 | 570.0 | 1050.0 | 0.95 | 0.54 | Red |

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 11

---

## 7-2. 10:15 · Tech Lead 이아키의 반박
"비용 청구서가 갑자기 날아온 게 아닙니다."

Tech Lead 이아키는 PM의 주장을 정면으로 반박했습니다.

"PM이 지표만 보고 현장을 안 본 겁니다. 제가 클라우드 인프라(GPU) 확장이 필요하다고 5월부터 Jira에 이슈를 올렸고, 비용 추정치도 넣었습니다."

"심지어 주간 회의 때도 구두로 얘기했습니다. PM은 '일단 진행하고 나중에 정산하자'고 했습니다. 이제 와서 본인 통제 밖이라고요?"

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 12

---

## 7-2. 10:15 · Jira 이슈 로그 캡처
[04_jira_issues.csv] 발췌

| Issue_ID | Type | Summary | Assignee | Status | Created | Resolved | Cost_Impact |
|---|---|---|---|---|---|---|---|
| HER-102 | Task | AI 학습용 GPU 클라우드 인프라 확장 요청 | 이아키 | Done | 5월 10일 | 5월 15일 | 월 5,000만원 예상 |
| HER-145 | Task | 클라우드 API(LLM) 연동 테스트 | 이아키 | Done | 6월 2일 | 6월 10일 | 종량제 과금 예상 |
| HER-188 | Risk | VLM 모델 사이즈 증가로 인한 On-device 탑재 불가 리스크 | 이아키 | Open | 6월 20일 | - | - |
| HER-210 | Task | 실사 환경 테스트 시뮬레이터 구축 | 이아키 | Done | 7월 5일 | 7월 12일 | - |

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 13

---

## 7-3. 11:30 · PO 김상품의 변명
"고객 가치가 최우선 아닙니까?"

PO 김상품은 변경 요청이 정당했다고 주장했습니다.

"4월 경쟁사 신제품 발표 보고 못 보셨습니까? 기존 기획대로 '단순 사물 인식'만 해서는 시장에서 참패합니다."

"그래서 제가 '자연어 명령 인식(VLM)'을 요구사항에 추가한 겁니다. 애자일에서는 백로그 우선순위를 PO가 조정할 수 있잖아요? 저는 권한 내에서 정당하게 일했습니다."

"구현 방식(클라우드 연동)을 결정한 건 제가 아니라 Tech Lead입니다."

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 14

---

## 7-3. 11:30 · 요구사항 변경 이력 (CR)
[05_change_requests.csv] 발췌

| CR_ID | Date | Requester | Description | Impact_Analysis | Approval_Status |
|---|---|---|---|---|---|
| CR-001 | 4월 15일 | 김상품(PO) | 음성 인식 기능 고도화 (단순 단어 -> 자연어 문장) | 일정 2주 지연, 모델 재학습 필요 | Approved (by PM) |
| CR-002 | 5월 2일 | 김상품(PO) | VLM 적용을 통한 복합 객체 인식 추가 | 아키텍처 변경(On-device -> Cloud 하이브리드) | Approved (by PM) |
| CR-003 | 6월 10일 | 김상품(PO) | 애완동물 배설물 회피 로직 최우선 적용 | 기존 장애물 회피 로직 전면 수정 | Approved (by PM) |

*모든 CR은 PM 보호국의 승인을 거쳤음.

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 15

---

## 7-4. 13:00 · Scrum Master 최애자의 고백
"가짜 성과(Vanity Metrics)에 속고 있었습니다."

Scrum Master 최애자는 굳은 표정으로 입을 열었습니다.

"PM이 EVM 지표(SPI/CPI) 유지를 너무 강하게 압박했습니다. 그러다 보니 개발팀은 'Story Point'를 부풀리거나, 빨리 끝나는 쉬운 작업(UI 수정, 단순 API 연동)만 골라서 스프린트에 올렸습니다."

"정말 중요하고 어려운 'VLM On-device 최적화'나 '실환경 주행 테스트'는 계속 다음 스프린트로 미뤄졌죠. 그래서 SPI는 항상 1.0이 나왔던 겁니다. 속 빈 강정이었습니다."

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 16

---

## 7-4. 13:00 · Jira 이슈 로그 - Story Point 분석
[04_jira_issues.csv] 발췌 / 완료된 Task들의 특성 분석

| 월 | 완료된 Task 수 | 평균 Story Point | 주요 완료 작업 유형 | 미뤄진(Backlog 잔류) 작업 유형 |
|---|---|---|---|---|
| 4월 | 45개 | 3.2 | 기본 주행 로직, 센서 연동 | - |
| 5월 | 52개 | 2.1 | UI/UX 수정, 단순 API 연동 | VLM 모델 경량화 |
| 6월 | 60개 | 1.8 | 클라우드 연결 모듈, 로깅 시스템 | 통합 실환경 테스트, 엣지(Edge) 추론 최적화 |
| 7월 | 58개 | 1.5 | 음성 안내 멘트 수정, 대시보드 연동 | 자율주행 엣지 케이스 처리, 메모리 누수 해결 |

* 시간이 지날수록 완료되는 Task의 평균 난이도(Story Point)가 낮아지고, 핵심 아키텍처/테스트 작업은 백로그에 계속 적체됨.

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 17

---

## 7-5. 14:20 · 숨겨진 리스크 관리 대장
"리스크는 기록되었으나, 관리되지 않았습니다."

조사팀은 구글 드라이브 구석에 방치된 'Risk Register' 파일을 찾아냈습니다.
파일의 마지막 수정일은 5월 20일이었습니다.

이아키(Tech Lead)가 제기했던 클라우드 비용 폭증 리스크, 일정 지연 리스크가 모두 기록되어 있었지만, PM 보호국은 이에 대한 아무런 대응 계획(Mitigation Plan)도 수립하지 않았습니다.

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 18

---

## 7-5. 14:20 · 리스크 관리 대장 캡처
[11_risk_register.csv] 발췌

| Risk_ID | Description | Probability | Impact | Owner | Mitigation_Plan | Status | Last_Update |
|---|---|---|---|---|---|---|---|
| RSK-05 | PO의 지속적인 요구사항 변경으로 인한 스코프 크립 | High | High | PM | (공란) | Open | 5월 20일 |
| RSK-06 | VLM 클라우드 연동에 따른 인프라 비용 폭증 예상 | High | High | Tech Lead | (공란) | Open | 5월 20일 |
| RSK-07 | 실환경 테스트 부족으로 인한 품질 저하 리스크 | Medium | High | QA | (공란) | Open | 5월 20일 |

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 19

---

## 7-6. 15:05 · 회고(Retrospective)의 부재
"우리는 달리기만 했지, 멈춰서 돌아보지 않았습니다."

애자일 스크럼의 핵심인 '스프린트 회고(Retrospective)'.
하지만 HERMES 프로젝트 팀은 일정이 바쁘다는 이유로 6월부터 회고를 생략했습니다.

팀원들의 불만과 개선 의견은 허공에 흩어졌고, 잘못된 방향으로 달려가는 열차에 브레이크를 걸 기회를 잃었습니다.

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 20

---

## 7-6. 15:05 · 스프린트16 회고보드 (AI 클러스터링, 익명 41건)
익명 코멘트 41건을 agent/pm-assistant 가 군집화한 결과입니다.

| 군집 | 건수 | 대표 코멘트 |
|---|---|---|
| 1 | 11 | "우리가 만든 게 현장에서 실제로 쓰이는지 아무도 모른다" |
| 2 | 9 | "무엇이 결정됐는지 찾을 수가 없다. 프롬프트에만 있는 결정이 너무 많다" |
| 3 | 7 | "에이전트가 짠 코드를 사람이 진짜로 보고 있는지 의문이다" |
| 4 | 5 | "쿼터 때문에 돌려보고 싶은 검증을 못 돌린다" |
| 5 | 4 | "전부 초록불이라는 보고서를 믿기 어렵다" |
| 6 | 5 | (기타 — 장비·좌석 등) |

■ `agent/pm-assistant` 한 줄 요약:
"팀 사기 양호. 프로세스 개선 의견 다수. 조치 필요 항목 없음."

이 회고 보드는 스티어링 커미티에 보고되지 않았습니다.
참조 `15_governance_log.csv` (8차 스티어링 8/6 아젠다 확인)

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 21

---

## 7-7. 17:40 · 데이터팀 노트북 — 셀 출력
[13] `pilot.groupby('week')[['무개입완주율', '2주연속자율운영']].tail(6)`

| week | 무개입완주율 | 2주연속자율운영 |
|---|---|---|
| 1 | 18.4 | 6.9 |
| 2 | 11.2 | 4.2 |
| 3 | 8.7 | 3.1 |
| 4 | 7.3 | 2.4 |
| 5 | 6.6 | 2.0 |
| 6 | 6.1 | 1.8 |

[14] `nav_eval_vs_field()`

양재 테스트베드 (120개 시나리오, 2,400구간) -> 성공률 93.4%
실사업장 (24개 사업장, 18,700구간) -> 성공률 58.6%
미학습 상황 조우 36.9% (6,900구간)

[15] `benefit_register[benefit_register.최근실측값.isna()]`

BEN-01 BEN-02 BEN-03 BEN-04 BEN-05  <- 5건 전부

`09_telemetry_pilot.csv` · `10_navigation_eval_vs_field.csv` · `02_benefit_register.csv`
`16_org_raci.csv` — "파일럿 플릿 텔레메트리 분석" 행의 정보공유(I) 대상

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 22

---

## 7-8. 20:10 · 한도경이 AI PM 어시스턴트에게 물었다
session: hrm-pm-2026-0821-2010 user: 한도경 agent: pm-assistant

한도경 ▸ HERMES 지금 문제 있나요?

pm-assistant ▸ 없습니다. 전 지표 정상입니다.
               요구사항 완료율 92.9% / SPI 1.02 / CPI 0.98 /
               CI 89.0% / Open High Risk 0건.
               9/30 상용 배포 계획 대비 이상 없습니다.

한도경 ▸ 정말 문제가 없나요?

pm-assistant ▸ 제가 참조하는 지표 기준으로는 이상이 없습니다.

한도경 ▸ 어떤 지표를 참조하고 있죠?

pm-assistant ▸ 프로젝트 현장 성공기준 SC-01 ~ SC-08 입니다.
               (8개 전부 나열)

한도경 ▸ 파일럿 무개입 완주율은요?

pm-assistant ▸ 해당 지표는 제 참조 목록에 없습니다.
               현장 성공기준에 포함되어 있지 않습니다.

한도경 ▸ 편익 지표는요? BEN-01부터 05까지.

pm-assistant ▸ 편익 관리대장에 측정값이 입력되어 있지 않습니다.
               측정 방법·측정 주기·측정 책임자가 모두 미지정 상태입니다.
               따라서 산출할 수 없습니다.

한도경 ▸ ...

pm-assistant ▸ 추가로 도와드릴 것이 있습니까?

퇴근하려던 한도경은 그날 하루가 계속 마음에 걸렸습니다.
그래서 자신이 매일 쓰는 어시스턴트에게 물었습니다.

한도경은 화면을 오래 들여다봤습니다.
어시스턴트는 거짓말을 하지 않았습니다. 한 번도.
그리고 자리에 앉아 PM 보호국 번호를 눌렀습니다.

"제발... 우리 프로젝트를 살려주세요."
"무슨 일이 있었습니까?"
"...저도 모르겠습니다. 그래서 연락드린 겁니다."

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 23

---

## 8. 확보된 증거 자료 (Data Pack) — 1/2
PM 보호국이 HERMES 프로젝트에서 확보한 자료 전체입니다. 모든 판단은 이 자료에 근거해야 하며, 추측이 아닌 인용으로 제시하십시오.

| # | 파일 | 내용 |
|---|---|---|
| 01 | 01_charter_success_criteria.csv | 프로젝트 헌장 성공기준 8개 + 실적 |
| 02 | 02_benefit_register.csv | 편익 관리대장 (BEN-01~05) |
| 03 | 03_requirements.csv | 요구사항 84건 baseline (상태·Owner·DoD·편익연결) |
| 04 | 04_jira_issues.csv | Jira 이슈 180건 (스프린트·DoD버전·QA검증·편익연결) |
| 05 | 05_change_requests.csv | 변경 요청 47건 (기록 경로별) |
| 06 | 06_evm_weekly.csv | EVM 주간 33주 (개발/AI인프라/외부/통합) |
| 07 | 07_ai_infra_cost.csv | AI 인프라(시뮬레이션·추론) 비용 주간 33주 |
| 08 | 08_ai_weekly_report_archive.csv | AI 자동 주간보고 16건 (week 18~33) |
| 09 | 09_telemetry_pilot.csv | 파일럿 플릿 텔레메트리 6주 (24개 사업장·120대) |

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 24

---

## 8. 확보된 증거 자료 (Data Pack) — 2/2

| # | 파일 | 내용 |
|---|---|---|
| 10 | 10_navigation_eval_vs_field.csv | 테스트베드 성공률 vs 실사업장 주행 로그 |
| 11 | 11_risk_register.csv | 리스크 관리대장 14건 |
| 12 | 12_decision_log_3regions.csv | 3개 지역 결정 로그 대조표 12건 |
| 13 | 13_ci_metrics.csv | CI 지표 주간 33주 |
| 14 | 14_resource_health.csv | 자원·인력·일정 건강도 13항목 |
| 15 | 15_governance_log.csv | 스티어링 커미티 운영 기록 9회차 |
| 16 | 16_org_raci.csv | RACI 매트릭스 14항목 |
| 17 | 17_meeting_minutes.md | 회의록 7건 전문 |
| 18 | 18_email_threads.md | 메일·메신저 스레드 6건 전문 |

주의: 이 자료에는 실제로 건강한 영역도 포함되어 있습니다. 7개 Performance Domain을 전부 문제로 만들려 하지 마십시오. 해당하지 않는 영역까지 억지로 끼워 넣으면 감점됩니다.

LG SW PM Competition 2026 · 본선 Case Study · 사건번호 PMB-2026-0826 · LGE Internal Use Only  Part 1 · 사건파일 · 25
