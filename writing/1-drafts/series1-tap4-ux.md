# Co-work Với AI Agent (Tập 4): Làm UX khi AI Vẽ UI — Ai Mới Thực Sự Hiểu User?

*AI vẽ được UI đẹp. Nhưng không cảm nhận được tại sao user bỏ app ở bước thứ 3.*

> **Series:** Co-work Với AI Agent | **Tập:** 4/5 | **Đọc Tập 3 trước:** [Link Tập 3 - PM]

---

Ở Tập 3, mình học cách viết spec rõ để AI xây đúng tính năng. Nhưng có một điều spec không nói được: liệu tính năng đó có dễ dùng không.

Đó chính xác là điểm khởi đầu của tập này.

AI có thể sinh ra một màn hình SwiftUI đẹp trong vòng 30 giây.

Layout cân đối, color scheme hài hòa, spacing theo đúng chuẩn Marketing. Trông rất “app store”.

Nhưng mình nhớ lần đầu tiên để AI design màn hình onboarding cho app: Nó ra một flow 5 bước, mỗi bước một màn hình animation đẹp, text giải thích đầy đủ, button “Next” to và rõ ràng.

Mình test nó với 3 người bạn (không phải user thật — nhưng đủ để nhận ra vấn đề). Cả 3 người đều bỏ app ở bước thứ 3.

**Onboarding đẹp 5 bước đó quá dài.** User hiện đại không đọc onboarding — họ skip. Cái AI vẽ tốt về mặt kỹ thuật nhưng tệ về mặt psychology của người dùng.

---

### 1. "AI Slop Design" — Đẹp nhưng không ai dùng

Có một từ trong cộng đồng design gọi là "AI Slop" — ý chỉ những sản phẩm trông rất bóng bẩy, rất "professional", nhưng thiếu đi cái gì đó. Nó thiếu soul.

Vấn đề là AI được train trên hàng triệu UI đẹp. Nó biết UI đẹp trông như thế nào. Nhưng nó không biết:
- User của **bạn** đang trong tâm trạng gì khi mở app.
- Ngón tay của họ trên màn hình 6 inch chạm vào đâu tự nhiên nhất.
- Cái micro-animation nào khiến họ thấy "ờ con app này nuột" chứ không phải "ừ thôi cũng được".

UX không phải là làm cho UI trông đẹp. UX là làm cho việc sử dụng UI trở nên dễ chịu và rõ ràng đến mức user không cần phải suy nghĩ.

---

### 2. Phân biệt UI (AI làm được) và UX (bạn phải làm)

| | AI làm tốt | Bạn phải quyết định |
|---|---|---|
| **Layout** | Responsive grid, spacing system | Cái gì visible fold first? |
| **Visual** | Color, typography, icon | Brand feeling có đúng không? |
| **Flow** | Generate màn hình tiếp theo | Có cần màn hình đó không? |
| **Copy** | Tạo text cho button/label | Tone có match culture app không? |
| **Animation** | Implement transition | Animation này thêm hay bớt giá trị? |

Cột bên phải — đó là UX. Và mỗi câu hỏi đó đều cần bạn hiểu user.

---

### 3. Kỹ thuật: "User Journey First" trước khi nhờ AI vẽ

Thay vì nói với AI "Vẽ cho mình màn hình checkout", hãy làm thêm một bước:

**Bước 1:** Vẽ tay (hoặc viết text) User Journey:
```
User mở giỏ hàng → Thấy tổng tiền → Muốn review item → 
Chọn phương thức payment → Confirm → Nhận confirmation
```

**Bước 2:** Identify "moment of doubt" — lúc user có thể bỏ đi:
```
→ Moment 1: Thấy tổng tiền cao hơn expect (add coupon input)
→ Moment 2: Không chắc payment có secure không (add security badge)
→ Moment 3: Không biết shipping về khi nào (add estimated date)
```

**Bước 3:** Chỉ sau đó mới feed cho AI: "Vẽ màn hình checkout, phải giải quyết 3 moment of doubt này: coupon input visible, security indication, estimated delivery date."

Bây giờ AI vẽ UI. Nhưng UX là của bạn.

---

### 4. Apple HIG — Người bạn AI hay quên

Apple Human Interface Guidelines không phải optional. Với app iOS, có những pattern Apple đã nghiên cứu hàng triệu user để tìm ra — và AI không phải lúc nào cũng follow đúng.

**Những thứ AI hay sai:**

- **Safe area**: Đôi khi quên padding bottom cho notched devices.
- **Thumb zone**: Đặt button quan trọng quá cao trên màn hình.
- **Haptic feedback**: Không chủ động thêm haptics khi confirm action quan trọng.
- **Accessibility**: Text contrast ratio, dynamic type support thường bị bỏ qua.

Sau khi AI vẽ xong, mình có một bộ câu hỏi nhanh để check:

```
[ ] Tất cả interactive element có hit target ≥ 44pt không?
[ ] Content có bị che khi keyboard hiện lên không?
[ ] Empty state có không? Error state có không?
[ ] App chạy ổn ở chế độ Dark mode không?
[ ] Text vẫn readable ở accessibility text size lớn nhất không?
```

---

### Tóm lại: AI vẽ, bạn cảm nhận

Cái khả năng “cảm nhận” UX — nhận ra khi nào một flow cảm thấy cồng kềnh, khi nào một animation thêm giá trị chứ không phải làm rối — đó là thứ bạn phát triển bằng cách dùng nhiều app tốt, quan sát user thật dùng app của mình, và liên tục đặt câu hỏi “Cái này thực sự dễ dùng chưa?”

AI không có khả năng đó. Đó là của bạn.

Nhìn lại 4 tập vừa rồi, mình nhận ra một điều: QA, PM, Architect, UX — tất cả những vai trò đó đều có một điểm chung. Chúng đều đòi hỏi **bạn phải biết mình muốn gì** trước khi nhờ AI làm.

Và đó cũng chính là câu hỏi mà tập cuối của series sẽ đưa ra: Bạn đã sẵn sàng chưa?

> 👉 **[Tập 5 (Cuối) — Bạn Đã Là AI-First Developer Rồi — Chỉ Là Chưa Nhận Ra Thôi](#)**

Anh em có UI nào “đẹp nhưng user không dùng” muốn chia sẻ không? 😄 Mình đoán hầu hết chúng ta đều có ít nhất một câu chuyện kiểu đó.

---

*Nếu bài viết này có ích, một cái 👏 là cách tốt nhất để giúp nó đến tay nhiều developer hơn. Follow để không bỏ lỡ các tập tiếp theo trong series.*
