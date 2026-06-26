---
name: causal_vs_predictive_writer
description: Áp dụng khi viết các chương về Hồi quy (Chương 6, 7), SEM (Chương 8) và Machine Learning (Chương 10).
---
# Hướng dẫn thực thi:
- **Linh hoạt Tiểu mục (Subsection Flexibility):** BẮT BUỘC giữ nguyên tên và thứ tự các mục lớn (Heading 2 - ví dụ 6.1, 6.2) theo đúng đề cương. Tuy nhiên, đối với các tiểu mục (Heading 3 trở xuống - ví dụ 6.2.1), bạn ĐƯỢC QUYỀN tự do thêm, bớt, gộp hoặc điều chỉnh tên sao cho mạch văn học thuật được liền mạch, logic và phù hợp nhất với luồng phân tích.
- **Quy chuẩn Văn phong Giáo trình (Textbook Prose):** Trình bày nội dung dưới dạng văn xuôi học thuật phân tích chuyên sâu, liền mạch. Tuyệt đối không viết kiểu bài giảng tóm tắt hay liệt kê bề mặt. Mỗi khái niệm, mô hình phải được diễn giải cặn kẽ bằng các đoạn văn hoàn chỉnh, lập luận chặt chẽ. Chỉ sử dụng danh sách khi thật sự cần thiết.
- **Quy tắc Trích dẫn (Citation Rule):** Ưu tiên tìm kiếm và trích dẫn thông tin từ các tài liệu trong thư mục `textbook/`. Chỉ dùng nguồn ngoài khi thật sự cần thiết và phải ghi rõ nguồn.
- Khi viết về mô hình hồi quy truyền thống (OLS, Logistic): Đi sâu phân tích bằng văn xuôi để giải thích hệ số Beta, kiểm định giả thuyết, tính nội sinh, và bẫy OVB.
- Khi viết về mô hình học máy: Chuyển hẳn trục tư duy sang kiểm chứng out-of-sample, đánh giá Bias-Variance Tradeoff, và Cross-validation. Phải giải thích cơ chế toán học bên trong thuật toán.
- Tuyệt đối không để xảy ra sự nhầm lẫn giữa tương quan phân tích dự báo và quan hệ nhân quả trong văn phong.
- **Phân chia nhiệm vụ cuối chương:** Tránh viết chồng lấn vào các mục "Case Study Ứng dụng", "Câu hỏi & Bài tập", và "Tóm tắt nội dung (Key Takeaways)" ở cuối chương vì các phần này sẽ do các Agent chuyên biệt khác (như `@assessment_generator`) phụ trách.
- Luôn đảm bảo văn phong phù hợp với cấp độ sinh viên đại học (tuyệt đối không dùng từ chỉ cơ sở giáo dục cấp dưới).