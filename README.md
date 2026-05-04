# 모아가이드 (MoaGuide)

구글 검색 유입 기반 수익형 정보 블로그.

## 기술 스택
- Jekyll 4.4 + Netlify
- Python + Pillow (썸네일 자동 생성)

## 로컬 실행
```
bundle install
bundle exec jekyll serve
```
http://localhost:4000 접속

## 글 생성
```
python scripts/generate_thumbnail.py --title "제목" --category it --slug my-slug
```
이후 `_posts/YYYY-MM-DD-my-slug.md` 작성

## 카테고리
- `it` — IT 정보
- `life` — 생활 정보
- `finance` — 금융 정보
- `health` — 건강 정보
- `review` — 제품 추천
