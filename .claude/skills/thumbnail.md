# 썸네일 생성 스킬 (thumbnail.md)

## 생성 명령
```bash
python scripts/generate_thumbnail.py --title "제목" --category CATEGORY --slug slug
```

## 스펙
- 크기: 800 × 420px
- 저장: assets/images/thumbnails/slug.png
- 구성: 배경(카테고리 색) + 카테고리 뱃지 + 타이틀(최대 3줄) + 사이트 URL

## 카테고리 색상
| 카테고리 | slug | 배경 | 액센트 | 뱃지 |
|---------|------|------|--------|------|
| IT 정보 | it | #2D5016 | #8BC34A | #4CAF50 |
| 생활 정보 | life | #1A237E | #64B5F6 | #2196F3 |
| 금융 정보 | finance | #E65100 | #FFB74D | #FF9800 |
| 건강 정보 | health | #880E4F | #F48FB1 | #E91E63 |
| 제품 추천 | review | #4A148C | #CE93D8 | #9C27B0 |

## 폰트 탐색 순서 (Windows)
1. NotoSansCJK-Bold.ttc / NotoSansKR-Bold.otf
2. malgunbd.ttf (맑은 고딕 Bold)
3. gulimche.ttf

## frontmatter 연결
```yaml
thumbnail: /assets/images/thumbnails/slug.png
```

## 변경이력
| 날짜 | 변경 내용 | 사유 |
|------|---------|------|
| 2026-05-04 | 초안 작성 | Phase 1 시스템 구축 |
