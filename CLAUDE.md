# 모아가이드 (MoaGuide) — Claude Code 작업 규칙

## 프로젝트 정보
- 수익형 정보 블로그 (Jekyll + Netlify)
- GitHub: galincia-hub/projects/blog/
- 로컬: C:\Vs\projects\blog\

## 글 생성 워크플로우
키워드를 받으면:
1. `_posts/` 에 `YYYY-MM-DD-slug.md` 생성 (frontmatter 포함)
2. `python scripts/generate_thumbnail.py` 실행 → 썸네일 PNG 생성
3. frontmatter `thumbnail` 필드에 경로 연결 (`/assets/images/thumbnails/slug.png`)
4. `git add → commit → push`

## 글 스타일
- IT수집가 스타일: 중립적 정보 전달, 깔끔한 구조
- 소제목(h2) → 설명 → 표/리스트 반복
- 첫 문단에서 검색 의도에 바로 답변
- 1,500~3,000자
- FAQ 섹션 포함 (해당되는 경우)

## frontmatter 필수 항목
```yaml
---
title: "글 제목"
date: YYYY-MM-DD
category: it  # it / life / finance / health / review
thumbnail: /assets/images/thumbnails/slug.png
description: "SEO용 요약 1~2문장"
tags: [키워드1, 키워드2]
---
```

## 썸네일 생성
```
python scripts/generate_thumbnail.py --title "제목" --category it --slug slug
```
저장 위치: `assets/images/thumbnails/slug.png`

## 카테고리 슬러그
- IT 정보 → `it`
- 생활 정보 → `life`
- 금융 정보 → `finance`
- 건강 정보 → `health`
- 제품 추천 → `review`

## git 규칙
- 커밋 메시지: `글 추가: 제목` 또는 `사이트 구조: 변경 내용`
- 글 추가 시 1글 1커밋
