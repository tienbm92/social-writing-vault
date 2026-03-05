# 🔖 Quy tắc lưu trữ Assets (Hình ảnh / Video)

## Cấu trúc thư mục

Hình ảnh / Video được lưu theo slug của bài viết tương ứng:

```
assets/
└── {post-slug}/
    ├── cover.png          # Ảnh bìa (ưu tiên 1200x630px cho social)
    ├── diagram-1.png
    └── screenshot-1.png
```

## Quy tắc đặt tên file

- Viết thường, dùng dấu gạch ngang thay dấu cách: `thiet-ke-clean-arch.png`
- Tên file mô tả nội dung: `revenue-chart-q1-2026.png` ✅  — `image1.png` ❌
- Format ưu tiên: `png` cho screenshot/diagram, `webp` hoặc `jpg` cho ảnh lớn.

## Giới hạn kích thước

- Cover image (LinkedIn/Facebook): **1200 x 630px**
- Square image (Instagram): **1080 x 1080px**
- Ảnh trong bài Medium: **1200px rộng** (chiều cao tự do)

---
> ⚠️ **Không commit ảnh nặng > 5MB vào repo**. Upload lên Imgur, Cloudflare Images hoặc GitHub CDN và dùng link embed thay thế.
