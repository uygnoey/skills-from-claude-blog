[English](./skills-deployment-paths.en.md) · **한국어** · [Español](./skills-deployment-paths.es.md) · [日本語](./skills-deployment-paths.ja.md)

## 이 가이드는 뭔가요
이 가이드는 원문에서 소개한 Claude 스킬의 주요 배포/관리 경로(Claude Apps, Claude Code, API)와 조직 단위 프로비저닝 개념을 요약합니다.

## 배포 경로
- **Claude Apps**: 스킬 디렉터리를 둘러보고 설정 > 기능(Capabilities) > 스킬(Skills)에서 활성화합니다.
- **Claude Code**: 플러그인 디렉터리에서 스킬을 설치하거나, 스킬 폴더를 리포지토리에 체크인합니다.
- **API**: `/v1/skills` 엔드포인트로 스킬을 사용합니다(플랫폼 문서 참고).

## 조직 단위 관리
- 관리자(Team/Enterprise)는 관리자 설정에서 스킬을 중앙 프로비저닝할 수 있습니다.
- 일부 스킬은 Code Execution 및 File Creation 활성화가 필요할 수 있습니다.

## 출처
- https://claude.com/blog/organization-skills-and-directory
