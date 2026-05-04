# Co-work Với AI Agent (Tập 3): Làm PM Khi AI Code Cho Bạn

*AI viết đúng những gì bạn nói, nhưng sai hoàn toàn những gì bạn cần. Lỗi không phải của AI.*

> **Series:** Co-work Với AI Agent | **Tập:** 3/5 | **Đọc Tập 2 trước:** [Link Tập 2 - Architect]

---

Ở Tập 2, mình nói về việc giữ "xương sống" kiến trúc — invariant docs, dependency direction, anti-pattern refactor. Nhưng có một điều mình nhận ra sau đó: Giữ được kiến trúc là tốt. Nhưng nếu requirement mơ hồ, AI sẽ xây đúng cấu trúc — mà sai hoàn toàn tính năng.

Mình từng có một task: *"Thêm tính năng notify trước khi position entry."*

AI hiểu đúng từng từ. Nó tạo một notification system hoàn chỉnh — gửi Discord message 30 giây trước khi entry. UI đẹp, logic chạy ổn.

Nhưng cái mình cần không phải là notify Discord. Cái mình cần là: trước khi hệ thống tự động đặt lệnh, có một khoảng pause để mình confirm — hoặc cancel nếu thấy thị trường đang biến động bất thường.

AI không biết điều đó. Vì mình chưa nói với nó. Mình nói "notify" — mình nghĩ trong đầu là "confirm window". Hai khái niệm khác nhau hoàn toàn.

---

### 1. Cái bẫy "lời nói không rõ nghĩa"

Cái bẫy phổ biến nhất khi làm việc với AI là: bạn nói một từ, AI hiểu một nghĩa khác — và cả hai đều tưởng đang đồng ý với nhau.

Khi bạn nói "user-friendly" với một dev thật, họ sẽ hỏi lại: "Ý anh là dễ dùng hay là đẹp?" Khi bạn nói "fast" — họ sẽ hỏi: "Fast ở startup hay fast ở runtime?" Đó là conversation.

AI không hỏi lại. AI assume. Và cái nó assume thường là cái phổ biến nhất trong training data — không phải cái bạn cần trong ngữ cảnh cụ thể của bạn.

**Công việc của một Product Manager — dù là PM thật hay "PM ảo" mà bạn tự đảm nhận khi làm indie — là biến sự mơ hồ thành sự rõ ràng, trước khi bất kỳ dòng code nào được viết.**

Ngày xưa, sự rõ ràng đó dành cho team dev. Bây giờ, nó dành cho AI của bạn. Nhưng AI còn tệ hơn dev ở điểm này: dev sẽ push back khi requirement không clear. AI thì không — nó sẽ code ngay, và code sai rất tự tin.

---

### 2. Bốn câu hỏi phải trả lời trước khi feed prompt

Qua thời gian, mình rút ra một bộ câu hỏi mà mình luôn tự trả lời trước khi nhờ AI implement bất kỳ tính năng nào. Không phải câu hỏi cho AI — câu hỏi cho chính mình.

**"Who" — Ai dùng tính năng này?**

Không phải "user" chung chung. Phải cụ thể: New user chưa từng tương tác với hệ thống? Hay user đang trong position và cần thông tin gấp? Hành vi của họ khác nhau hoàn toàn. New user cần guidance. User đang trong position cần speed.

**"What" — Họ muốn đạt được điều gì?**

Không phải "xem màn hình này". Phải là: họ cần đưa ra quyết định gì? Nếu là decision, cái gì họ cần để quyết định? Thông tin nào thiếu sẽ khiến họ không thể move forward?

**"Edge case" — Cái gì có thể fail?**

Network timeout giữa chừng thì sao? User cancel action khi system đang xử lý? Data source trả về empty result? AI sẽ không chủ động hỏi bạn những điều này — bạn phải đặt câu hỏi trước cho mình.

**"Definition of Done" — Khi nào thì xong?**

"Chạy được" không phải Done. Done là: user có thể hoàn thành workflow từ đầu đến cuối, error path được xử lý bằng human-readable message, và system không leak state khi user abort giữa chừng.

---

### 3. Spec-driven development — viết spec trước, code sau

Trong dự án mình, requirement không được communicate qua lời nói hay chat message. Nó được viết thành file `.yaml` dưới `config/`.

Ví dụ: file `agents.yaml` định nghĩa behavior của từng agent — name, role, description, model profile, routing path. File `trading.yaml` định nghĩa safety limits — max position size, leverage rules, stop-loss requirements. File `models.yaml` định nghĩa ai dùng model nào, profile nào, CLI nào.

Khi mình cần thay đổi behavior của hệ thống, mình không nói với AI "em sửa cái này cho anh." Mình update file config, và AI đọc config đó để biết phải làm gì.

**Lý do mình làm vậy:**

Config file là specification. Nó buộc bạn phải cụ thể: key name là gì, value type là gì, default là gì, validation rule là gì. Không thể viết "user-friendly" trong YAML — bạn phải định nghĩa cụ thể: timeout bao nhiêu giây, max retry bao nhiêu lần, error message là gì.

Quá trình bạn viết config buộc bạn phải suy nghĩ clear. Và một khi config đã rõ — AI không thể "sáng tạo" sai ý được. Nó chỉ read config và execute.

**Áp dụng cho project của bạn:**

Bạn không cần `.yaml` nếu project không cần. Nhưng bạn cần một format specification nào đó — có thể là markdown, có thể là JSON schema, có thể là comment block trên đầu file. Quan trọng là: requirement không nằm trong đầu bạn, không nằm trong chat message — nó nằm trong file, và AI đọc từ đó.

---

### 4. Anti-pattern PM AI hay gặp — và cách chặn

**Anti-pattern 1: "Copy-paste yêu cầu vào prompt"**

Lấy nguyên một câu yêu cầu từ ticket, Slack, hay ghi chú — paste thẳng vào prompt. Kết quả: AI hiểu đúng chữ, sai ngữ cảnh. Cách chặn: trước khi paste, tự hỏi "Nếu một người chưa biết gì đọc câu này, họ có hiểu đúng ý mình không?" Nếu không — viết lại.

**Anti-pattern 2: "Delivery 20 tính năng cùng lúc"**

Đưa AI một danh sách dài và bảo "viết hết đi." Kết quả: 20 tính năng đều ở mức "trung bình cộng" — không tính năng nào được làm thật sự tốt. Cách chặn: một tính năng tại một thời điểm. Release nhanh để test với user thật. Học từ feedback thật.

**Anti-pattern 3: "Done = chạy được"**

AI báo "xong" khi code chạy không error. Nhưng Done thật sự là: happy path hoạt động, error path được xử lý, edge case được cover, và user có thể cancel/undo action. Cách chặn: định nghĩa Acceptance Criteria trước khi AI bắt đầu — và check từng item trước khi accept.

**Anti-pattern 4: "Assume AI hiểu context"**

Bạn nói "thêm caching" — AI thêm cache. Nhưng bạn không nói: cache expire sau bao lâu, invalidate khi nào, fallback khi cache miss. Cách chặn: với mỗi yêu cầu, viết ra 3 scenario — happy path, error path, edge case. Feed cả 3 cho AI.

---

### Tóm lại: Rõ ràng trước khi code

Bạn không cần học Product Management bài bản. Bạn chỉ cần nhớ:

1. **Spec không nằm trong đầu bạn** — viết ra file, AI đọc từ đó. Config > lời nói.
2. **Bốn câu hỏi trước mỗi prompt**: Who, What, Edge case, Definition of Done.
3. **Một tính năng tại một thời điểm** — đừng bulk deliver.
4. **Done ≠ chạy được** — Done = workflow hoàn chỉnh từ đầu đến cuối, error path được xử lý.

Nhưng mình đã mất một thời gian để nhận ra: Dù spec có rõ đến đâu — nếu user không hiểu cách dùng cái thiết kế AI tạo ra, thì tất cả đều vô nghĩa. Viết spec đúng giúp AI xây đúng tính năng. Nhưng ai đảm bảo tính năng đó được dùng một cách dễ dàng?

**Đó sẽ là chủ đề của tập tiếp theo.**

> 👉 **[Tập 4 — Làm UX Khi AI Vẽ UI: User Không Cần UI Đẹp, Họ Cần UI Dễ Dùng](#)**

Anh em đang define requirement cho AI theo cách nào? Comment chia sẻ nhé — mình đang rất tò mò liệu câu chuyện này có giống của mọi người không.

---

*Nếu bài viết này có ích, một cái 👏 là cách tốt nhất để giúp nó đến tay nhiều developer hơn. Follow để không bỏ lỡ các tập tiếp theo trong series.*
