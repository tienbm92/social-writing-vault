# Co-work Với AI Agent (Tập 5): Bạn Đã Là AI-First Developer Rồi — Chỉ Là Chưa Nhận Ra Thôi

*Tất cả những lần AI làm sai đều dẫn về một bài học duy nhất: biết mình muốn gì trước khi nhờ AI.*

> **Series:** Co-work Với AI Agent | **Tập cuối:** 5/5 | **Đọc Tập 4 trước:** [Link Tập 4]

---

Mình ngồi nhìn lại lịch sử chat với AI trong 6 tháng vừa rồi.

Có cái module bị sai mà mình kể ở Tập 0. Có cái bug crash im lặng mà AI review xong bảo “Code ổn” ở Tập 1. Có cái refactor bắt ngờ mà mình để AI làm sau đó mất 2 tiếng dọn ở Tập 2. Có cái subscription tier “Weekly” mình thêm vào cho có và AI cứ thế mà viết ở Tập 3. Và cái onboarding 5 bước đẹp nhưng user bỏ ngay bước thứ 3 ở Tập 4.

Tất cả những điều đó xảy ra không phải vì AI dở. Chúng xảy ra vì mình chưa rõ ý của mình trước khi nhờ AI.

Và đó là bài học duy nhất của toàn bộ series này.

Nếu anh em đã đọc cả series từ đầu, khả năng cao là vì anh em đang có chung một nỗi lo:

*“Mình đang làm việc với AI hàng ngày. Nhưng mình chưa chắc mình đang làm đúng cách.”*

Mình hiểu cảm giác đó. Hai năm trước mình cũng ở trong cái trạng thái “vừa excited vừa lo” đó.

Hôm nay — tập cuối của series — mình muốn đặt ra một câu hỏi khác.

---

### 1. Câu hỏi sai: “AI đang thay thế dev không?”

Đây là câu hỏi mình thấy khắp nơi. Và mình nghĩ đây là câu hỏi sai.

Không phải vì câu trả lời là “không” — mà vì câu hỏi này khiến bạn ở thế bị động. Bạn đang chờ xem liệu mình có bị thay thế không, thay vì chủ động định nghĩa mình muốn là ai trong cái workflow mới này.

Câu hỏi đúng hơn: **“Mình muốn đóng vai trò gì trong một team mà AI là member?”**

---

### 2. Nhìn lại: Bạn đã làm được gì trong series này

Qua 5 tập, chúng ta đã đi qua các vai trò:

**Tập 0:** Nhận ra rằng AI là coder, bạn là người ra quyết định. Đừng để vào bẫy “Vibe Coding” chỉ vì code build xanh.

**Tập 1 — QA:** Hoài nghi có hệ thống. AI không biết nó sai, và không bao giờ tự test lại output của mình. Đó là việc của bạn.

**Tập 2 — Architect:** Giữ “xương sống” của hệ thống. Không để AI refactor theo ý nó mà không có lý do. Document design decision để AI không “quên”.

**Tập 3 — PM:** Biến sự mơ hồ thành specification rõ ràng trước khi AI bắt đầu. “AI viết đúng những gì mình nói, nhưng sai hoàn toàn những gì mình cần” — đó là lỗi của mình, không phải của AI.

**Tập 4 — UX:** AI vẽ UI, bạn quyết định UX. “Đẹp” và “dùng được” là hai thứ khác nhau.

Tất cả những kỹ năng này — bạn đang làm chúng mỗi ngày rồi. Điều thay đổi chỉ là nhận thức: bạn đang làm chúng **một cách có chủ ý** hơn.

---

### 3. Kỹ năng quan trọng nhất của AI-First Developer

Nếu phải chọn một kỹ năng duy nhất — một thứ mà bạn có thể bắt đầu rèn giũa ngay hôm nay — mình sẽ chọn:

**Khả năng đặt câu hỏi tốt.**

Không phải "Viết cho mình function A".

Mà là: "Mình đang cố giải quyết vấn đề B. User journey là C. Constraint là D. Có ít nhất 3 cách implement A — trade-off của mỗi cách là gì?"

Cách bạn frame câu hỏi cho AI quyết định 80% chất lượng output. Và kỹ năng frame câu hỏi tốt — đó là kỹ năng mà bạn xây dựng bằng kinh nghiệm đời thực, không phải từ training data.

---

### 4. Mô hình tư duy cuối cùng: "Decision Stack"

Đây là framework mình dùng mỗi khi làm việc với AI:

```
┌─────────────────────────────────────┐
│  LV5 - VISION (Bạn giữ)            │
│  Sản phẩm đang đi về đâu?          │
├─────────────────────────────────────┤
│  LV4 - STRATEGY (Bạn giữ)          │  
│  Cái gì build, cái gì skip?        │
├─────────────────────────────────────┤
│  LV3 - DESIGN (Bạn + AI)           │
│  Architecture, UX, logic flow      │
├─────────────────────────────────────┤
│  LV2 - IMPLEMENTATION (AI nhiều)   │
│  Viết code, boilerplate, unit test  │
├─────────────────────────────────────┤
│  LV1 - SYNTAX (AI gần như toàn bộ) │
│  Syntax, format, docs              │
└─────────────────────────────────────┘
```

AI giỏi nhất ở LV1-LV2. Bạn không thể delegate LV4-LV5. LV3 là nơi bạn và AI collaborare thực sự.

Khi bạn biết mình đang làm việc ở level nào — bạn sẽ biết cần giữ lại bao nhiêu quyền kiểm soát.

---

### 5. Điều mình muốn nói sau cùng

Cuộc cách mạng AI không đang xảy ra ở đâu đó trong tương lai. Nó đang xảy ra ngay bây giờ, trong từng lần bạn mở Cursor, gõ một câu prompt, và nhận lại code.

Developer nào thắng trong kỷ nguyên này không phải là người dùng AI nhiều nhất. Cũng không phải người prompt hay nhất.

Đó là người **biết mình muốn gì** và đủ rõ ràng để truyền đạt điều đó cho AI.

Cái đó không phải là kỹ năng AI. Đó là kỹ năng con người.

---

### Cảm ơn anh em đã đồng hành!

Đây là lần đầu tiên mình thử viết một series dài về chủ đề này. Nếu nó có ích với anh em — dù chỉ một tập — mình sẽ rất vui nếu anh em share cho người khác cùng đọc.

Và nếu có chủ đề nào anh em muốn mình đào sâu hơn — inbox mình hoặc comment dưới đây nhé. Mình đang lên kế hoạch cho Series 2 rồi đây. 🚀

---

**📚 Toàn bộ Series "Co-work Với AI Agent":**
- [Tập 0: Khi AI Là Coder Của Bạn](#)
- [Tập 1: Làm QA — Không Trust Hoàn Toàn Vào AI](#)
- [Tập 2: Giữ Vừng Cương Vị Architect Khi AI Muốn Refactor](#)
- [Tập 3: Làm PM khi AI Code cho Bạn](#)
- [Tập 4: Làm UX khi AI Vẽ UI](#)
- Tập 5: Bạn Đã Là AI-First Developer Rồi ← *Bạn đang ở đây*

---

*Series hoàn thành. Nếu anh em thấy có ích — một cái 👏 và share cho đồng nghiệp là điều tuyệt vời nhất có thể làm. Hẹn gặp lại ở Series 2. 🚀*
