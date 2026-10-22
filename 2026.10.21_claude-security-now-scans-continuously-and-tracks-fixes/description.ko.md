[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Claude Enterprise 대상 퍼블릭 베타로 나온 Claude Security 업데이트입니다. 누군가 스캔을 시작하기를
기다리는 대신, 코드가 바뀔 때마다 리포지토리를 따라가고, 어떤 발견 사항이 수정됐는지 추적하며,
팀이 알려 준 환경 정보를 바탕으로 무엇이 중요한지 판단합니다.

## 언제 유용한가요
- Enterprise 보안 팀이 일정을 잡지 않아도 최신 상태를 유지하는 스캔을 원할 때.
- 발견 사항의 우선순위를 정하려면 팀 맥락(배포 방식, 정책, 리스크 정책)이 필요할 때.
- 엔지니어가 Claude Code에서 바로 분류·수정하거나 기존 도구로 발견 사항을 보내고 싶을 때.

## 핵심 포인트
- 지속 모니터링: 심층 기준선 스캔 후, 변경 사항을 위험도와 복잡도에 따라 정기적으로 스캔. Claude
  GitHub 앱(GitHub Enterprise Server 포함)이나 GitLab·기타 Git 제공자 토큰으로 연결. 한 프로젝트에
  여러 리포를 묶어 서비스 사이의 문제도 찾음.
- 수정 추적: 수정이 반영되면(Claude Code든 다른 곳이든) 자동으로 fixed 처리, 문제가 다시 나타나면
  자동으로 재오픈.
- 프로젝트별 지식 베이스와, 자동 생성되고 팀이 편집할 수 있는 위협 모델. 이후 스캔은 이를 근거로
  무엇을 보고하고 무엇을 건너뛸지 결정.
- 모든 발견 사항에 위협 모델 기준 심각도와 공격 경로 설명(때로 다이어그램 포함).
- API(프로젝트·발견 사항 조회, 해결/재오픈, 리포 관리), 사용자 권한 범위로 제한되는 개인 액세스
  토큰, 새 발견 사항 웹훅, Claude.ai·Claude Code용 MCP 커넥터.
- 역할 기반 접근 제어: 프로젝트 조회, 발견 사항 분류, 프로젝트 생성 권한을 분리.
- Claude Mythos를 포함한 전체 모델 제품군으로 동작하며 Cyber Verification Program 접근 불필요.
  두 달간 매월 $25,000 무료 사용 크레딧(2026년 12월 31일까지의 사용분, 세부는 Help Center).

## 번들 리소스
- Skill: `continuous-security-scanning` — 활성화, 역할, 프로젝트, 지식 베이스, 위협 모델, 분류,
  수정 추적, 연동 (`references/feature-reference.md`, `templates/project-knowledge-base.md`).

## 출처
- https://claude.com/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes
