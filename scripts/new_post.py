#!/usr/bin/env python3
"""
new_post.py – Tạo file bài viết mới từ template chuẩn.
// Dùng: python scripts/new_post.py "Tên bài viết của tôi"

Usage:
  python scripts/new_post.py "Tại sao Indie Hacker không cần marketing"
  python scripts/new_post.py "My new post" --stage drafts
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
TEMPLATE_FILE = ROOT / "templates" / "default.md"
STAGES = {
    "ideas": ROOT / "writing" / "0-ideas",
    "drafts": ROOT / "writing" / "1-drafts",
    "ready": ROOT / "writing" / "2-ready",
}


def slugify(text: str) -> str:
    """Chuyển tiêu đề thành slug URL-safe."""
    text = text.lower()
    # Chuyển ký tự tiếng Việt phổ biến sang dạng latin cơ bản
    viet_map = {
        "à": "a", "á": "a", "ả": "a", "ã": "a", "ạ": "a",
        "ă": "a", "ắ": "a", "ặ": "a", "ằ": "a", "ẵ": "a", "ẳ": "a",
        "â": "a", "ấ": "a", "ậ": "a", "ầ": "a", "ẫ": "a", "ẩ": "a",
        "đ": "d",
        "è": "e", "é": "e", "ẻ": "e", "ẽ": "e", "ẹ": "e",
        "ê": "e", "ế": "e", "ệ": "e", "ề": "e", "ễ": "e", "ể": "e",
        "ì": "i", "í": "i", "ỉ": "i", "ĩ": "i", "ị": "i",
        "ò": "o", "ó": "o", "ỏ": "o", "õ": "o", "ọ": "o",
        "ô": "o", "ố": "o", "ộ": "o", "ồ": "o", "ỗ": "o", "ổ": "o",
        "ơ": "o", "ớ": "o", "ợ": "o", "ờ": "o", "ỡ": "o", "ở": "o",
        "ù": "u", "ú": "u", "ủ": "u", "ũ": "u", "ụ": "u",
        "ư": "u", "ứ": "u", "ự": "u", "ừ": "u", "ữ": "u", "ử": "u",
        "ỳ": "y", "ý": "y", "ỷ": "y", "ỹ": "y", "ỵ": "y",
    }
    for viet, latin in viet_map.items():
        text = text.replace(viet, latin)
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def main():
    parser = argparse.ArgumentParser(description="Tạo bài viết mới từ template.")
    parser.add_argument("title", type=str, help="Tên bài viết (có thể tiếng Việt).")
    parser.add_argument(
        "--stage",
        choices=list(STAGES.keys()),
        default="drafts",
        help="Giai đoạn ban đầu (mặc định: drafts).",
    )
    args = parser.parse_args()

    slug = slugify(args.title)
    today = date.today().isoformat()
    dest_dir = STAGES[args.stage]
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_file = dest_dir / f"{slug}.md"

    if dest_file.exists():
        print(f"⚠️  File đã tồn tại: {dest_file}")
        sys.exit(1)

    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    content = template.replace('YYYY-MM-DD', today)
    content = content.replace('tua-de-bai-viet', slug)
    content = content.replace('Tựa đề bài viết (viết ngắn gọn, gợi sự tò mò)', args.title)

    dest_file.write_text(content, encoding="utf-8")
    print(f'✅ Đã tạo: {dest_file.relative_to(ROOT)}')
    print(f'   Title:  "{args.title}"')
    print(f'   Slug:   {slug}')


if __name__ == "__main__":
    main()
