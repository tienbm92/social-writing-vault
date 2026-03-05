# 🗺️ CONTEXT MAP (For AI Assistant)

> **Mục Đích**: Đây là file quan trọng nhất dành cho các AI Agent (Copilot, Kilo, Claude) mỗi khi được gán vào repo này. File này hướng dẫn AI cách làm việc với thư mục và cách hiểu người viết.

---

## 🧭 Navigation Guide (AI: Đọc theo thứ tự này)

| Ưu tiên | File | Dùng khi |
|---------|------|----------|
| 1 | `context/profile.md` | Luôn đọc — để biết giọng văn và persona của người viết |
| 2 | `context/audience.md` | Cần biết viết cho ai trong từng bài/platform cụ thể |
| 3 | `context/platforms.md` | Khi Format/Rewrite bài cho 1 platform cụ thể (LinkedIn/X/Medium…) |
| 4 | `WORKFLOW.md` | Khi hỏi về quy trình viết bài hoặc di chuyển file giữa các stage |

---

## ⚙️ Workflow Rules (Quy trình)

- **Không tự ý di chuyển file**: AI chỉ đề xuất, không tự move file giữa các stage. Phải được phép.
- **Formatting**: Bài viết MXH cần nhiều khoảng trắng. Xuống dòng sau mỗi 1-2 câu.
- **Frontmatter bắt buộc**: Mọi file `.md` trong `writing/` phải có YAML Frontmatter đúng chuẩn template tại `templates/default.md`.

---

## 🛠️ Scripts Có Sẵn

| Script | Lệnh | Chức năng |
|--------|------|-----------|
| `new_post.py` | `python scripts/new_post.py "Tên bài"` | Tạo file bài mới từ template |
| `formatter.py` | `python scripts/formatter.py writing/2-ready/ten-bai.md` | Format bài cho tất cả platform |
| `formatter.py` | `python scripts/formatter.py writing/2-ready/ten-bai.md --platform linkedin` | Format cho 1 platform cụ thể |

---

## 📁 Cấu trúc thư mục

```
social-writing-vault/
├── context/          # AI Context (profile, audience, platforms)
├── writing/
│   ├── 0-ideas/      # Ý tưởng thô
│   ├── 1-drafts/     # Đang viết
│   ├── 2-ready/      # Chờ post
│   └── 3-published/YYYY/MM/  # Đã đăng (lưu trữ theo năm/tháng)
├── assets/{post-slug}/  # Hình ảnh theo bài
├── scripts/          # Automation scripts
└── templates/        # Template mẫu có Frontmatter
```
