# Co-work Với AI Agent (Tập 4): Làm UX Khi AI Vẽ UI — User Không Cần UI Đẹp, Họ Cần UI Dễ Dùng

*AI vẽ được UI đẹp. Nhưng không cảm nhận được tại sao user bỏ flow ở bước thứ ba.*

> **Series:** Co-work Với AI Agent | **Tập:** 4/5 | **Đọc Tập 3 trước:** [Link Tập 3 - PM]

---

Ở Tập 3, mình nói về việc viết spec rõ để AI xây đúng tính năng. Nhưng có một điều spec không nói được: liệu tính năng đó có dễ dùng không.

AI có thể sinh ra một interface hoàn chỉnh trong vòng 30 giây — dashboard, form, navigation, tất cả layout cân đối, spacing chuẩn, color scheme hài hòa. Nhìn qua, rất "professional."

Nhưng chỉ đẹp ở bề ngoài.

Thực tế là: AI được train trên hàng triệu UI đẹp. Nó biết UI đẹp trông như thế nào. Nhưng nó không biết:

- User của bạn đang trong tâm trạng gì khi mở hệ thống — vội vàng, lo lắng, hay đang multitask.
- Thông tin nào user cần thấy trong 3 giây đầu tiên.
- Cái flow nào khiến họ phải dừng lại suy nghĩ — và đó chính là moment họ bỏ đi.

**UX không phải là làm cho UI trông đẹp. UX là làm cho việc sử dụng UI trở nên rõ ràng đến mức user không cần phải suy nghĩ.**

---

### 1. "AI Slop Design" — đẹp nhưng vô dụng

Có một từ trong cộng đồng design gọi là "AI Slop" — chỉ những sản phẩm trông rất bóng bẩy, rất "professional", nhưng thiếu cái gì đó. Nó thiếu cảm nhận về người dùng thật.

Vấn đề không phải AI dở về design. Vấn đề là AI optimize cho "đẹp theo tiêu chuẩn trung bình" — không phải "dễ dùng cho user của bạn."

Khi bạn bảo AI "vẽ cho mình một dashboard," nó sẽ sinh ra một cái dashboard với: chart đẹp, card layout gọn, navigation sidebar đầy đủ. Tất cả đều đúng. Nhưng nó không hỏi:

- Dashboard này dùng để **quyết định** hay để **theo dõi**? Hai cái đó cần layout khác nhau hoàn toàn.
- Metric nào là quan trọng nhất? Nếu mọi thứ đều được highlight — không có gì là quan trọng.
- User sẽ làm gì sau khi nhìn dashboard? Click vào đâu? Nếu không có next action rõ ràng — dashboard chỉ là bức tranh đẹp.

**Bẫy lớn nhất: bạn thấy AI sinh ra UI đẹp, bạn approve, bạn ship — và user không biết dùng.** Không phải vì user dở. Vì UI đó được thiết kế cho một "average user" không tồn tại.

---

### 2. Phân biệt UI (AI làm được) và UX (bạn phải làm)

| Khía cạnh | AI làm tốt | Bạn phải quyết định |
| --- | --- | --- |
| **Layout** | Responsive grid, spacing system | Thông tin nào user thấy đầu tiên? |
| **Visual** | Color, typography, icon | Cảm giác tổng thể có match context không? |
| **Flow** | Generate màn hình tiếp theo | Có cần màn hình đó không? |
| **Copy** | Tạo text cho button/label | Tone có match expectation của user không? |
| **Animation** | Implement transition | Animation này thêm giá trị hay làm rối? |

Cột bên phải — đó là UX. Và mỗi câu hỏi đó đều cần bạn hiểu user thật, không phải "average user" trong training data của AI.

---

### 3. User Journey First — trước khi nhờ AI vẽ

Thay vì nói với AI "vẽ cho mình màn hình X," hãy làm thêm một bước:

**Bước 1:** Viết text User Journey:

User mở hệ thống → Thấy trạng thái hiện tại → Muốn review detail → Chọn action → Confirm → Nhận kết quả

**Bước 2:** Identify "moment of doubt" — lúc user có thể bỏ đi:

→ Moment 1: Mở hệ thống, không thấy trạng thái tổng quan → *"App này có hoạt động không?"*
→ Moment 2: Nhìn vào detail, không hiểu metric nào quan trọng → *"Mình cần làm gì tiếp?"*
→ Moment 3: Đến bước confirm, không chắc action này reversible → *"Có cancel được không?"*

**Bước 3:** Chỉ sau đó mới feed cho AI: "Vẽ interface cho flow này, phải giải quyết 3 moment of doubt: trạng thái tổng quan visible ngay, metric quan nhất được highlight, confirmation rõ ràng với option cancel."

Bây giờ AI vẽ UI. Nhưng UX là của bạn.

---

### 4. Anti-pattern UX AI hay làm — và cách chặn

**Anti-pattern 1: "Everything is important"**
AI generate một dashboard với 15 metric, tất cả đều được highlight, chart đẹp, color rực rỡ. Kết quả: user không biết nhìn vào đâu. Cách chặn: định nghĩa trước — metric nào là "north star" (1-2 cái), metric nào là "supporting" (3-5 cái), cái còn lại hide trong detail view.

**Anti-pattern 2: "Flow quá dài"**
AI design một onboarding 5 bước, một checkout 4 màn hình, một settings page với 20 option. Mỗi bước đều có lý do hợp lý — nhưng user không đọc. Họ scroll, họ skip, họ bỏ. Cách chặn: trước khi nhờ AI design, hỏi "Cái gì là minimum để user hoàn thành task?" Sau đó cut bất cứ thứ gì không phục vụ task đó.

**Anti-pattern 3: "Error state không có"**
AI sinh ra happy path hoàn hảo — nhưng không có empty state, không có loading state, không có error state. Khi data chưa có, user thấy màn hình trắng. Khi network lỗi, user thấy crash. Cách chặn: với mỗi screen, yêu cầu AI generate cả 4 state: default/empty, loading, success, error.

**Anti-pattern 4: "Platform guideline bị ignore"**
Mỗi platform có convention riêng — iOS Human Interface Guidelines, Material Design, Web Accessibility standards. AI biết tất cả — nhưng không tự động follow đúng. Nó sinh ra UI "chung chung" — không sai platform nào, nhưng cũng không đúng platform nào. Cách chặn: sau khi AI vẽ xong, check qua platform guideline checklist. Những thứ cơ bản như: interactive element có hit target đủ lớn không, text có readable ở size lớn không, contrast ratio có đạt chuẩn không.

---

### Tóm lại: AI vẽ, bạn cảm nhận

Bạn chỉ cần nhớ:

1. **User Journey trước, UI sau** — viết flow ra, identify moment of doubt, rồi mới nhờ AI vẽ.
2. **UI ≠ UX** — AI làm đẹp, bạn làm dễ dùng.
3. **4 state cho mỗi screen** — default, loading, success, error. Đừng chỉ có happy path.
4. **Cut, đừng add** — hỏi "cái gì là minimum để user hoàn thành task?" — rồi cut hết phần thừa.

Nhìn lại 4 tập vừa rồi, mình nhận ra một điều: QA, Architect, PM, UX — tất cả những vai trò đó đều có một điểm chung. Chúng đều đòi hỏi **bạn phải biết mình muốn gì** trước khi nhờ AI làm.

Và đó cũng chính là câu hỏi mà tập cuối của series sẽ đưa ra.

**Đó sẽ là chủ đề của tập tiếp theo.**

> 👉 **[Tập 5 (Cuối) — Bạn Đã Là AI-First Developer Rồi — Chỉ Là Chưa Nhận Ra Thôi](#)**

Anh em có UI nào "đẹp nhưng user không dùng" muốn chia sẻ không? Mình đoán hầu hết chúng ta đều có ít nhất một câu chuyện kiểu đó.

---

*Nếu bài viết này có ích, một cái 👏 là cách tốt nhất để giúp nó đến tay nhiều developer hơn. Follow để không bỏ lỡ các tập tiếp theo trong series.*
