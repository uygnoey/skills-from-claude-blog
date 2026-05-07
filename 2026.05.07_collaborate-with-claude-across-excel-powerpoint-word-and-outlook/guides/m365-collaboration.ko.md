[English](./m365-collaboration.en.md) · **한국어** · [Español](./m365-collaboration.es.md) · [日本語](./m365-collaboration.ja.md)

# Claude와 함께하는 Microsoft 365 앱 간 워크플로

## 이 가이드는 뭔가요
Excel, PowerPoint, Word, Outlook에서 Claude와 협업할 때 하나의 대화 맥락을 유지하면서 작업을 이어가는 방법을 짧고 실용적으로 정리한 가이드입니다.

## 권장 워크플로
1. **메일 → 첨부 → 분석 → 서술 → 발표자료**
   - Outlook에서 요청을 먼저 파악합니다.
   - 첨부 파일을 Word/Excel에서 열어 요청 맥락을 유지합니다.
   - Excel에서 분석하고, Word에서 서술을 작성한 뒤, PowerPoint에서 자료를 만듭니다.

2. **산출물을 나란히 열어두기**
   - 가능하면 스프레드시트, 메모, 발표자료를 동시에 열어둡니다.
   - 가정이 바뀌면 차트와 서술의 의존 부분을 함께 갱신합니다.

3. **Outlook 초안을 ‘마지막 단계’로 사용하기**
   - Claude가 회신과 일정 초대를 초안으로 작성하게 합니다.
   - 전송 전에는 반드시 사람이 검토합니다.

## 관리자 관점 고려사항(엔터프라이즈)
- 배포는 Microsoft 관리 도구 및 AppSource 기반으로 진행할 수 있습니다.
- 조직은 OpenTelemetry 기반 관측 가능성과 Analytics API 기반 사용량 리포팅을 설정할 수 있습니다.

## 출처
- https://claude.com/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook
