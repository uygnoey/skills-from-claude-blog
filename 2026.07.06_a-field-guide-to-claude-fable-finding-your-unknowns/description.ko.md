[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude Fable 5 현장 가이드: 나의 미지(unknowns) 찾기

## 이 글이 뭔가요

Anthropic 기술 스태프 Thariq Shihipar가 쓴 현장 가이드로, Claude Fable 5와 일할 때 **지도**(내가 준 프롬프트·스킬·컨텍스트)와 **실제 지형**(진짜 코드베이스와 그 제약)의 간극을 좁히는 것을 핵심 과제로 놓는다. 모델이 강해질수록 결과물의 품질을 가르는 것은 계획을 얼마나 잘 세웠느냐가 아니라, **말해야 할 줄 몰랐던 것을 얼마나 잘 끄집어냈느냐**라는 주장이다.

글은 아직 말하지 않은 것을 네 가지로 나눈다 — 아는 앎(known knowns), 아는 모름(known unknowns), 모르는 앎(unknown knowns), 모르는 모름(unknown unknowns) — 그리고 프로젝트의 각 단계(구현 전 / 구현 중 / 구현 후)에 맞는 구체적인 수를 제시한다.

## 언제 유용한가요

- 잘 모르는 코드베이스 영역에서 작업을 시작할 때.
- 계획이나 스펙을 쓰면서 Claude가 편집을 시작하기 전에 의사결정 지점을 미리 찾아내고 싶을 때.
- 아직 좋은 결과와 나쁜 결과를 구분하지 못하는 낯선 도메인에서 일할 때.
- 완료한 변경을 맥락을 모르는 리뷰어나 이해관계자에게 넘겨야 할 때.
- Claude가 만들어 준 변경을 내가 정말로 이해했는지 검증하고 싶을 때.

## 핵심 포인트

- **네 가지 미지.** *아는 앎*은 프롬프트에 적어 넣은 것. *아는 모름*은 이름 붙일 수 있는 공백. *모르는 앎*은 나에게 너무 당연해서 적을 생각조차 안 하는 세부사항. *모르는 모름*은 아예 고려해 본 적 없는 사각지대.
- **블라인드 스팟 패스.** Claude에게 사각지대를 직접 물어보되, 내 숙련도를 함께 알려 주어 눈높이를 맞추게 한다.
- **브레인스토밍과 프로토타입.** 본 구현에 들어가기 전에 여러 접근을 탐색해, 모호한 판단 기준을 싸게 일찍 드러낸다.
- **인터뷰.** Claude에게 한 번에 한 질문씩 인터뷰하게 하고, 답에 따라 아키텍처가 바뀔 질문을 우선하게 한다.
- **레퍼런스.** 원하는 동작을 이미 구현한 기존 소스 코드를 가리켜 준다 — 프로그래밍 언어가 달라도 상관없다.
- **구현 계획.** 작업 시작 전에 유력한 의사결정 지점을 명시한 계획을 요청한다.
- **구현 노트.** 임시 `implementation-notes.md`를 두고, 엣지 케이스 때문에 계획에서 벗어난 지점을 Claude가 전부 기록하게 한다.
- **피치와 해설 문서.** 프로토타입·스펙·구현 노트를 하나의 공유 가능한 문서로 묶어 동의를 얻는다.
- **퀴즈.** 맥락이 담긴 리포트와 자가진단 퀴즈를 요청해, 변경 내용을 실제로 이해했는지 확인한다.
- **실제 사례.** 저자는 Claude Code로 Fable 런칭 영상을 편집하면서, 전사·컬러 그레이딩·영상 조작 등 처음 접하는 도메인에서 미지를 반복적으로 발견해 나갔다.

## 번들 리소스

- `skills/finding-your-unknowns/SKILL.md` — 전체 워크플로를 Agent Skill로 정리하고, 각 수마다 프롬프트 템플릿을 연결.
- `skills/finding-your-unknowns/references/four-unknowns.md` — 4분면 모델과 각 분면 공략법.
- `skills/finding-your-unknowns/templates/` — 블라인드 스팟 패스, 인터뷰, 구현 노트, 피치, 퀴즈용 붙여넣기 프롬프트.
- `skills/finding-your-unknowns/examples/launching-fable.md` — 런칭 영상 사례 연구.
- `guides/knowing-your-unknowns.ko.md` — 같은 내용을 서술형 가이드로, 4개 언어 제공.

## 출처

- [A Field Guide to Claude Fable 5: Finding Your Unknowns](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns) — 2026-07-06 게시
