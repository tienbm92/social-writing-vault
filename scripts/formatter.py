#!/usr/bin/env python3
"""
formatter.py – Format bài viết Markdown cho từng Social Platform.
// Dùng: python scripts/formatter.py <path_to_md> [--platform linkedin|x|medium|facebook]

Usage:
  python scripts/formatter.py writing/2-ready/ten-bai.md
  python scripts/formatter.py writing/2-ready/ten-bai.md --platform linkedin
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

# ─── Helper functions ────────────────────────────────────────────────────── #

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Tách frontmatter (YAML) và nội dung chính của file Markdown."""
    metadata = {}
    body = text
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            fm_block = text[3:end].strip()
            for line in fm_block.splitlines():
                if ":" in line:
                    key, _, val = line.partition(":")
                    metadata[key.strip()] = val.strip().strip('"\'')
            body = text[end + 3:].strip()
    return metadata, body


def strip_markdown(text: str) -> str:
    """Xóa cú pháp Markdown cơ bản để ra plain text thuần."""
    text = re.sub(r"#{1,6}\s+", "", text)          # Headings
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)   # Bold
    text = re.sub(r"\*(.*?)\*", r"\1", text)        # Italic
    text = re.sub(r"`(.*?)`", r"\1", text)          # Inline code
    text = re.sub(r"```[\s\S]*?```", "", text)      # Code blocks
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text) # Links → hiển thị text
    text = re.sub(r"^[-*]\s+", "• ", text, flags=re.MULTILINE)  # Bullets
    return text.strip()


def copy_to_clipboard(text: str):
    """Copy text vào clipboard macOS (pbcopy)."""
    try:
        subprocess.run("pbcopy", input=text.encode("utf-8"), check=True)
        print("✅ Đã copy vào Clipboard!")
    except FileNotFoundError:
        print("⚠️  pbcopy không có. Tự copy thủ công nhé.")


# ─── Platform Formatters ─────────────────────────────────────────────────── #

def format_linkedin(body: str, meta: dict) -> str:
    """
    LinkedIn: xuống dòng sau mỗi câu, không link trong bài.
    """
    text = strip_markdown(body)
    # Tách câu theo dấu chấm, chấm than, chấm hỏi → mỗi câu 1 dòng
    sentences = re.split(r"(?<=[.!?])\s+", text)
    lines = []
    for s in sentences:
        s = s.strip()
        if s:
            lines.append(s)
    result = "\n\n".join(lines)
    result += "\n\n#IndieHacker #iOSDev #BuildInPublic"
    return result.strip()


def format_x_thread(body: str, meta: dict) -> str:
    """
    X/Twitter Thread: cắt thành các tweet ≤ 280 ký tự, đánh số.
    """
    text = strip_markdown(body)
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    tweets = []
    for p in paragraphs:
        # Nếu đoạn quá dài, cắt tại khoảng trắng gần nhất trước 260 ký tự
        while len(p) > 260:
            cut = p.rfind(" ", 0, 260)
            if cut == -1:
                cut = 260
            tweets.append(p[:cut].strip())
            p = p[cut:].strip()
        if p:
            tweets.append(p)
    # Đánh số thread
    numbered = [f"{i+1}/{len(tweets)+1} {t}" for i, t in enumerate(tweets)]
    numbered.append(f"{len(tweets)+1}/{len(tweets)+1} Follow mình để cập nhật thêm 🚀")
    return "\n\n---\n\n".join(numbered)


def format_medium(body: str, meta: dict) -> str:
    """
    Medium: giữ nguyên Markdown. Thêm title làm H1.
    """
    title = meta.get("title", "Bài Viết")
    result = f"# {title}\n\n{body}"
    return result.strip()


def format_facebook(body: str, meta: dict) -> str:
    """
    Facebook: plain text, không Markdown, thân thiện hơn.
    """
    text = strip_markdown(body)
    # Giữ xuống dòng nhưng tối ưu readability
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return "\n\n".join(paragraphs)


FORMATTERS = {
    "linkedin": format_linkedin,
    "x": format_x_thread,
    "medium": format_medium,
    "facebook": format_facebook,
}

# ─── CLI Entry Point ──────────────────────────────────────────────────────── #

def main():
    parser = argparse.ArgumentParser(description="Format bài viết Markdown cho Social Media.")
    parser.add_argument("file", type=Path, help="Đường dẫn đến file Markdown.")
    parser.add_argument(
        "--platform",
        choices=list(FORMATTERS.keys()),
        default=None,
        help="Platform cần format. Nếu bỏ trống sẽ output tất cả.",
    )
    args = parser.parse_args()

    if not args.file.exists():
        print(f"❌ File không tồn tại: {args.file}")
        sys.exit(1)

    raw_text = args.file.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(raw_text)
    title = meta.get("title", args.file.stem)

    targets = [args.platform] if args.platform else list(FORMATTERS.keys())
    outputs = {}

    print(f'\n📝 Bài: "{title}"\n{"─" * 60}')
    for platform in targets:
        fn = FORMATTERS[platform]
        formatted = fn(body, meta)
        outputs[platform] = formatted
        print(f"\n▶ [{platform.upper()}]\n\n{formatted}\n")
        print("─" * 60)

    # Copy bản đầu tiên vào clipboard
    first_platform = targets[0]
    copy_to_clipboard(outputs[first_platform])
    print(f"\n📋 Clipboard chứa bản [{first_platform.upper()}]")


if __name__ == "__main__":
    main()
