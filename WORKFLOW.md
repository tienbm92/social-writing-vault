# 📋 Workflow: Vòng đời 1 bài viết

> **Tài liệu này mô tả quy trình từ khi "nảy ra ý tưởng" đến khi "bài đã được đăng" — giúp bạn đồng bộ tư duy và nhắc nhở các bước không bỏ sót.**

---

## 🗺️ Pipeline Tổng Quát

```
[Ý Tưởng] → [Bản Nháp] → [Hoàn chỉnh] → [Format] → [Đăng] → [Lưu Trữ]
 0-ideas      1-drafts     2-ready       (scripts)   (MXH)    3-published
```

---

## Bước 1 — Hứng ý tưởng (`0-ideas/`)

**Mục tiêu**: Ghi lại nhanh, không cần hoàn chỉnh. Xả vào đây rồi mới xử lý sau.

1. Copy file `templates/default.md` vào `writing/0-ideas/`.
2. Đặt tên theo slug: `tai-sao-indie-khong-can-mkt.md`.
3. Điền chỉ: `title`, `tags` và ghi vài dòng ý chính.
4. Không cần viết đầy đủ — chỉ cần capture đủ để sau này đọc lại hiểu ngay.

---

## Bước 2 — Viết bản nháp (`1-drafts/`)

**Mục tiêu**: Mở rộng ý tưởng thành bài viết có cấu trúc.

1. Move file từ `0-ideas/` sang `1-drafts/`.
2. Cập nhật `status: draft` trong Frontmatter.
3. Viết theo outline template: **Hook → Core Message → Story/Case → CTA**.
4. Không filter khi viết — cứ viết ra hết, chỉnh sửa ở bước sau.

**Lúc này có thể nhờ AI (ví dụ Kilo/Copilot) với prompt**:
> "Đọc file này, hãy đánh giá cấu trúc bài, chỉ ra điểm nào thiếu logic và đề xuất lại Hook mạnh hơn."

---

## Bước 3 — Hoàn chỉnh & Review (`2-ready/`)

**Mục tiêu**: Bài viết đạt "đăng được ngay" — không cần làm gì thêm về nội dung.

**Checklist trước khi chuyển sang `2-ready/`**:

- [ ] Hook có đủ mạnh không (câu đầu tiên)?
- [ ] Core Message rõ, 1 ý duy nhất?
- [ ] Có ít nhất 1 ví dụ/câu chuyện thực tế không?
- [ ] CTA cụ thể ở cuối bài chưa?
- [ ] Tone giọng đúng với `context/profile.md` chưa?

1. Move file từ `1-drafts/` sang `2-ready/`.
2. Cập nhật `status: ready`.
3. Xác định platform sẽ đăng (update `platforms:` trong Frontmatter).

---

## Bước 4 — Format & Đăng

**Mục tiêu**: Chạy script để tự động sinh ra bản text phù hợp từng nền tảng.

```bash
# Format tất cả platforms trong 1 lệnh
python scripts/formatter.py writing/2-ready/ten-bai-viet.md

# Format chỉ LinkedIn
python scripts/formatter.py writing/2-ready/ten-bai-viet.md --platform linkedin
```

Script sẽ:

- In ra console bản đã format theo từng platform.
- Copy bản đầu tiên vào Clipboard (sẵn sàng để paste).

---

## Bước 5 — Lưu trữ (`3-published/YYYY/MM/`)

**Mục tiêu**: Giữ lại bản gốc đã đăng, có ghi thêm ngày đăng và link bài.

1. Move file từ `2-ready/` sang `3-published/2026/03/`.
2. Cập nhật Frontmatter:

   ```yaml
   status: published
   published_at: 2026-03-05
   links:
     linkedin: https://www.linkedin.com/posts/...
     medium: https://medium.com/...
   ```
