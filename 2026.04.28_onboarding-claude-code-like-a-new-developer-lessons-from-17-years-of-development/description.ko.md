[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Brendan MacLean(워싱턴대학교 MacCoss Lab)이 대규모·장수 코드베이스에 새 개발자를 온보딩하듯, Claude Code도 동일한 방식으로 온보딩하는 방법을 설명합니다. 핵심은 컨텍스트와 프로세스 문서를 “프로젝트 아티팩트”로 취급해 버전 관리하며 축적하는 것입니다.

## 언제 유용한가요
- 암묵지(숨은 규칙/전제)가 많은 큰 저장소에서 Claude Code가 효율적으로 일해야 할 때
- 팀 구성원이 자주 바뀌는 환경(학생/오픈소스 기여자 등)에서 반복 가능한 온보딩이 필요할 때
- 코드를 고치기 전마다 설명을 다시 해야 하는 비용을 줄이기 위해, 지속 가능한 컨텍스트를 코드와 함께 관리하고 싶을 때

## 핵심 포인트
- 별도의 “AI 컨텍스트” 저장소(글의 예시는 `pwiz-ai`)를 운영해 브랜치 변동과 무관하게 지침이 축적·개선되도록 합니다.
- 저장소 루트에 `CLAUDE.md`를 두고 개발 환경 설정과 주요 문서 링크를 안내합니다(“embed 대신 reference”).
- 반복되는 작업 패턴(예: 디버깅, 버전 관리 규약, 프로젝트 개요)을 스킬 라이브러리로 정리합니다.
- 통합(글에서는 MCP 서버)을 활용해 테스트 결과, 예외, 지원 스레드, 릴리스 태그 같은 프로젝트 데이터에 Claude Code가 접근할 수 있게 합니다.

## 번들 리소스
- 글에 별도의 첨부 파일은 없으며, `CLAUDE.md` 및 보조 저장소(`pwiz-ai`) 같은 프로젝트 아티팩트를 예시로 언급합니다.

## 출처
- https://claude.com/blog/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development
