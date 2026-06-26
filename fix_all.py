import json
import os
import re

chapters_dir = r"d:\CODE\amsa_book\chapters"

def fix_notebook(filename, replacements):
    path = os.path.join(chapters_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    changed = False
    for cell in data.get("cells", []):
        if cell.get("cell_type") == "markdown":
            source = cell.get("source", [])
            new_source = []
            for line in source:
                new_line = line
                for old_text, new_text in replacements.items():
                    if isinstance(old_text, re.Pattern):
                        new_line = old_text.sub(new_text, new_line)
                    elif old_text in new_line:
                        new_line = new_line.replace(old_text, new_text)
                if new_line != line:
                    changed = True
                new_source.append(new_line)
            cell["source"] = new_source
            
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1)
        print(f"Updated {filename}")
    else:
        print(f"No changes made to {filename}")

# Chapter 3
ch3_reps = {
    "## 3.4. Bài tập và Case Study": "## Case Study Ứng dụng",
    "### Bài tập và Case Study": "",
    "### Mini-Case Study:": "### Mini-Case Study:",
    "### Bài tập Lập trình": "## Câu hỏi & Bài tập\n### Bài tập Lập trình",
    "### Tóm tắt nội dung": "## Tóm tắt nội dung (Key Takeaways)"
}
fix_notebook("03_Chuong_3.ipynb", ch3_reps)

# Chapter 4
ch4_reps = {
    "## Case Study\n": "## Case Study Ứng dụng\n",
    "## Tóm tắt nội dung\n": "## Tóm tắt nội dung (Key Takeaways)\n"
}
fix_notebook("04_Chuong_4.ipynb", ch4_reps)

# Chapter 8
ch8_reps = {
    "### Ví dụ Số minh họa Tính toán AVE và CR": "### 8.2.2. Ví dụ Số minh họa Tính toán AVE và CR",
    "### Các Giả định Cần Kiểm tra Trước khi Chạy CFA": "### 8.2.3. Các Giả định Cần Kiểm tra Trước khi Chạy CFA",
    "### Chỉ số Modification Indices và Quyết định Tái chỉ định Mô hình": "### 8.2.4. Chỉ số Modification Indices và Quyết định Tái chỉ định Mô hình",
    "### CFA Bậc Hai (Second-Order CFA)": "### 8.2.5. CFA Bậc Hai (Second-Order CFA)",
    
    "### Phân tích Trung gian (Mediation Analysis) trong SEM": "### 8.3.2. Phân tích Trung gian (Mediation Analysis) trong SEM",
    "### Phân rã Tổng tác động và Ý nghĩa Quản trị": "### 8.3.3. Phân rã Tổng tác động và Ý nghĩa Quản trị",
    "### Chiến lược So sánh Mô hình và Kiểm định Nested Models": "### 8.3.4. Chiến lược So sánh Mô hình và Kiểm định Nested Models",
    "### 8.3.2. Chỉ số độ phù hợp (Model Fit: Chi-square, RMSEA, CFI, TLI)": "### 8.3.5. Chỉ số độ phù hợp (Model Fit: Chi-square, RMSEA, CFI, TLI)",
    "### Hướng dẫn Thực hành Đánh giá và Cải thiện Độ phù hợp": "### 8.3.6. Hướng dẫn Thực hành Đánh giá và Cải thiện Độ phù hợp",
    
    "### Bảng so sánh chi tiết CB-SEM và PLS-SEM": "### 8.4.1. Bảng so sánh chi tiết CB-SEM và PLS-SEM",
    "### Ví dụ Thực tế Phân biệt Khi Nào Dùng CB-SEM vs PLS-SEM": "### 8.4.2. Ví dụ Thực tế Phân biệt Khi Nào Dùng CB-SEM vs PLS-SEM",
    "### Hướng dẫn Ra quyết định Chọn Phương pháp": "### 8.4.3. Hướng dẫn Ra quyết định Chọn Phương pháp",
    "### Các Hiểu lầm Phổ biến về CB-SEM và PLS-SEM": "### 8.4.4. Các Hiểu lầm Phổ biến về CB-SEM và PLS-SEM",
    
    "### Diễn giải Kết quả SEM theo Góc nhìn Quản trị": "### 8.5.1. Diễn giải Kết quả SEM theo Góc nhìn Quản trị"
}
fix_notebook("08_Chuong_8.ipynb", ch8_reps)

# Chapter 9
ch9_reps = {
    "### Kiểm định chẩn đoán sau ước lượng VAR": "### 9.5.1. Kiểm định chẩn đoán sau ước lượng VAR"
}
fix_notebook("09_Chuong_9.ipynb", ch9_reps)

# Chapter 10
ch10_reps = {
    "### 10.4.1. Phân loại các Phương pháp Giải giải Mô hình": "### 10.4.1. Phân loại các Phương pháp Giải thích Mô hình",
    "### 10.4.1. LIME (Local Interpretable Model-agnostic Explanations)": "### 10.4.2. LIME (Local Interpretable Model-agnostic Explanations)",
    "### 10.4.2. Phân tích giá trị SHAP (SHapley Additive exPlanations)": "### 10.4.3. Phân tích giá trị SHAP (SHapley Additive exPlanations)",
    "##### C. Tóm tắt và định hướng thực hành": "#### 7. Tóm tắt và định hướng thực hành"
}
fix_notebook("10_Chuong_10.ipynb", ch10_reps)
