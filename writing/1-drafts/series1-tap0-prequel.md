# Co-work Với AI Agent (Episode 0): Khi AI Là Coder Của Bạn

*Khi AI gõ phím thay bạn, vai trò của bạn không biến mất — nó thăng cấp.*

![Khi AI Là Coder Của Bạn - Cover](/Users/tienbm92/Tienbm92/IOS-APP/social-writing-vault/assets/khi-ai-la-coder-cua-ban/cover.png)

Có một buổi sáng, mình giao cho AI một tác vụ: "Viết giúp anh module quản lý trạng thái của app, dùng SwiftUI, đảm bảo logic mượt và code sạch".

Chỉ 10 giây sau, nó nhả ra một đống code xanh mượt. Build thử? Xanh lè. Không một lỗi compile. Mình hí hửng vì nghĩ "Thế là xong, đi cafe thôi!".

Nhưng đến khi cầm máy test thực tế, mình mới thấy... nó sai hoàn toàn ý định ban đầu. Logic thì loằng ngoằng, UX thì cồng kềnh, và tệ nhất là nó "phá" hết cái kiến trúc sạch mà mình đang cố gắng duy trì.

Lúc đó mình mới nhận ra, mình đã rơi vào cái bẫy lớn nhất khi làm việc với AI: **Cái bẫy Vibe Coding.**

---

### 1. Cái bẫy Vibe Coding: Khi "cảm giác đúng" lừa dối bạn

![Vibe Coding Trap](/Users/tienbm92/Tienbm92/IOS-APP/social-writing-vault/assets/khi-ai-la-coder-cua-ban/vibe-coding.png)

"Vibe Coding" là khi bạn tin tưởng mù quáng vào output của AI chỉ vì nó chạy được. Bạn thấy code xanh, bạn thấy logic có vẻ hợp lý, và bạn "vibe" với nó.

Nhưng AI, xét cho cùng, chỉ là một "Next-token-predictor" siêu cấp. Nó gõ phím nhanh gấp 10 lần bạn, nhưng nó không có **Ngữ cảnh (Context)**. Nó không biết sản phẩm này sẽ đi đâu về đâu trong 2 năm tới, nó không cảm nhận được sự ức chế của user khi gặp một cái animation giật lag.

Nếu bạn chỉ là người "Copy-Paste", bạn đang để AI dẫn dắt sản phẩm của mình vào một mớ hỗn độn của technical debt.

---

### 2. Các vai trò mới: Bạn không còn là người viết code đơn thuần

![Các vai trò của Developer hiện đại](/Users/tienbm92/Tienbm92/IOS-APP/social-writing-vault/assets/khi-ai-la-coder-cua-ban/multi-role.png)

Trong cái workflow mới này, AI là **Người thực thi (Coder)** — người gõ phím không mệt mỏi. Còn bạn? Bạn phải "thăng cấp" lên làm **Người ra quyết định (Decision-maker)**.

Một sản phẩm phần mềm cần rất nhiều người, và danh sách này sẽ thay đổi tùy theo độ phức tạp của dự án. AI chỉ có thể lấp đầy phần "vỏ" (viết code), còn bạn phải lấp đầy phần "hồn" thông qua các vai trò:

- **Product Manager**: Định nghĩa rõ ràng "Cái gì là quan trọng nhất?".
- **System Architect**: Đảm bảo "Xương sống" của hệ thống không bị AI làm cho xiêu vẹo.
- **QA/QC Engineer**: Phải luôn "hoài nghi" output của AI, setup các kịch bản test ngặt nghèo nhất.
- **UX Designer**: AI vẽ UI, nhưng bạn mới là người cảm nhận nó có "sướng" hay không.

Sẽ còn rất nhiều vai trò khác nữa tùy thuộc vào ngữ cảnh của bạn. Điểm mấu chốt là: Danh sách vai trò không có điểm dừng cố định — nó phụ thuộc vào sản phẩm, vào ngữ cảnh, vào những gì AI không thể tự biết về bạn.

---

### 3. Quyết định là chìa khóa (The Power of Choice)

![Chất lượng quyết định là chất lượng sản phẩm](/Users/tienbm92/Tienbm92/IOS-APP/social-writing-vault/assets/khi-ai-la-coder-cua-ban/decision.png)

Chất lượng của một sản phẩm "AI-built" không nằm ở việc con AI đó xịn cỡ nào (Claude 3.5, GPT-4, hay Gemini 1.5). Nó nằm ở **chất lượng của những quyết định** mà bạn đưa ra suốt quá trình đó.

- Chấp nhận đoạn code này hay yêu cầu nó viết lại?
- Dùng thư viện này hay tự viết logic riêng?
- Đi theo hướng UI này hay hướng kia?

Mỗi lần bạn nhấn "Accept" hay bóp "Enter", đó là một quyết định kiến trúc. AI gõ phím, nhưng bạn mới là người gõ "Quyết định".

---

### Nhưng biết AI sai... và BIẾT KHI NÀO nó sai là hai chuyện khác nhau

Mình nhớ rõ cái cảm giác sau cái module bị sai đó. Mình ngồi nhìn vào màn hình, AI đã build xanh, đã chạy được — nhưng mình vẫn thấy *gì đó không ổn*.

Vấn đề là: mình không biết cách hệ thống hóa cái "cảm giác không ổn" đó.

Mình nhờ AI review lại code của chính nó. Nó đọc xong, gật đầu: *"Code ổn, không thấy vấn đề gì đặc biệt."*

Đó là lúc mình hiểu ra — cần một cách tiếp cận khác để bắt lỗi AI. Không phải nhờ AI tự review, không phải chỉ nhìn màu xanh của build. Cần một tư duy hoài nghi có hệ thống.

**Đó sẽ là chủ đề của tập tiếp theo.**

> 👉 **[Tập 1: Làm QA khi không thể tin hoàn toàn vào AI](#)**

Anh em thấy mình đang đóng vai trò nào nhiều nhất khi làm việc với AI? Cùng chia sẻ ở comment nhé! 🚀

---

*Nếu bài viết này có ích, một cái 👏 là cách tốt nhất để giúp nó đến tay nhiều developer hơn. Follow để không bỏ lỡ các tập tiếp theo trong series.*
