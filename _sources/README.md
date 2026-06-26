# Giáo trình Thực hành Phân tích Dữ liệu và Mô hình hóa với Python

Chào mừng bạn đến với kho lưu trữ mã nguồn và dữ liệu thực hành của dự án **Sách/Giáo trình Phân tích Dữ liệu và Mô hình hóa với Python**. Kho lưu trữ này cung cấp toàn bộ các file Jupyter Notebook, dữ liệu Case Study và môi trường để bạn có thể học tập, chạy thử nghiệm và tự tay xây dựng các báo cáo phân tích từ cơ bản đến nâng cao.

## 📖 Nội dung các chương

Cuốn sách được thiết kế theo lộ trình từ tiền xử lý dữ liệu cho đến các mô hình thống kê và máy học chuyên sâu. Toàn bộ mã nguồn nằm trong thư mục `chapters/`:

- **Chương 0 - 3:** Khởi động, Thu thập, Tiền xử lý và Làm sạch dữ liệu.
- **Chương 4:** Khám phá cấu trúc dữ liệu với **EFA** (Exploratory Factor Analysis) và **PCA** (Principal Component Analysis).
- **Chương 5 - 7:** Các thuật toán Machine Learning (Phân loại, Hồi quy) và Kỹ thuật Resampling (xử lý dữ liệu mất cân bằng).
- **Chương 8:** Mô hình cấu trúc tuyến tính **SEM** (Structural Equation Modeling) và **CFA** (Confirmatory Factor Analysis).
- **Chương 9 - 10:** Phân tích Chuỗi thời gian (Time Series), Mô hình **VAR** (Vector Autoregression), **VECM**, và Dự báo (Forecasting).
- **Chương 11:** Tổng kết và định hướng phát triển.
- **Phụ lục:** Tài liệu tham khảo học thuật (`references.bib`).

## 🗂 Cấu trúc thư mục dự án

```text
├── case_studies/           # Chứa toàn bộ các file dữ liệu (.csv, .xlsx) cho bài tập thực hành.
├── chapters/               # Mã nguồn chính (.ipynb). Mỗi chương là một notebook độc lập.
│   └── images/             # Nơi lưu trữ các biểu đồ, hình ảnh EDA được xuất ra trong quá trình chạy code.
├── my_book/                # Thư mục cấu hình Jupyter Book (chứa _config.yml, _toc.yml).
├── requirements.txt        # Danh sách các thư viện Python và phiên bản tương thích cần thiết.
├── README.md               # Tài liệu mô tả dự án này.
└── .gitignore              # Định nghĩa các tệp rác không đẩy lên GitHub.
```

## 🚀 Hướng dẫn cài đặt và sử dụng

Dự án này sử dụng Python. Để đảm bảo tất cả các file code hoạt động trơn tru (đặc biệt là các thư viện đặc thù như `semopy` hay `factor_analyzer`), vui lòng thiết lập môi trường y hệt như cấu hình chuẩn.

**Bước 1: Clone dự án về máy**
```bash
git clone https://github.com/your-username/amsa_book.git
cd amsa_book
```

**Bước 2: Cài đặt thư viện**
Khuyến nghị bạn tạo một môi trường ảo (virtual environment) trước khi cài đặt.
```bash
pip install -r requirements.txt
```

**Bước 3: Chạy Jupyter Notebook**
```bash
jupyter notebook
```
Sau đó, bạn điều hướng vào thư mục `chapters/` và mở lần lượt các file `.ipynb` để chạy thực hành.

## 📚 Build phiên bản Sách Web (HTML Book)

Kho lưu trữ này được tích hợp sẵn cấu hình **Jupyter Book** để chuyển đổi toàn bộ mã nguồn thành một website học liệu trực quan. Để tự build sách HTML trên máy của bạn:

```bash
# Di chuyển vào thư mục dự án
cd amsa_book

# Build thư mục my_book/
jupyter-book build my_book/
```

Sau khi quá trình build kết thúc thành công, bạn chỉ cần mở file `my_book/_build/html/index.html` trên trình duyệt web để bắt đầu đọc sách!

## 💡 Lưu ý về phiên bản (Versioning)
- Để tránh xung đột API nội bộ (cụ thể ở hàm `check_array`), dự án này đã cố định phiên bản `scikit-learn==1.5.2` để tương thích hoàn toàn với thư viện phân tích nhân tố `factor_analyzer`. Xin lưu ý nếu bạn có ý định nâng cấp thư viện này lên các bản `1.6.x` trở lên.

---
*Dự án này được xây dựng với mục tiêu giáo dục và lan tỏa tri thức về khoa học dữ liệu.*
