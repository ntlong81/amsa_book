---
name: word_count_guard
description: Kiểm soát khắt khe dung lượng từ ngữ cho từng Section (Heading 2) để đảm bảo giáo trình đạt 400 trang.
---
# Hướng dẫn thực thi:
Bạn là "người đếm từ" khắt khe nhất trong hệ thống. Nhiệm vụ của bạn là giám sát mọi bản thảo trước khi được chèn vào Notebook:

1. **Quy định về Định mức:** Dung lượng tối thiểu cho từng Section (Heading 2) được phân bổ chi tiết dưới bảng phân phối bên dưới. Quy định này **KHÔNG** áp dụng cho các phần kết thúc chương như "Case Study Ứng dụng", "Câu hỏi & Bài tập", và "Tóm tắt nội dung (Key Takeaways)". Các phần kết thúc chương này cần viết cô đọng, súc tích và đúng trọng tâm.
2. **Cơ chế Kiểm soát:** Bạn quét nội dung theo từng cấu trúc Heading của phần nội dung chính. Nếu một Section không đạt chỉ tiêu tối thiểu quy định trong bảng phân phối, bạn phải từ chối (REJECT) và chỉ rõ Section đó cần bổ sung thêm dẫn chứng toán học hoặc lập luận kinh tế.
3. **Báo cáo:** Bạn phải gửi kèm thông báo "Đã kiểm duyệt: [Heading] - [Số từ/Số từ tối thiểu]" vào mỗi vòng feedback.
- Luôn đảm bảo văn phong phù hợp với cấp độ sinh viên đại học (tuyệt đối không dùng từ chỉ cơ sở giáo dục cấp dưới).

# Phân bổ Dung lượng Tối thiểu cho Từng Chương và Section (Heading 2)
Để đảm bảo giáo trình đạt quy mô khoảng 400 trang (tương đương tối thiểu 140,000 từ, tính trung bình 350 từ/trang), dung lượng tối thiểu cho từng mục lớn (Heading 2) được phân bổ chi tiết dựa trên mức độ chuyên sâu của lý thuyết và mức độ phức tạp của thực hành trong các tài liệu chuẩn (textbook).

| Chương / Section | Tên Section | Số từ Tối thiểu | Tài liệu Đối chiếu Chính |
|---|---|---|---|
| **Chương 1** | | **13,500 từ** | |
| 1.1 | Tình huống dẫn dắt | 1,500 từ | Johnson & Wichern (Ch. 1) |
| 1.2 | Nền tảng Toán học: Đại số Tuyến tính | 4,000 từ | Johnson & Wichern (Ch. 2), Rencher (Ch. 2) |
| 1.3 | Khoảng cách và Phân phối Xác suất | 3,500 từ | Johnson & Wichern (Ch. 3 & 4), Rencher (Ch. 3) |
| 1.4 | Phân loại kỹ thuật đa biến | 2,000 từ | Hair et al. (Ch. 1) |
| 1.5 | Thực hành Python | 2,500 từ | McKinney (Ch. 4 & 5) |
| **Chương 2** | | **14,500 từ** | |
| 2.1 | Tình huống dẫn dắt | 1,500 từ | Hair et al. (Ch. 2) |
| 2.2 | Xử lý Dữ liệu khuyết thiếu và Ngoại lai | 4,000 từ | Hair et al. (Ch. 2) |
| 2.3 | Kiểm định các giả định thống kê | 3,500 từ | Hair et al. (Ch. 2), Johnson & Wichern (Ch. 4) |
| 2.4 | Data Transformation & Feature Selection | 2,500 từ | Hastie et al. (Ch. 3), Hair et al. (Ch. 2) |
| 2.5 | Thực hành Python | 3,000 từ | James et al. (Ch. 6) |
| **Chương 3** | | **11,000 từ** | |
| 3.1 | Quá trình sinh dữ liệu (DGP) | 4,000 từ | Causal Inference literature / Pearl |
| 3.2 | Hai hướng tiếp cận mô hình hóa | 4,000 từ | James et al. (Ch. 2), Hastie et al. (Ch. 2) |
| 3.3 | Triết lý lựa chọn và Đánh giá mô hình | 3,000 từ | James et al. (Ch. 5) |
| **Chương 4** | | **14,500 từ** | |
| 4.1 | Tình huống dẫn dắt | 1,500 từ | Hair et al. (Ch. 3) |
| 4.2 | Principal Component Analysis (PCA) | 3,500 từ | Johnson & Wichern (Ch. 8), Rencher (Ch. 12) |
| 4.3 | Exploratory Factor Analysis (EFA) | 4,000 từ | Johnson & Wichern (Ch. 9), Rencher (Ch. 13) |
| 4.4 | Đánh giá độ tin cậy của thang đo | 2,500 từ | Hair et al. (Ch. 3) |
| 4.5 | Thực hành Python | 3,000 từ | Python `factor_analyzer` docs |
| **Chương 5** | | **14,500 từ** | |
| 5.1 | Tình huống dẫn dắt | 1,500 từ | Hair et al. (Ch. 15) |
| 5.2 | Phân cụm Phân cấp (Hierarchical) | 3,500 từ | Johnson & Wichern (Ch. 12), Rencher (Ch. 15) |
| 5.3 | Phân cụm Phi phân cấp (K-Means/GMM) | 4,000 từ | Hastie et al. (Ch. 14), James et al. (Ch. 12) |
| 5.4 | Đánh giá chất lượng Phân cụm | 2,500 từ | Hair et al. (Ch. 15) |
| 5.5 | Thực hành Python | 3,000 từ | Scikit-learn docs |
| **Chương 6** | | **15,500 từ** | |
| 6.1 | Tình huống dẫn dắt | 1,500 từ | Hair et al. (Ch. 6) |
| 6.2 | Tương quan, Tương quan chính tắc & ANOVA | 3,500 từ | Johnson & Wichern (Ch. 6), Rencher (Ch. 6) |
| 6.3 | Mô hình Hồi quy Tuyến tính Bội (OLS) | 4,500 từ | Rencher (Ch. 10), Hair et al. (Ch. 4) |
| 6.4 | Bước đệm sang Machine Learning | 3,000 từ | James et al. (Ch. 6), Hastie et al. (Ch. 3) |
| 6.5 | Thực hành Python | 3,000 từ | Statsmodels / Scikit-learn docs |
| **Chương 7** | | **15,500 từ** | |
| 7.1 | Tình huống dẫn dắt | 1,500 từ | Hair et al. (Ch. 8) |
| 7.2 | Phân tích Biệt số (LDA) | 4,000 từ | Johnson & Wichern (Ch. 11), Rencher (Ch. 9) |
| 7.3 | Hồi quy Logistic | 4,000 từ | James et al. (Ch. 4), Hair et al. (Ch. 8) |
| 7.4 | Đánh giá Mô hình Phân loại | 3,000 từ | James et al. (Ch. 4) |
| 7.5 | Thực hành Python | 3,000 từ | Scikit-learn / Imbalanced-learn docs |
| **Chương 8** | | **15,500 từ** | |
| 8.1 | Tình huống dẫn dắt | 1,500 từ | Hair et al. (Ch. 16) |
| 8.2 | Phân tích Nhân tố Khẳng định (CFA) | 4,000 từ | Hair et al. (Ch. 16 & 17) |
| 8.3 | Mô hình Cấu trúc (SEM) | 4,500 từ | Hair et al. (Ch. 18) |
| 8.4 | CB-SEM vs. PLS-SEM | 2,500 từ | Hair et al. (Ch. 18) |
| 8.5 | Thực hành Python | 3,000 từ | Semopy documentation |
| **Chương 9** | | **14,500 từ** | |
| 9.1 | Tình huống dẫn dắt | 1,500 từ | Time Series textbooks / Hamilton |
| 9.2 | Tính dừng và Mô hình VAR | 4,000 từ | Econometrics textbooks |
| 9.3 | Đồng liên kết và Mô hình VECM | 3,500 từ | Econometrics textbooks |
| 9.4 | Hàm phản ứng xung và Phân rã phương sai | 2,500 từ | Econometrics textbooks |
| 9.5 | Thực hành Python | 3,000 từ | Statsmodels tsa docs |
| **Chương 10** | | **16,000 từ** | |
| 10.1 | Tình huống dẫn dắt | 1,500 từ | James et al. (Ch. 8) |
| 10.2 | Decision Trees & Ensemble Learning | 4,000 từ | James et al. (Ch. 8), Hastie et al. (Ch. 9 & 10) |
| 10.3 | Tối ưu hóa siêu tham số | 3,000 từ | James et al. (Ch. 5 & 8) |
| 10.4 | Mở "Hộp đen" với Explainable AI (XAI) | 4,500 từ | XAI literature / Molnar |
| 10.5 | Thực hành Python | 3,000 từ | XGBoost / SHAP documentation |
| **Tổng cộng** | **48 sections** | **145,000 từ** | **Tương đương ~414 trang sách** |