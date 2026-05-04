# AEO/GEO 스킬 (aeo.md)
## Answer Engine Optimization + Generative Engine Optimization

## GEO 핵심 원칙
AI(ChatGPT, Gemini, Perplexity 등)는 첫 문단에서 답을 추출하고 나머지를 보조 정보로 취급한다.

### 첫 문단 작성 원칙
- 2~3문장으로 질문에 직접 답하는 완전한 문장
- 공식 URL 또는 서비스명 명시 포함
- 나쁜 예: "한컴오피스에 대해 알아보겠습니다."
- 좋은 예: "한컴오피스를 무료로 사용하려면 공식 사이트(hancom.com)에서 한글 뷰어를 다운로드하거나 한컴독스 웹 버전을 이용하면 됩니다."

## AI 인용률 높이는 구현 기법
| 기법 | 효과 | 구현 방법 |
|------|------|---------|
| FAQPage 스키마 | 인용률 최대 67% 향상 | faq frontmatter + schema.html |
| 비교 표 | AI가 표 데이터 잘 파싱 | 모든 글에 최소 1개 표 |
| 구조화된 리스트 | 단계별 가이드 파싱 용이 | 순서 있는 `ol/li` 마크업 |
| 구체적 수치 | 신뢰도 향상 | "많은" 대신 "5가지" |
| 날짜 명시 | 최신성 인정 | "2026년 5월 기준" |

## Schema.org 다중 스킴 활용
```yaml
# frontmatter 예시
schema_type: software_faq    # Article + FAQPage + SoftwareApplication
schema_type: howto_faq       # Article + FAQPage + HowTo
schema_type: article_faq     # Article + FAQPage (기본)
```

## 엔티티 일관성 강화
- 첫 등장 시 정식 명칭: "한컴오피스(Hancom Office)"
- 이후 동일 명칭만 사용
- 약칭·별칭·오타 혼용 절대 금지
- 공식 사이트 URL 일관 표기

## FAQ 작성 원칙
- 실제 검색되는 질문 형식 (구글 '사람들이 묻는 질문' 참고)
- 답변은 2~3문장, 완결된 정보
- 3~5개 FAQ 권장
- faq frontmatter 형식으로 Schema.org FAQPage 자동 생성:
```yaml
faq:
  - q: "질문?"
    a: "답변"
```

## 변경이력
| 날짜 | 변경 내용 | 사유 |
|------|---------|------|
| 2026-05-04 | 초안 작성 | Phase 1 시스템 구축 |
| 2026-05-04 | GEO 원칙, AI 인용률 기법, 엔티티 일관성 추가 | Phase 1 고도화 |
