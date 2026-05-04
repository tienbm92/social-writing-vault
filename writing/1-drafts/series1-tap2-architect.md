# Co-work Với AI Agent (Tập 2): Giữ Vững Cương Vị Architect Khi AI Muốn "Refactor" Cả Hệ Thống

*AI làm theo bất cứ điều bạn nói — kể cả khi bạn nói sai. Và đó là vấn đề.*

> **Series:** Co-work Với AI Agent | **Tập:** 2/5 | **Đọc Tập 1 trước:** [Link Tập 1 - QA]

---

Ở Tập 1, mình kể chuyện AI review code của chính nó rồi bảo "ổn" — trong khi app crash im lặng. Nhưng sau khi fix xong cái bug đó, mình nhận ra một nguy cơ còn thầm lặng hơn: **AI không chỉ viết bug — nó còn có thể refactor toàn bộ kiến trúc của bạn theo ý nó, và bạn sẽ gật đầu vì nó nghe rất hợp lý.**

Hôm đó, mình bảo AI: *"Em refactor giúp anh module network layer, đổi từ URLSession sang async/await cho nó hiện đại."*

AI gật đầu. Trong vòng 10 phút, nó refactor sạch sẽ. Code mới ngắn hơn, gọn hơn, dùng `async/await` đúng chuẩn iOS 15+. Nhìn qua — hoàn hảo.

Nhưng khi mình merge vào nhánh chính, cả đống thứ khác vỡ theo: interceptor chain không chạy đúng thứ tự, retry logic bị bypass, và cái cache layer mình từng mất 2 ngày để tune — giờ ignore hoàn toàn.

AI không phá. AI chỉ **không biết** cái context dài hạn của mình. Nó optimize cho "đúng ngay bây giờ" — không phải "đúng sau 6 tháng bảo trì."

---

### 1. Tại sao AI không thể tự quyết kiến trúc?

AI là một lập trình viên cực kỳ giỏi — nhưng nó bị mù trong 3 thứ mà chỉ bạn mới biết:

**Business context dài hạn.**
AI không biết app của bạn sẽ mở rộng sang subscription model trong 3 tháng nữa. Nó không biết team bạn đang chuẩn bị onboard 3 dev mới — và kiến trúc bạn đang giữ là để họ có thể onboard nhanh. Nó chỉ thấy code hiện tại, và refactor cho code đó "tốt hơn."

**Maintenance cost.**
AI không phải là người sẽ thức lúc 2h sáng để fix production bug khi module nó refactor vừa crash. Bạn là. Và cái "clean hơn" mà AI tạo ra đôi khi trade-off bằng "khó debug hơn gấp 3 lần."

**The "right now" vs "over time" trap.**
AI optimize cho moment hiện tại — code ngắn hơn, pattern hiện đại hơn, dependency mới hơn. Nhưng kiến trúc tốt không phải là kiến trúc đẹp nhất hôm nay. Đó là kiến trúc mà 6 tháng sau, bạn vẫn hiểu tại sao nó được thiết kế vậy.

**Quyết định kiến trúc không thể delegate 100%. Bạn có thể nhờ AI propose. Nhưng bạn phải là người approve.**

---

### 2. Những gì Architect phải quyết định TRƯỚC khi để AI code

Sau lần refactor "hoàn hảo" đó, mình rút ra một bộ câu hỏi mà mình luôn trả lời trước khi nhờ AI touch vào kiến trúc:

**"Cấu trúc nào đang giữ xương sống hệ thống?"**
Mỗi app có một số ít "linh hồn" — những pattern, những boundary, những rule mà nếu phá vỡ, cả hệ thống sụp. Với mình, đó là: Domain layer phải độc lập, Repository là cầu nối duy nhất giữa data và use case, UI không được gọi trực tiếp API. Mình viết mấy rule này ra file `ARCHITECTURE.md` trong project — và feed nó cho AI trước mỗi lần nhờ refactor.

**"Dependency ownership — ai sở hữu cái gì?"**
AI hay có xu hướng import bừa: module này gọi module kia, dependency chạy vòng tròn, và sau đó không ai test được gì vì mọi thứ dính vào nhau. Mình quyết định trước: module nào được import module nào, và enforce điều đó qua code review — kể cả code AI viết.

**"Khi nào dùng pattern nào?"**
MVVM cho màn hình có state phức tạp. Simple View cho màn hình static. Repository pattern cho data layer. UseCase cho business logic. AI biết tất cả pattern này — nhưng nó không biết **khi nào** nên dùng cái nào trong **ngữ cảnh cụ thể của bạn**. Đó là decision của Architect.

---

### 3. Case study: Một quyết định kiến trúc sai và cái giá phải trả

Mình từng có một quyết định mà giờ nhìn lại vẫn thấy đau.

Hôm đó, mình cần gấp tính năng hiển thị portfolio crypto. AI suggest: *"Anh ơi, để em bypass Domain layer luôn, gọi API thẳng từ ViewModel cho nhanh. Chứ tạo UseCase rồi Repository thì lâu lắm."*

Mình gật. Vì đúng là nhanh hơn. Và tính năng đó live trong vòng 2 giờ.

Nhưng 2 tuần sau, mình cần thêm tính năng: hiển thị portfolio đó trên cả màn hình home và màn hình chi tiết. Lúc đó mới nhận ra: vì bypass Domain layer, logic fetch data bị duplicate ở 2 nơi. Khi API thay đổi response format, mình phải fix ở 2 chỗ. Và dĩ nhiên, fix xong chỗ này — chỗ kia crash.

**Cái "nhanh hơn 2 giờ" ban đầu — trả giá bằng 2 ngày refactor sau đó.**

Bài học: shortcut kiến trúc không bao giờ là shortcut. Nó là debt. Và lãi suất của nó cao hơn bạn tưởng.

---

### Tóm lại: Giữ xương sống, delegate phần còn lại

Bạn không cần phải viết mọi dòng code. Nhưng bạn cần biết **dòng nào không được phép sai kiến trúc.**

1. **Viết ARCHITECTURE.md** — ghi rõ pattern, boundary, rule mà AI phải follow. Feed nó trước mỗi lần nhờ AI code.
2. **Review kiến trúc trước khi review code** — đừng đọc từng dòng. Nhìn tổng thể: module nào gọi module nào? Dependency có đúng chiều không? Boundary có bị phá không?
3. **Không bao giờ bypass Domain layer vì "cho nhanh"** — shortcut hôm nay là tech debt ngày mai.

Nhưng mình đã mất một thời gian để nhận ra: Giữ được "xương sống" là tốt. Nhưng nếu requirement mơ hồ, AI sẽ xây đúng cấu trúc — nhưng sai hoàn toàn tính năng. Và đó là chuyện của tập tiếp theo.

**Đó sẽ là chủ đề của tập tiếp theo.**

> 👉 **[Tập 3 — Làm PM Khi AI Code Cho Bạn: AI Viết Đúng Những Gì Bạn Nói, Nhưng Sai Những Gì Bạn Cần](#)**

Anh em có câu chuyện nào AI "refactor" xong thì hệ thống vỡ không? Share dưới comment — mình đoán không chỉ mình đâu. 😅

---

*Nếu bài viết này có ích, một cái 👏 là cách tốt nhất để giúp nó đến tay nhiều developer hơn. Follow để không bỏ lỡ các tập tiếp theo trong series.*
