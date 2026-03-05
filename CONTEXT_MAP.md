# 🗺️ CONTEXT MAP (For AI Assistant)

> **File quan trọng nhất dành cho AI Agent (Copilot, Kilo, Claude) khi vào repo này. Đọc file này TRƯỚC KHI làm bất kỳ hành động nào.**

---

## 🧭 Navigation Guide (AI: Đọc theo thứ tự này)

| Ưu tiên | File | Dùng khi |
|---------|------|----------|
| 1 | `context/profile.md` | LUÔN đọc — Persona, tone giọng, phong cách viết của tác giả |
| 2 | `context/audience.md` | Cần biết viết cho ai trên từng platform |
| 3 | `context/platforms.md` | Khi Format/Rewrite bài — rule riêng từng nền tảng |
| 4 | `context/topics.md` | Khi hỏi về kế hoạch nội dung, series nào đang có, bài nào trong hàng chờ |
| 5 | `WORKFLOW.md` | Khi hỏi về quy trình viết bài hoặc di chuyển file giữa các stage |

---

## ⚙️ Workflow Rules (Bất biến)

- **Không tự ý di chuyển file**: AI chỉ đề xuất, không tự move file giữa stages. Phải được phép.
- **Formatting chuẩn MXH**: Xuống dòng sau mỗi 1-2 câu. Nhiều khoảng trắng hơn paragraphs dài.
- **Frontmatter bắt buộc**: Mọi file `.md` trong `writing/` phải có YAML Frontmatter theo `templates/default.md`.
- **Series Footer**: Cuối mỗi bài trong Series phải có footer dẫn link tập trước/sau.

---

## 🛠️ Scripts Có Sẵn

| Script | Lệnh | Chức năng |
|--------|------|-----------|
| `new_post.py` | `python scripts/new_post.py "Tên bài"` | Tạo file bài mới từ template |
| `formatter.py` | `python scripts/formatter.py writing/2-ready/ten-bai.md` | Format bài cho tất cả platform |
| `formatter.py` | `python scripts/formatter.py writing/2-ready/ten-bai.md --platform linkedin` | Format 1 platform cụ thể |

---

## 📁 Cấu trúc thư mục

```
social-writing-vault/
├── CONTEXT_MAP.md    # File này — AI đọc đầu tiên
├── WORKFLOW.md       # Vòng đời bài viết 5 bước
├── context/
│   ├── profile.md    # Persona + tone giọng tác giả
│   ├── audience.md   # Target audience từng platform
│   ├── platforms.md  # Format rule cho LinkedIn/X/Medium/Facebook
│   └── topics.md     # Kế hoạch Series + Outline từng bài
├── writing/
│   ├── 0-ideas/      # Ý tưởng + scaffold các tập series (chưa viết)
│   ├── 1-drafts/     # Đang viết
│   ├── 2-ready/      # Hoàn chỉnh, chờ format/post
│   └── 3-published/YYYY/MM/  # Đã đăng (lưu trữ)
├── assets/{post-slug}/  # Hình ảnh theo từng bài
├── scripts/
│   ├── new_post.py   # Tạo bài mới từ template
│   └── formatter.py  # Format Markdown → LinkedIn/X/Medium/Facebook
└── templates/
    └── default.md    # Template chuẩn có Frontmatter + Series metadata
```

---

## 📚 Series Hiện Có (Quick Reference)

| Series | Tập | File trong writing/0-ideas/ |
|--------|-----|--------------------------|
| **S1: Co-work Với AI Agent** | Prequel (Tập 0) | `series1-tap0-prequel.md` ← **Viết trước nhất** |
| | Tập 1 — Vai trò PM | `series1-tap1-pm.md` |
| | Tập 2 — Vai trò Architect | `series1-tap2-architect.md` |
| | Tập 3 — Vai trò QA | `series1-tap3-qa.md` |
| | Tập 4 — Vai trò UX | `series1-tap4-ux.md` |
| | Tập 5 — Context Engineering | `series1-tap5-context-eng.md` |
| **S2: Build In Public** | Tập 1 — Ship App đầu tiên | *(chưa tạo file)* |
| **S3, S4** | Nhiều tập | *(parked, xem topics.md)* |

> **AI**: Khi user hỏi "viết bài tiếp theo", hãy check `context/topics.md` để xác định đúng tập đang trong hàng chờ, sau đó mở đúng scaffold file tương ứng ở trên.
