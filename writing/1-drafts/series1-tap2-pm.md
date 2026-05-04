# Co-work Với AI Agent (Tập 3): Làm PM Khi AI Code Cho Bạn

*AI viết đúng những gì bạn nói, nhưng sai hoàn toàn những gì bạn cần. Lỗi không phải của AI.*

> **Series:** Co-work Với AI Agent | **Tập:** 3/5 | **Đọc Tập 2 trước:** [Link Tập 2 - Architect]

---

Ở Tập 2, mình bảo vệ được kiến trúc khỏi bị AI refactor liều lĩnh. Nhưng có một điều mình nhận ra sau đó: Giữ được “xương sống” là tốt. Nhưng nếu requirement mơ hồ, AI sẽ xây đúng cấu trúc, nhưng sai hoàn toàn tính năng.

Vậy phòng bệnh nghe có vẻ đơn giản. Nhưng thực tế thì không.

Hôm đó mình mở Cursor, gõ một câu prompt dài dằng dặc: "Viết cho mình tính năng subscription, gồm 3 tier, có thời hạn, tự renew, notify trước 3 ngày..."

AI gật đầu, và trong vòng 2 phút, mình có một cái màn hình subscription hoàn chỉnh. Weekly plan, Monthly plan, Annual plan. UI đẹp. Logic chạy ổn.

Nhưng sau khi test thật, mình mới nhận ra: **AI viết đúng những gì mình nói, nhưng sai hoàn toàn những gì mình cần.**

Tier "Weekly" mình thêm vào cho có — thực ra user của mình không cần nó. Notify 3 ngày trước là quá sớm, phải là 1 ngày. Và cái "tự renew" thì cần xử lý cả edge case khi payment fail...

AI không biết điều đó. Vì mình chưa nói với nó.

---

### 1. PM tệ nhất là người "Copy-Paste yêu cầu từ Slack vào AI"

Cái bẫy phổ biến nhất mà dev mắc phải khi làm việc với AI là: Lấy nguyên một câu yêu cầu trên Slack, paste thẳng vào prompt, và kỳ vọng AI hiểu được toàn bộ ngữ cảnh.

Nó không hiểu được. Và đó không phải lỗi của AI.

Công việc của một Product Manager — dù là PM thật hay "PM ảo" mà bạn tự đảm nhận khi làm indie — là **biến sự mơ hồ thành sự rõ ràng**, trước khi bất kỳ dòng code nào được viết.

Ngày xưa, sự rõ ràng đó dành cho team dev. Bây giờ, nó dành cho AI của bạn.

---

### 2. Yêu cầu rõ = Code đúng (Công thức thực tế)

Một requirement tốt để feed cho AI cần trả lời được 4 câu hỏi:

**"Who" — Ai dùng tính năng này?**
Không phải "user" chung chung. Phải cụ thể: New user chưa từng mua? Hay user đang dùng free tier muốn upgrade? Hành vi của họ khác nhau hoàn toàn.

**"What" — Họ muốn đạt được điều gì?**
Không phải "xem màn hình subscription". Phải là: "Họ muốn biết cái gì họ nhận được để quyết định có bỏ tiền không."

**"Edge case" — Cái gì có thể fail?**
Payment fail thì sao? User đổi thiết bị giữa chừng? Subscription expire đúng ngày lễ? AI sẽ không chủ động hỏi bạn những điều này — bạn phải đặt câu hỏi trước cho mình.

**"Definition of Done" — Khi nào thì xong?**
"Màn hình chạy được" không phải Done. Done là: User có thể purchase, restore, cancel và nhận notification đúng thời điểm.

---

### 3. Viết "User Story" cho AI, không phải cho con người

Hóa ra cái format User Story mà các PM hay dùng ("As a [user], I want to [action], so that [outcome]") lại cực kỳ hữu dụng khi làm việc với AI.

Không phải vì AI cần đọc User Story. Mà vì **quá trình bạn viết User Story buộc bạn phải suy nghĩ clear trước khi đưa cho AI.**

```
Thay vì: "Làm tính năng in-app purchase"

Hãy viết:
"As a new user who just finished onboarding,
I want to see the 3 subscription options clearly,
So that I can understand the value difference and make a purchase decision.

Acceptance Criteria:
- Show monthly and annual price clearly
- Highlight the "most popular" option  
- Handle payment failure with a human-readable error message
- After successful purchase, immediately unlock premium features"
```

Khi bạn đã viết được đến AC (Acceptance Criteria) — bạn đã có trong tay một specification đủ tốt để AI không "sáng tạo" sai ý.

---

### 4. Backlog nhỏ, Release thường, Học nhanh

Một sai lầm kinh điển nữa: Đưa AI một danh sách 20 tính năng cùng lúc và bảo nó "viết hết đi".

Kết quả? 20 tính năng viết theo kiểu "trung bình cộng". Không tính năng nào được làm thật sự tốt.

Tư duy của PM khi làm việc với AI là: **Nhỏ - Nhanh - Thật.**
- Một tính năng tại một thời điểm.
- Release càng nhanh càng tốt để test với user thật.
- Học từ feedback thật chứ không phải phán đoán.

AI giúp bạn implement nhanh hơn bao giờ hết. Nhưng nếu bạn xây nhầm thứ nhanh hơn — thiệt hại cũng lớn hơn bao giờ hết.

---

### Tóm lại: PM của một AI-powered workflow

Bạn không cần học Product Management bài bản để làm tốt vai trò này. Bạn chỉ cần nhớ 3 điều:

1. **Rõ ràng trước khi code**: AI chỉ giỏi khi bạn đã suy nghĩ xong.
2. **Đặt câu hỏi trước AI**: Edge case, failure cases, Definition of Done.
3. **Nhỏ và nhanh**: Đừng build hết trước khi test gì.

Nhưng mình đã mất một thời gian để nhận ra: Dù spec có rõ đến đâu — nếu user không hiểu cách dùng cái thiết kế AI tạo ra, thì tất cả đều vô nghĩa.

Viết spec đúng giúp AI xây đúng tính năng. Nhưng ai đảm bảo tính năng đó được dùng một cách dễ dàng?

**Đó sẽ là chủ đề của tập tiếp theo.**

> 👉 **[Tập 4 — Làm UX khi AI Vẽ UI: User Không Cần UI Đẹp, Họ Cần UI Dễ Dùng](#)**

Anh em đang define requirement cho AI theo cách nào? Comment chia sẻ nhé — mình đang rất tò mò liệu câu chuyện này có giống của mọi người không. 🙏

---

*Nếu bài viết này có ích, một cái 👏 là cách tốt nhất để giúp nó đến tay nhiều developer hơn. Follow để không bỏ lỡ các tập tiếp theo trong series.*
