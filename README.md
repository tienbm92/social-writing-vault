# social-writing-vault

> **Repo chuyên dụng để quản lý Content, Bản thảo (Drafts) và các Script tự động phục vụ cho việc viết bài định kỳ.**

## Mục đích

Hệ thống này giúp tách biệt rạch ròi giữa:

- **Ý tưởng thô (Ideas)**
- **Bản thảo đang viết (Drafts)**
- **Bài viết đã hoàn thành & chờ post (Ready)**
- **Bài viết đã xuất bản (Published)**

Đồng thời tập trung các context về "giọng văn", "phong cách", "độc giả mục tiêu" ở một nơi duy nhất để AI dễ dàng tham chiếu, hiểu được người viết và hỗ trợ Rewrite, Format chính xác nhất.

## Cấu trúc thư mục

```bash
social-writing-vault/
├── context/         # AI Context: chứa rule, profile, master prompt
├── writing/         # Content Pipeline
│   ├── 0-ideas/     # Các ý tưởng lóe lên, chưa thành hình
│   ├── 1-drafts/    # Đang phát triển thành bài hoàn chỉnh
│   ├── 2-ready/     # Hoàn thiện 100%, chờ script format/post
│   └── 3-published/ # Lưu trữ lại bài đã đăng
├── assets/          # Hình ảnh/Video minh họa (đặt theo slug bài)
├── scripts/         # Các Script tự động (Python/Node)
└── templates/       # Mẫu MD có Frontmatter chuẩn
```

## Cách sử dụng cơ bản

1. Copy file `templates/default.md` vào `writing/0-ideas/` hoặc `writing/1-drafts/`
2. Viết nội dung bằng Markdown (có thể dùng VS Code, Obsidian,...).
3. Đọc `CONTEXT_MAP.md` để biết cách AI (ví dụ Kilo/Copilot) có thể tương tác với repo này.
