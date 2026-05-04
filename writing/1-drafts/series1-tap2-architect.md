# Co-work Với AI Agent (Tập 2): Giữ Vững Cương Vị Architect Khi AI Muốn "Refactor" Cả Hệ Thống

*AI làm theo bất cứ điều bạn nói — kể cả khi bạn nói sai. Và đó là vấn đề.*

> **Series:** Co-work Với AI Agent | **Tập:** 2/5 | **Đọc Tập 1 trước:** [Link Tập 1 - QA]

---

Ở Tập 1, mình kể chuyện AI review code của chính nó rồi bảo "ổn" — trong khi app crash im lặng. Nhưng sau khi fix xong cái bug đó, mình nhận ra một nguy cơ còn thầm lặng hơn: **AI không chỉ viết bug — nó còn có thể refactor toàn bộ kiến trúc của bạn theo ý nó, và bạn sẽ gật đầu vì nó nghe rất hợp lý.**

Mình từng bảo AI refactor một module network. Nó làm xong trong 10 phút. Code mới ngắn hơn, dùng async/await đúng chuẩn, nhìn qua — hoàn hảo.

Nhưng khi tích hợp vào hệ thống, cả đống thứ khác vỡ theo: interceptor chain không chạy đúng thứ tự, retry logic bị bypass, cache layer ignore hoàn toàn.

AI không phá. AI chỉ **không biết** cái context dài hạn của mình. Nó optimize cho "đúng ngay bây giờ" — không phải "đúng sau 6 tháng bảo trì."

---

### 1. Tại sao AI mù với kiến trúc dài hạn

AI là một lập trình viên cực kỳ giỏi — nhưng nó blind ở 3 thứ mà chỉ bạn mới biết:

**Business context.**
AI không biết hệ thống của bạn sẽ cần scale theo hướng nào trong 3 tháng nữa. Nó không biết team bạn đang chuẩn bị onboard người mới — và kiến trúc bạn đang giữ là để họ có thể onboard nhanh. Nó chỉ thấy code hiện tại, và refactor cho code đó "tốt hơn."

**Maintenance cost.**
AI không phải là người sẽ debug lúc 2h sáng khi module nó refactor vừa crash. Bạn là. Và cái "clean hơn" mà AI tạo ra đôi khi trade-off bằng "khó debug hơn gấp 3 lần."

**The "right now" vs "over time" trap.**
AI optimize cho moment hiện tại — code ngắn hơn, pattern hiện đại hơn, dependency mới hơn. Nhưng kiến trúc tốt không phải là kiến trúc đẹp nhất hôm nay. Đó là kiến trúc mà 6 tháng sau, bạn vẫn hiểu tại sao nó được thiết kế vậy.

**Quyết định kiến trúc không thể delegate 100%. Bạn có thể nhờ AI propose. Nhưng bạn phải là người approve.**

---

### 2. Những gì Architect phải quyết định TRƯỚC khi để AI code

Sau vài lần AI refactor "hoàn hảo" xong thì hệ thống vỡ, mình rút ra một bộ rule mà mình luôn enforce trước khi nhờ AI touch vào kiến trúc.

**Invariant files — file nào AI không được phép động vào.**

Trong hệ thống mình có một file tên là `soul.md`. Đây là file chứa các hard-rule tối thượng — mọi agent phải đọc nó trước khi làm bất cứ điều gì. Nó nằm tách biệt khỏi code, vì nếu AI refactor, nó sẽ merge file này vào chỗ khác "cho gọn" — và system invariant bị mất.

Mỗi project cần ít nhất một file kiểu này: định nghĩa các rule không được vi phạm, các boundary không được phá, các decision không được override. Mình đặt tên nó là `ARCHITECTURE.md` hoặc `INVARIANTS.md` — tên gì không quan trọng. Quan trọng là AI biết: *đây là file đọc, không phải file sửa.*

**Single source of truth cho config.**

AI rất thích hardcode. Bạn bảo nó "set timeout 30 giây" — lần sau nó nhớ 30. Bạn bảo "max leverage 5x" — nó hardcode vào method signature. Rồi một ngày bạn đổi thành 3x, bạn phải tìm khắp codebase để sửa.

Trong hệ thống mình, tất cả config — model assignment, agent topology, trade mode presets, safety limits — nằm trong các file `.yaml` dưới `config/`. Code chỉ read từ đó, không bao giờ hardcode default. Khi AI refactor, mình check ngay: có dòng nào hardcode parameter mà đáng lẽ phải lấy từ config không?

**Dependency direction — module nào được gọi module nào.**

AI hay có xu hướng import bừa: module này gọi module kia, dependency chạy vòng tròn, và sau đó không ai test được gì vì mọi thứ dính vào nhau.

Mình enforce rule đơn giản: **high-level policy không được phụ thuộc vào low-level detail.** Trong hệ thống multi-agent của mình, orchestrator gọi specialist, specialist không gọi ngược lại orchestrator. Gate agent là chốt chặn cuối — không ai bypass gate. Rule này nghe hiển nhiên, nhưng AI sẽ vi phạm nó nếu bạn không nói trước.

---

### 3. Anti-pattern AI hay làm — và cách chặn

Qua thời gian làm việc với AI, mình thấy nó lặp lại vài anti-pattern kiến trúc này khá đều đặn:

**Anti-pattern 1: "Gộp cho gọn"**
AI nhìn thấy 3 file riêng biệt với 3 responsibility khác nhau, và suggest: *"Em gộp thành 1 file cho dễ quản lý nhé."* Về mặt code — đúng là gọn hơn. Về mặt kiến trúc — bạn vừa mất separation of concerns. Khi nào AI suggest gộp: chỉ đồng ý nếu các file đó thực sự cùng một concern. Còn không — giữ nguyên.

**Anti-pattern 2: "Hardcode default cho nhanh"**
AI viết: `function buildConfig(timeout = 30, maxRetry = 3)`. Lần sau bạn đổi timeout thành 60 — bạn phải sửa ở 3 chỗ khác nhau. Cách chặn: luôn pass config object từ caller, không dùng default value cho parameter mang tính business.

**Anti-pattern 3: "Bypass abstraction layer"**
AI cần data từ tầng thấp nhất, nên nó import thẳng từ tầng cao nhất xuống, bỏ qua lớp trung gian. Kết quả: dependency injection vỡ, không mock test được, và khi tầng thấp thay đổi — 5 file phải sửa cùng lúc. Cách chặn: enforce dependency direction ngay từ đầu, và reject bất kỳ import nào đi ngược chiều.

**Anti-pattern 4: "Refactor mà không biết tại sao"**
AI nhìn thấy code dùng callback → suggest đổi sang Promise. Nhìn thấy Promise → suggest đổi sang async/await. Mỗi lần refactor đều "đúng" về mặt kỹ thuật. Nhưng nó không biết *tại sao* bạn dùng callback ở chỗ đó — có thể là để maintain backward compatibility với một legacy module. Cách chặn: trước mỗi lần AI refactor, hỏi nó: *"Cái gì đang broken mà cần refactor?"* Nếu câu trả lời là "không có gì broken, chỉ cho nó modern hơn" — thì đừng refactor.

---

### Tóm lại: Giữ xương sống, delegate phần còn lại

Bạn không cần phải viết mọi dòng code. Nhưng bạn cần biết **dòng nào không được phép sai kiến trúc.**

1. **Có ít nhất một invariant file** — `soul.md`, `ARCHITECTURE.md`, gì cũng được. AI đọc, không sửa.
2. **Config không bao giờ hardcode** — yaml/json là single source of truth, code chỉ read.
3. **Enforce dependency direction** — high-level không phụ thuộc low-level. Không ai bypass layer.
4. **Không refactor nếu không có gì broken** — "cho nó modern hơn" không phải lý do.

Nhưng mình đã mất một thời gian để nhận ra: Giữ được "xương sống" là tốt. Nhưng nếu requirement mơ hồ, AI sẽ xây đúng cấu trúc — nhưng sai hoàn toàn tính năng. Và đó là chuyện của tập tiếp theo.

**Đó sẽ là chủ đề của tập tiếp theo.**

> 👉 **[Tập 3 — Làm PM Khi AI Code Cho Bạn: AI Viết Đúng Những Gì Bạn Nói, Nhưng Sai Những Gì Bạn Cần](#)**

Anh em có câu chuyện nào AI "refactor" xong thì hệ thống vỡ không? Share dưới comment — mình đoán không chỉ mình đâu.

---

*Nếu bài viết này có ích, một cái 👏 là cách tốt nhất để giúp nó đến tay nhiều developer hơn. Follow để không bỏ lỡ các tập tiếp theo trong series.*
