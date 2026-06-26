import json
import os

chapters_dir = r"d:\CODE\amsa_book\chapters"

# Fix Chapter 4
path4 = os.path.join(chapters_dir, "04_Chuong_4.ipynb")
with open(path4, "r", encoding="utf-8") as f:
    data = json.load(f)

changed = False
for cell in data.get("cells", []):
    if cell.get("cell_type") == "markdown":
        source = cell.get("source", [])
        new_source = []
        for line in source:
            if line.strip() == "## Case Study":
                line = line.replace("## Case Study", "## Case Study Ứng dụng")
                changed = True
            elif line.strip() == "## Tóm tắt nội dung":
                line = line.replace("## Tóm tắt nội dung", "## Tóm tắt nội dung (Key Takeaways)")
                changed = True
            new_source.append(line)
        cell["source"] = new_source

if changed:
    with open(path4, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1)
    print("Fixed Chapter 4.")

# Create 00_Muc_Luc.ipynb
muc_luc_content = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# MỤC LỤC\n",
    "\n",
    "Đây là trang mục lục tổng thể của toàn bộ giáo trình. Giúp độc giả dễ dàng định vị các chương và các khái niệm cốt lõi trong sách."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
with open(os.path.join(chapters_dir, "00_Muc_Luc.ipynb"), "w", encoding="utf-8") as f:
    json.dump(muc_luc_content, f, indent=1)
print("Created 00_Muc_Luc.ipynb")

# Create 11_Tong_Ket.ipynb
tong_ket_content = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# TỔNG KẾT GIÁO TRÌNH\n",
    "\n",
    "Phần này khép lại toàn bộ luồng công việc (pipeline) xử lý dữ liệu và mô hình hóa. Từ việc làm sạch dữ liệu ban đầu, đến phân tích các cấu trúc ẩn bằng PCA/EFA, khám phá cấu trúc cụm khách hàng, cho đến việc dự báo bằng các mô hình hiện đại như XGBoost và giải thích bằng SHAP.\n",
    "\n",
    "Hy vọng cuốn giáo trình đã mang lại cho bạn đọc một cái nhìn hệ thống và sâu sắc về Phân tích Đa biến."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
with open(os.path.join(chapters_dir, "11_Tong_Ket.ipynb"), "w", encoding="utf-8") as f:
    json.dump(tong_ket_content, f, indent=1)
print("Created 11_Tong_Ket.ipynb")

# Clear note.txt
open(r"d:\CODE\amsa_book\note.txt", "w").close()
print("Cleared note.txt")
