# 📚 Topics & Series Master Plan

> **Single Source of Truth cho toàn bộ kế hoạch nội dung. AI đọc file này để biết series nào đang có, bài nào thuộc tập nào, và sườn từng bài ra sao.**

---

## 🗂️ Danh sách Series

| # | Series | Status | Platform chính |
|---|--------|--------|----------------|
| S1 | [Co-work với AI Agent](#series-1) | 🔥 Active — Viết ngay | LinkedIn + Medium + Hashnode |
| S2 | [Build In Public — Indie App](#series-2) | 🔄 Song song | LinkedIn + X + Medium |
| S3 | [Góc Nhìn Thực Tế Về AI](#series-3) | ⏳ Sau S1 có 2-3 bài | Medium + Dev.to |
| S4 | [Thiết Kế Sản Phẩm Một Mình](#series-4) | 🅿️ Parked | Medium |

---

## Distribution Strategy (Hub & Spoke)

```
Medium (bài chính, full version ~1500-2000 từ)
    ↑
    ├── LinkedIn (~200-300 từ tóm tắt + link)
    ├── Facebook (~100-150 từ tiếng Việt casual + link)
    ├── Hashnode (cross-post y hệt Medium, canonical → Medium)
    └── X/Twitter (Thread 5-7 tweets, tease story + link)
```

---

## 🎯 Series 1: "Co-work Với AI Agent — Khi Developer Trở Thành Người Ra Quyết Định" {#series-1}

> **Tagline**: *"AI là coder của bạn. Vậy bạn là ai?"*
> **Core Insight**: Khi AI đảm nhận vai trò "người viết code", người làm việc cùng AI buộc phải đồng thời là PM, Architect, QA, UX Designer và Tech Lead. Decision-making — không phải coding — mới là kỹ năng cốt lõi.

### Episode Map

| Tập | File | Tiêu đề | Core Message | Status |
|-----|------|---------|--------------|--------|
| **0** | `series1-tap0-prequel.md` | "Khi AI là Coder — Bạn Phải Trở Thành Tất Cả Những Người Còn Lại" | Overview: vai trò developer thay đổi hoàn toàn khi co-work với AI | `idea` → **Viết trước nhất** |
| **1** | `series1-tap1-pm.md` | "Làm PM Khi Co-work Với AI: Đặt Câu Hỏi Đúng Còn Quan Trọng Hơn Code Đúng" | Skill quan trọng nhất: Define rõ bài toán trước khi bảo AI làm gì | `idea` |
| **2** | `series1-tap2-architect.md` | "Làm Architect Khi Co-work Với AI: AI Làm Theo Bất Cứ Điều Bạn Nói — Kể Cả Khi Sai" | Decision về cấu trúc, trade-off. AI execute giỏi — nhưng execute cái gì? | `idea` |
| **3** | `series1-tap3-qa.md` | "Làm QA Khi Co-work Với AI: Tin Tưởng Nhưng Luôn Verify" | AI không tự biết nó sai. Reviewer là vai trò không thể bỏ | `idea` |
| **4** | `series1-tap4-ux.md` | "Làm UX Designer Khi Co-work Với AI: AI Không Biết Cảm Xúc Người Dùng" | Empathy, flow, storytelling — AI không có, người phải có | `idea` |
| **5** | `series1-tap5-context-eng.md` | "Context Engineering — Giải Pháp Cho Tất Cả Những Vấn Đề Trên" | Pull everything together. Giới thiệu AI_CONTEXT.md và hệ thống của tôi | `idea` |

### Lịch đăng gợi ý

- Tập 0: **Càng sớm càng tốt** (bài khai màn)
- Tập tiếp theo: Mỗi 2 tuần

### Sườn chi tiết Tập 0 (Bài viết đầu tiên)

```
TIÊU ĐỀ: Khi AI Là Coder Của Bạn —
          Bạn Phải Trở Thành Tất Cả Những Người Còn Lại

HOOK (~100 từ)
  "Tôi giao cho AI viết toàn bộ một màn hình iOS.
  Code chạy hoàn hảo. Nhưng sai hoàn toàn những gì tôi muốn.
  Lỗi không phải ở AI. Lỗi ở tôi —
  vì tôi vẫn nghĩ mình đang là một coder truyền thống."

PHẦN 1: Cái bẫy của Vibe Coding (~300 từ)
  - Developer thêm AI vào workflow nhưng giữ mindset cũ
  - "Tôi bảo nó làm, nó làm" — tư duy sai ở đâu?
  - Case study thực: một lần tôi bị AI dẫn đi lạc hoàn toàn

PHẦN 2: Vai trò developer thay đổi (~400 từ)
  Trước: Dev = người viết code
  Sau:   Dev = người đưa ra quyết định ở mọi tầng

  → PM: Cái gì? Tại sao? Cho ai? Scope đến đâu?
  → Architect: Cấu trúc thế nào? Trade-off là gì?
  → QA: Output này có đúng không? Đúng về mặt nào?
  → UX: Người dùng thực sự trải nghiệm gì?
  → Tech Lead: Tôi có đang dẫn AI đúng hướng không?

PHẦN 3: Decision Quality = Output Quality (~300 từ)
  - AI execute rất tốt — nhưng execute cái gì?
  - Bad decision → AI execute perfectly → Bad product
  - Kỹ năng cốt lõi không còn là coding, là decision-making

KẾT + CTA (~150 từ)
  - Loạt bài tiếp theo đi sâu vào từng vai trò
  - Tập 1: "Làm PM khi co-work với AI"
  - CTA: Follow để không bỏ lỡ
```

---

## 🏗️ Series 2: "Build In Public — Hành Trình Indie App Từ $0" {#series-2}

> **Tagline**: *"Không team, không marketing budget, không network. Chỉ có code, ASO và sự kiên trì."*
> **Format**: Monthly report thực tế (số liệu thật: downloads, revenue, ratings)

| Tập | Tiêu đề | Status |
|-----|---------|--------|
| 1 | "Ship App đầu tiên: Từ idea đến App Store — và đây là điều xảy ra" | `idea` |
| 2 | "ASO thực tế: Tôi làm gì để App được tìm thấy mà không tốn đồng nào" | `idea` |
| 3 | "Tháng đầu tiên: Download, Revenue, Bài học" | `idea` |
| 4+ | Monthly Build In Public Report | `recurring` |

---

## 📡 Series 3: "Góc Nhìn Thực Tế Về AI Trong Công Việc Dev" {#series-3}

> **Viết sau khi Series 1 có ít nhất 2-3 bài đã published**

| Tập | Tiêu đề | Status |
|-----|---------|--------|
| 1 | "AI Không Thay Thế Tôi — Nó Làm Tôi 10x Tệ Hơn Hoặc 10x Tốt Hơn" | `parked` |
| 2 | "Tôi Dùng AI Viết 80% Code — Và Đây Là Hậu Quả" | `parked` |
| 3 | "Kilo, Copilot, Claude, Cursor — Honest Review Từ Người Dùng Thực Tế" | `parked` |

---

## 🎨 Series 4: "Thiết Kế Sản Phẩm Một Mình" {#series-4}

> **Parked — Chờ thêm experience. Không viết vội.**

| Tập | Tiêu đề | Status |
|-----|---------|--------|
| 1 | "No Team, No Problem — Cách Tôi Ra Quyết Định Design Một Mình" | `parked` |
| 2 | "Storytelling-driven UI: Tại Sao App Phải Kể Chuyện" | `parked` |
| 3 | "Từ Reject App Store Đến 4.8 Stars" | `parked` |

---

## 📝 Standalone Posts (Không thuộc Series)

- "5 điều tôi ước mình biết trước khi làm Indie"
- "Tại sao tôi chọn SwiftUI thay vì Flutter năm 2025"
- "Làm App một mình: Khi nào nên dừng, khi nào nên tiếp"

---

## 🏆 Priority Order

```
1. Series 1 - Tập 0  ← BẮT ĐẦU NGAY (bài khai màn Series)
2. Series 1 - Tập 1  ← 2 tuần sau
3. Series 2 - Tập 1  ← Có thể viết song song
   ...
4. Series 1 - Tập 2, 3, 4, 5
5. Series 3
6. Series 4
```
