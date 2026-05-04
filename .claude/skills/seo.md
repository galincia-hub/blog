# SEO 스킬 (seo.md)

## 기본 설정 (Jekyll 플러그인)
- jekyll-sitemap: sitemap.xml 자동 생성
- jekyll-seo-tag: 메타태그 자동 삽입
- jekyll-feed: RSS 피드 자동 생성

## frontmatter SEO 필수 항목
```yaml
title: "핵심 키워드 포함 제목 | 모아가이드"
description: "검색 결과에 표시될 요약 (120자 이내, 핵심 키워드 포함)"
tags: [키워드1, 키워드2, 키워드3]
last_updated: YYYY-MM-DD
```

## 시멘틱 HTML 구조 (애드센스+SEO 공통)
구글 크롤러는 시멘틱 태그 구조로 페이지 주제와 정보성을 판단한다.
레이아웃에서 준수 중인 구조:
- 네비게이션: `<nav class="site-nav">`
- 본문: `<main class="container">` → `<article>` 내부 배치
- 각 페이지 고유한 `<title>`과 `<meta name="description">` 필수
- footer에 About, Privacy, Contact 링크 포함

## 콘텐츠 신선도 관리
- frontmatter에 `last_updated` 필드 추가 (글 수정 시 반드시 갱신)
- post.html에서 자동 표시: "최종 업데이트: YYYY년 M월 D일"
- 수정 없이 날짜만 바꾸는 행위 금지

## 이미지 SEO
- 모든 이미지에 구체적 ALT 텍스트 필수 (빈 ALT 금지)
- ALT 형식: "서비스명 기능설명 스크린샷 연도"
- 예: "한컴오피스 다운로드 페이지 스크린샷 2026"
- 썸네일 ALT: `alt="{{ page.title }}"` (post.html에서 자동 처리)

## 내부 링크 전략
- 글 하단 related-posts.html: 같은 카테고리 글 최대 4개 자동 노출
- 본문 중 관련 키워드 등장 시 해당 글로 자연스러운 내부 링크
- 고아 페이지(내부 링크 0개) 방지
- 카테고리 뱃지 → 카테고리 페이지 링크 (post.html에서 처리)

## URL 구조
- 영문 슬러그 사용 (한글 URL 금지)
- 형식: /posts/keyword-slug/
- 슬러그에 핵심 키워드 포함

## Schema.org
- Article: 모든 글 공통
- FAQPage: FAQ 섹션 있는 글 (faq frontmatter 사용)
- SoftwareApplication: 유틸리티 다운로드 글
- HowTo: 설치/사용법 가이드 글

## 변경이력
| 날짜 | 변경 내용 | 사유 |
|------|---------|------|
| 2026-05-04 | 초안 작성 | Phase 1 시스템 구축 |
| 2026-05-04 | 시멘틱 HTML, 콘텐츠 신선도, 이미지 SEO, 내부 링크 전략 추가 | Phase 1 고도화 |
