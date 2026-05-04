# CTA 버튼 스킬 (cta.md)

## 기본 사용법
```liquid
{% include cta-button.html url="URL" text="버튼 텍스트" type="TYPE" affiliate="ID" %}
```

## 파라미터
| 파라미터 | 필수 | 설명 |
|---------|------|------|
| url | ✓ | 이동 URL (tel: 형태 가능) |
| text | ✓ | 버튼 표시 텍스트 |
| type | - | download / link / phone / form (기본: link) |
| affiliate | - | 제휴 파트너 ID → data-affiliate 속성으로 렌더링 |

## type별 아이콘 & 색상
| type | 아이콘 | 버튼 색상 기준 |
|------|--------|------------|
| download | ↓ | 카테고리 색상 |
| link | → | 카테고리 색상 |
| phone | 📞 | 카테고리 색상 |
| form | 📄 | 카테고리 색상 |

## 배치 규칙
- **상단 CTA**: 도입부 직후 (첫 h2 이전)
- **하단 CTA**: 마무리 문장 직전
- 글 1편당 최소 2개 (애드센스 승인 전 필수)
- 적절한 섹션에 3번째 CTA 추가 가능

## 제휴 연동 준비
버튼 클릭 이벤트는 data-affiliate 속성으로 구분:
```js
document.querySelectorAll('[data-affiliate]').forEach(btn => {
  btn.addEventListener('click', e => {
    const partner = e.currentTarget.dataset.affiliate;
    // 배너 팝업 또는 리다이렉트 처리
  });
});
```

## 변경이력
| 날짜 | 변경 내용 | 사유 |
|------|---------|------|
| 2026-05-04 | 초안 작성 | CTA 시스템 구축 |
| 2026-05-04 | type=form 추가, 카테고리 색상 적용 | 스킬 고도화 |
