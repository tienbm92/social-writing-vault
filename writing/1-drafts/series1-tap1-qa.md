# Co-work Với AI Agent (Tập 1): Làm QA Khi Bạn Không Thể Tin Hoàn Toàn Vào AI

*AI review code của chính nó và bảo "Code ổn". Rồi app crash. Đây là cách mình debug tư duy đó.*

> **Series:** Co-work Với AI Agent | **Tập:** 1/5 | **Đọc Tập 0 trước:** [Link Tập 0]

![AI Confidence vs Human Skepticism](/Users/tienbm92/.gemini/antigravity/brain/929e7c5c-2b93-49b6-a659-dd02448d0c24/tap1_qa_skepticism_1776334509091.png)

---

Ở Tập 0, mình kể cạnh giao AI viết module, build xanh, nhưng test thực tế thì sai. Sau đó, mình làm một điều mà nhiều người vẫn hay làm: nhờ AI tự review lại code của chính nó.

Kết quả? Nó bảo: *"Code ổn, không thấy vấn đề gì đặc biệt."*

Có một sự thật khá khó nghe: **AI không biết nó sai.**

Không phải vài lần. Không phải thỉnh thoảng. Mà rất thường xuyên — đặc biệt là ở những chỗ quan trọng nhất: edge case, concurrency, memory management.

Mình từng có một bug đơn giản: Màn hình bị deallocate trước khi async task complete, dẫn đến crash im lặng. Mình nhờ AI review code. Nó đọc xong, bảo “Code ổn, không thấy vấn đề gì đặc biệt.”

Mình test thêm một lần nữa. App crash.

AI confident. Nhưng AI sai. Và đó là lý do tại sao QA không thể để AI tự review output của chính nó.

---

### 1. "Confirmation Bias" của AI

AI được train để tạo ra câu trả lời có vẻ tự tin và hợp lý. Khi bạn hỏi "Code này có ổn không?", xu hướng mặc định của nó là tìm lý do để nói "Ổn". Không phải vì nó muốn lừa bạn — mà vì đó là pattern được re-enforce trong training.

Nếu bạn hỏi theo kiểu khác — "Tìm cho mình bất kỳ vấn đề tiềm ẩn nào, dù nhỏ" — bạn sẽ nhận được một câu trả lời khác hoàn toàn.

**Kỹ năng QA đầu tiên: Đặt câu hỏi như một người hoài nghi, không phải người muốn được reassure.**

---

### 2. Ba loại bug AI thường bỏ sót

Qua kinh nghiệm thực tế, mình thấy AI thường miss 3 nhóm bug này:

**Nhóm 1 — Timing & Concurrency:**
Race condition, async/await được xử lý không đúng thứ tự, UI update từ background thread. AI biết lý thuyết nhưng thường không "cảm" được vấn đề khi nhìn vào code tĩnh.

**Nhóm 2 — Memory & Lifecycle:**
Retain cycle trong closure, view controller không được deallocate, observable chưa được cancel. Đây là những vấn đề chỉ xuất hiện khi bạn chạy app qua nhiều màn hình.

**Nhóm 3 — Business Logic Edge Case:**
Những gì xảy ra khi user subscription vừa hết đúng lúc đang request? Khi network bị mất giữa chừng? Khi app bị force-quit giữa một transaction? AI không tự nghĩ ra những scenario này — bạn phải chủ động đặt ra.

---

### 3. Cách viết test case hiệu quả khi làm việc với AI

Thay vì nhờ AI viết test cho code của chính nó (không bao giờ là ý hay), hãy dùng AI như một **Test Case Generator** dựa trên specification, không phải implementation.

```
Prompt tốt:
"Đây là spec của tính năng in-app purchase. 
Liệt kê cho mình tất cả các test case có thể xảy ra, 
bao gồm happy path, error path và edge case.
Đừng viết code test — chỉ cần list scenario thôi."
```

Khi AI generate scenario từ spec (không phải từ code), nó không bị anchored vào implementation hiện tại. Bạn sẽ nhận được các scenario mà chính bạn có thể không nghĩ tới.

Sau đó, bạn tự viết test hoặc nhờ AI viết — nhưng bây giờ bạn đang control cái gì được test.

---

### 4. Review checklist của một QA khi nhận code từ AI

Trước khi merge bất kỳ đoạn code nào AI viết, mình có một checklist nhanh:

```
[ ] Chạy thử trên device thật (không chỉ simulator)?
[ ] Test network = offline?
[ ] Test khi app bị interrupt (call đến, push notification)?
[ ] Check Instruments: memory không tăng liên tục?
[ ] Có màn hình nào không load đúng lần thứ 2 trở đi không?
[ ] Edge case: empty state, loading state, error state?
```

Nghe đơn giản. Nhưng phần lớn bug production của mình đến từ việc skip ít nhất một item trong list này.

---

### Tóm lại: Hoài nghi không phải thiếu tin tưởng

Một QA giỏi là người không trust vào bất kỳ output nào cho đến khi có bằng chứng cụ thể rằng nó chạy đúng. Điều đó áp dụng cả với code của chính bạn, lẫn code của AI.

AI là một developer không bao giờ mệt và không bao giờ complain — nhưng nó cũng không bao giờ test lại công việc của mình. Đó là việc của bạn.

Nhưng sau nhiều lần debug, mình nhận ra một điều khó chịu hơn: bắt bug sau khi nó xảy ra là "chữa bệnh". Nhưng còn một nguy cơ lắng thầm hơn mà mình chưa đề cập: **AI không chỉ viết bug — nó còn có thể đề xuất refactor toàn bộ kiến trúc của bạn theo ý nó, và bạn sẽ gật đầu vì nó nghe rất hợp lý.**

Và lúức đó, không có checklist nào cứu được bạn nếu bạn không phải là người giữ "xương sống" của hệ thống.

**Đó sẽ là chủ đề của tập tiếp theo.**

> 👉 **[Tập 2 — Giữ Vững Cương Vị Architect khi AI Muốn “Refactor” Cả Hệ Thống](#)**

Anh em có câu chuyện bug “vui” nào khi tin tưởng AI review code không? Inbox hoặc comment mình với — đảm bảo sẽ có material cho bài tiếp theo. 😂

---

*Nếu bài viết này có ích, một cái 👏 là cách tốt nhất để giúp nó đến tay nhiều developer hơn. Follow để không bỏ lỡ các tập tiếp theo trong series.*
