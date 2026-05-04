# 모아가이드 (MoaGuide) — Claude Code 작업 규칙

## 프로젝트 정보
- 수익형 정보 블로그 (Jekyll + Netlify)
- GitHub: galincia-hub/blog
- 로컬: C:\Vs\projects\blog\

---

## 시스템 자기 진화 규칙

이 프로젝트의 글쓰기 시스템은 피드백을 통해 지속적으로 발전한다.

### 피드백 수렴 원칙
- 사용자가 글에 대해 수정 피드백을 주면, 해당 글만 수정하는 게 아니라
  원인이 되는 스킬 파일도 함께 업데이트한다.
- "이런 식으로 써줘" → writing.md에 규칙 추가
- "CTA가 이상해" → cta.md 수정
- "SEO가 부족해" → seo.md 보강
- "새로운 유형의 규칙이 필요해" → 새 스킬 파일 생성

### 스킬 수정 시 규칙
- 수정 전 기존 내용을 주석으로 보존 (`<!-- 이전: ... -->`)
- 수정 이유를 스킬 파일 하단 변경이력에 기록
- 변경이력 형식: `| 날짜 | 변경 내용 | 사유 |`

### 새 스킬 추가 시 규칙
- `.claude/skills/` 폴더에 생성
- CLAUDE.md의 스킬 목록에 경로 추가
- 기존 스킬과 역할 충돌 없는지 확인

### 스킬 현황 보고
사용자가 "스킬 현황" 또는 "시스템 상태"라고 하면
`.claude/skills/` 폴더의 모든 스킬 파일 목록과 마지막 수정일을 표시한다.

---

## 애드센스 승인 모드 (현재 활성)

애드센스 승인이 완료될 때까지 모든 글 작성에 `.claude/skills/adsense.md`를 강제 적용한다.
글 생성 완료 후 adsense.md의 자기 검증 체크리스트를 반드시 실행하고,
하나라도 미통과 시 수정 후 저장한다.
사용자가 **"애드센스 승인됨"** 이라고 알리면 이 강제 모드를 해제한다.

---

## 스킬 목록

| 스킬 | 파일 | 역할 |
|------|------|------|
| 글쓰기 | `.claude/skills/writing.md` | 글 구조, 톤, 유형별 포인트 |
| CTA 버튼 | `.claude/skills/cta.md` | 버튼 컴포넌트 사용법, 배치 규칙 |
| 썸네일 | `.claude/skills/thumbnail.md` | 자동 생성 스크립트, 색상 테마 |
| SEO | `.claude/skills/seo.md` | 메타태그, 시멘틱 구조, 내부 링크 |
| AEO/GEO | `.claude/skills/aeo.md` | AI 인용 최적화, FAQ, 스키마 |
| 리뷰/검수 | `.claude/skills/review.md` | 팩트 검증, 품질 체크리스트 |
| 애드센스 | `.claude/skills/adsense.md` | 승인 요건, 글 자기 검증 체크리스트 |

---

## 글 생성 워크플로우

키워드를 받으면:
1. `.claude/skills/writing.md` 참고하여 `_posts/YYYY-MM-DD-slug.md` 작성
2. `python scripts/generate_thumbnail.py --title "제목" --category CAT --slug slug` 실행
3. frontmatter `thumbnail` 필드에 경로 연결
4. `.claude/skills/adsense.md` 자기 검증 체크리스트 실행 (승인 전 필수)
5. `git add → commit → push`

---

## frontmatter 필수 항목

```yaml
---
title: "글 제목"
date: YYYY-MM-DD
last_updated: YYYY-MM-DD
category: it  # it / life / finance / health / review
thumbnail: /assets/images/thumbnails/slug.png
description: "SEO용 요약 1~2문장 (120자 이내)"
tags: [키워드1, 키워드2]
---
```

---

## 카테고리 슬러그

| 카테고리 | slug |
|---------|------|
| IT 정보 | `it` |
| 생활 정보 | `life` |
| 금융 정보 | `finance` |
| 건강 정보 | `health` |
| 제품 추천 | `review` |

---

## git 규칙
- 커밋 메시지: `글 추가: 제목` / `사이트 구조: 변경 내용` / `스킬 업데이트: 파일명`
- 글 추가 시 1글 1커밋
- 스킬 파일 수정 시 별도 커밋
