#!/usr/bin/env python3
"""
모아가이드 썸네일 자동 생성 스크립트
사용법: python generate_thumbnail.py --title "제목" --category it --slug my-post
"""
import argparse
import os
import math
from PIL import Image, ImageDraw, ImageFont

THEMES = {
    "it":      {"bg": "#2D5016", "accent": "#8BC34A", "badge": "#4CAF50", "label": "IT 정보"},
    "life":    {"bg": "#1A237E", "accent": "#64B5F6", "badge": "#2196F3", "label": "생활 정보"},
    "finance": {"bg": "#E65100", "accent": "#FFB74D", "badge": "#FF9800", "label": "금융 정보"},
    "health":  {"bg": "#880E4F", "accent": "#F48FB1", "badge": "#E91E63", "label": "건강 정보"},
    "review":  {"bg": "#4A148C", "accent": "#CE93D8", "badge": "#9C27B0", "label": "제품 추천"},
}

W, H = 800, 420
SITE_URL = "moaguide.com"


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def draw_circle(draw, cx, cy, r, color, alpha=40):
    """반투명 원형 도형"""
    r_color = hex_to_rgb(color) + (alpha,)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=r_color)


def get_font(size, bold=False):
    """시스템 폰트 탐색 — Noto Sans CJK → 맑은 고딕 → 기본"""
    candidates = []
    if bold:
        candidates = [
            r"C:\Windows\Fonts\NotoSansCJK-Bold.ttc",
            r"C:\Windows\Fonts\NotoSansKR-Bold.otf",
            r"C:\Windows\Fonts\malgunbd.ttf",
            r"C:\Windows\Fonts\gulimche.ttf",
        ]
    else:
        candidates = [
            r"C:\Windows\Fonts\NotoSansCJK-Medium.ttc",
            r"C:\Windows\Fonts\NotoSansKR-Medium.otf",
            r"C:\Windows\Fonts\malgun.ttf",
            r"C:\Windows\Fonts\gulim.ttc",
        ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def wrap_text(draw, text, font, max_width):
    """텍스트를 max_width에 맞게 줄 분리"""
    lines = []
    words = list(text)  # 한글은 문자 단위 분리
    # 단어 단위(스페이스 기준)로 먼저 분리
    space_words = text.split()
    current = ""
    for word in space_words:
        test = (current + " " + word).strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines[:3]  # 최대 3줄


def generate(title, category, slug, output_dir):
    theme = THEMES.get(category, THEMES["it"])
    bg_rgb = hex_to_rgb(theme["bg"])
    accent_rgb = hex_to_rgb(theme["accent"])

    # RGBA 캔버스
    img = Image.new("RGBA", (W, H), bg_rgb + (255,))
    draw = ImageDraw.Draw(img, "RGBA")

    # 배경 장식 원
    draw_circle(draw, W - 60, 60, 160, theme["accent"], alpha=30)
    draw_circle(draw, W - 20, H - 20, 120, theme["accent"], alpha=20)
    draw_circle(draw, 30, H - 50, 100, theme["accent"], alpha=15)

    # 카테고리 뱃지
    badge_font = get_font(18, bold=True)
    badge_text = theme["label"]
    bx, by = 48, 48
    b_bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
    bw = b_bbox[2] - b_bbox[0] + 24
    bh = b_bbox[3] - b_bbox[1] + 12
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=8, fill=hex_to_rgb(theme["badge"]) + (255,))
    draw.text((bx + 12, by + 6), badge_text, font=badge_font, fill=(255, 255, 255, 255))

    # 메인 타이틀
    title_font = get_font(42, bold=True)
    max_w = W - 96
    lines = wrap_text(draw, title, title_font, max_w)

    line_h = 52
    start_y = 130
    for i, line in enumerate(lines):
        draw.text((48, start_y + i * line_h), line, font=title_font, fill=(255, 255, 255, 255))

    # 구분선
    line_y = start_y + len(lines) * line_h + 16
    draw.line([(48, line_y), (W - 48, line_y)], fill=hex_to_rgb(theme["accent"]) + (120,), width=2)

    # 사이트 URL
    url_font = get_font(20)
    draw.text((48, line_y + 16), SITE_URL, font=url_font, fill=hex_to_rgb(theme["accent"]) + (200,))

    # RGB로 변환 후 저장
    final = img.convert("RGB")
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{slug}.png")
    final.save(out_path, "PNG", optimize=True)
    print(f"[OK] {out_path}")
    return out_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--category", required=True, choices=THEMES.keys())
    parser.add_argument("--slug", required=True)
    parser.add_argument("--output-dir", default=r"C:\Vs\projects\blog\assets\images\thumbnails")
    args = parser.parse_args()
    generate(args.title, args.category, args.slug, args.output_dir)
