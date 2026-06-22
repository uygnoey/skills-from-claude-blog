[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 AWS, Google Cloud, Microsoft Foundry를 통해 Claude Desktop을 사용하는 조직이 이제 하나의 앱에서 전체 Desktop 경험(채팅, Claude Cowork, Claude Code)을 모두 사용할 수 있게 되었음을 알립니다.

## 언제 유용한가요
클라우드 내 추론을 유지하면서, 엔터프라이즈 계정/디바이스 관리 체계로 Claude Desktop을 조직 전체에 배포하려는 관리자 또는 IT·보안 담당자에게 유용합니다.

## 핵심 포인트
- 이제 단일 배포로 채팅, Claude Cowork, Claude Code를 모두 제공하며, 각 표면(surface)별로 정책 키가 분리되어 누가 무엇을 사용할지 제어할 수 있습니다.
- 구성원은 공유 키 대신 기존 엔터프라이즈 ID 공급자(IAM Identity Center, Microsoft Entra ID, 기타 OIDC 공급자 등)로 로그인합니다.
- 관리자는 설정 UI에서 정책 템플릿을 내보내 Intune, GPO, Jamf 등 일반적인 MDM/엔드포인트 관리 도구로 배포할 수 있으며, 에어갭 환경을 위한 오프라인 설치 옵션도 언급됩니다.
- 배포 전 검증으로 커넥터 테스트, 제공되는 Claude 모델 확인, 연결 검증을 수행하며, 설정 오류가 있어도 Claude로 라우팅을 유지하도록 돕는 “model guard”가 설명됩니다.
- Microsoft 365는 자체 Entra 앱을 사용한 커넥터(테넌트 허용 목록 포함)로 연결할 수 있고, 엄격한 레지던시 요구사항을 위한 로컬 커넥터 옵션도 언급됩니다.

## 번들 리소스
- 글은 정책 템플릿(설정 UI에서 내보내기)과 관리자용 배포 가이드(SSO, 정책 템플릿, 사전 검증)를 참조합니다.

## 출처
- https://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry
