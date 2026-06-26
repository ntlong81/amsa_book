# DANH MỤC THUẬT NGỮ CHUYÊN NGÀNH (GLOSSARY GUARD)

Để đảm bảo sự chuẩn xác theo thông lệ học thuật quốc tế và thuận tiện cho người học trong việc tra cứu tài liệu nước ngoài hoặc lập trình, các thuật ngữ dưới đây sẽ được giữ nguyên bản tiếng Anh xuyên suốt nội dung cuốn giáo trình.

* **Bias-Variance Tradeoff (Sự đánh đổi giữa Độ chệch và Phương sai):** Khái niệm cốt lõi trong học máy giải thích sự đánh đổi giữa việc mô hình quá đơn giản dẫn đến bỏ sót quy luật (High Bias) và mô hình quá phức tạp dẫn đến học thuộc lòng cả nhiễu (High Variance).
* **Cluster Analysis (Phân tích Cụm):** Nhóm thuật toán học không giám sát nhằm gom các điểm dữ liệu thành từng cụm sao cho các điểm trong cùng một cụm có đặc tính giống nhau nhất.
* **Cointegration (Đồng liên kết):** Hiện tượng hai hay nhiều chuỗi thời gian tuy không dừng (non-stationary) nhưng lại di chuyển cùng nhau theo một xu hướng cân bằng chung trong dài hạn.
* **Cross-validation (Kiểm chứng chéo):** Kỹ thuật đánh giá mô hình bằng cách chia tập dữ liệu thành nhiều phần, lặp lại quá trình huấn luyện và kiểm tra nhiều lần nhằm đảm bảo sự ổn định của kết quả.
* **Data Generating Process - DGP (Quá trình sinh dữ liệu):** Quy luật tự nhiên, cơ chế thực tế hoặc tập hợp các nguyên nhân ngầm định tạo ra tập dữ liệu mà chúng ta quan sát được.
* **Data Leakage (Rò rỉ dữ liệu):** Sai lầm nghiêm trọng khi thông tin từ tập dữ liệu kiểm tra (test set) vô tình bị rò rỉ và tác động vào quá trình huấn luyện mô hình (training set), tạo ra kết quả đánh giá ảo tưởng.
* **Dependence Techniques (Nhóm kỹ thuật Phụ thuộc):** Các phương pháp thống kê (như Hồi quy, ANOVA) trong đó có sự phân định rạch ròi biến nào là biến nguyên nhân/dự báo (độc lập) và biến nào là biến kết quả (phụ thuộc).
* **Endogeneity (Tính nội sinh):** Tình trạng một biến độc lập trong mô hình có tương quan với phần dư (sai số), thường do bỏ sót biến hoặc quan hệ nhân quả hai chiều, dẫn đến hệ số ước lượng bị sai lệch.
* **Explainable AI - XAI (Trí tuệ nhân tạo có thể giải thích):** Bộ các kỹ thuật (như SHAP, LIME) giúp con người "mở hộp đen" học máy, hiểu được lý do tại sao mô hình lại đưa ra một dự báo cụ thể.
* **Feature Selection / Feature Engineering (Chọn lọc / Kỹ nghệ Đặc trưng):** Quá trình biến đổi, tạo mới hoặc loại bỏ bớt các biến số (features) để giúp mô hình học tập hiệu quả và chính xác hơn.
* **Impulse Response Function - IRF (Hàm phản ứng xung):** Công cụ trong chuỗi thời gian dùng để đo lường đường đi của một biến số sau khi nó hoặc một biến khác trong hệ thống chịu một cú sốc đột ngột.
* **Interdependence Techniques (Nhóm kỹ thuật Tương thuộc):** Các phương pháp (như PCA, EFA, Phân cụm) không phân biệt biến độc lập hay phụ thuộc, chỉ tập trung vào khám phá cấu trúc và mối liên hệ giữa toàn bộ các biến.
* **Latent Variables / Constructs (Biến tiềm ẩn / Khái niệm đo lường):** Các khái niệm vô hình không thể đo lường trực tiếp bằng một con số (ví dụ: Sự hài lòng, Rủi ro hệ thống) mà phải suy ra từ các biến quan sát được.
* **Missing at Random - MAR (Khuyết thiếu ngẫu nhiên):** Tình trạng dữ liệu bị thiếu có thể dự đoán/giải thích được thông qua các biến khác đã có trong tập dữ liệu (VD: Nam giới thường ít điền thông tin thu nhập). Khác với MCAR (Missing Completely at Random) là khuyết thiếu hoàn toàn ngẫu nhiên.
* **Multicollinearity (Đa cộng tuyến):** Hiện tượng hai hay nhiều biến độc lập trong mô hình hồi quy có mối tương quan tuyến tính quá mạnh với nhau, làm mất tính ổn định của các hệ số ước lượng.
* **Omitted Variable Bias - OVB (Thiên lệch do bỏ sót biến):** Sự méo mó, sai lệch của hệ số hồi quy xảy ra khi ta quên không đưa một biến quan trọng vào mô hình, mà biến này lại có tương quan với cả biến độc lập và biến phụ thuộc hiện tại.
* **Outliers (Ngoại lai):** Các điểm dữ liệu có giá trị bất thường, nằm quá xa so với phần lớn dữ liệu còn lại trong không gian đa chiều, có khả năng làm sai lệch toàn bộ mô hình.
* **Overfitting / Underfitting (Quá khớp / Kém khớp):** Overfitting là khi mô hình quá phức tạp, học thuộc lòng cả nhiễu và làm kém trên dữ liệu mới. Underfitting là khi mô hình quá đơn giản, không học được quy luật cơ bản nào.
* **Principal Component Analysis - PCA (Phân tích Thành phần chính):** Kỹ thuật giảm chiều dữ liệu bằng cách biến đổi các biến gốc có tương quan thành các "thành phần chính" mới vuông góc (không tương quan) với nhau.
* **Regularization (Điều chuẩn / Chuẩn hóa mô hình):** Kỹ thuật toán học thêm "hình phạt" (penalty) vào mô hình để kìm hãm độ lớn của các hệ số hồi quy, ngăn chặn tình trạng quá khớp (VD: Ridge, Lasso).
* **Stationarity (Tính dừng):** Đặc tính của một chuỗi thời gian khi các giá trị thống kê cốt lõi của nó (trung bình, phương sai) không bị thay đổi theo thời gian.
* **Exploratory Factor Analysis - EFA (Phân tích Nhân tố Khám phá):** Kỹ thuật thống kê dùng để rút gọn một tập hợp nhiều biến quan sát thành một số ít các nhân tố ẩn mà không cần giả định trước cấu trúc lý thuyết.
* **Confirmatory Factor Analysis - CFA (Phân tích Nhân tố Khẳng định):** Kỹ thuật dùng để kiểm định xem cấu trúc đo lường (mối quan hệ giữa biến ẩn và các biến quan sát) có phù hợp với mô hình lý thuyết đề ra hay không.
* **Structural Equation Modeling - SEM (Mô hình hóa Phương trình Cấu trúc):** Khung phân tích thống kê toàn diện kết hợp giữa CFA (mô hình đo lường) và phân tích hồi quy đường dẫn (mô hình cấu trúc) để kiểm định đồng thời các mối quan hệ phức tạp giữa nhiều biến ẩn và biến quan sát.
* **Vector Autoregression - VAR (Mô hình Tự hồi quy Vector):** Mô hình kinh tế lượng chuỗi thời gian đa biến trong đó tất cả các biến đều được coi là nội sinh và tác động qua lại lẫn nhau qua các độ trễ thời gian.
* **Vector Error Correction Model - VECM (Mô hình Hiệu chỉnh Sai số Vector):** Mô hình chuỗi thời gian đa biến được áp dụng khi các chuỗi dữ liệu không dừng nhưng có mối quan hệ đồng liên kết dài hạn, giúp phân tích các biến động ngắn hạn và cơ chế tự điều chỉnh về trạng thái cân bằng dài hạn.
* **Discriminant Analysis / Linear Discriminant Analysis - LDA (Phân tích Biệt số Tuyến tính):** Phương pháp phân loại thống kê tìm kiếm các tổ hợp tuyến tính của các biến độc lập để phân tách tối đa các nhóm đối tượng khác nhau.
* **Odds Ratio (Tỷ số chênh / Tỷ lệ chênh):** Thước đo sức mạnh liên kết giữa hai biến, biểu thị tỷ lệ giữa khả năng xảy ra một sự kiện so với khả năng sự kiện đó không xảy ra dưới tác động của một yếu tố.

---

## TÀI LIỆU THAM KHẢO CHÍNH (REFERENCES)

### Nhóm lý thuyết nền tảng
1. Johnson, R. A., & Wichern, D. W. *Applied Multivariate Statistical Analysis* (6th Edition).
2. Rencher, A. C., & Christensen, W. F. (2012). *Methods of Multivariate Analysis* (Third Edition).

### Nhóm ứng dụng kinh doanh
3. Hair, J. F., Black, W. C., Babin, B. J., & Anderson, R. E. (2018). *Multivariate Data Analysis* (8th Edition). Cengage.

### Nhóm Data Science
4. James, G., Witten, D., Hastie, T., & Tibshirani, R. *An Introduction to Statistical Learning with Applications in Python*.
5. Hastie, T., Tibshirani, R., & Friedman, J. (2008). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction* (Second Edition).

### Nhóm thực hành lập trình
6. Schumacker, R. E. (2016). *Using R with Multivariate Statistics*.
7. McKinney, W. (2022). *Python for Data Analysis*.
