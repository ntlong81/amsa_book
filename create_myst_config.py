import os
import yaml

dest_book = r"d:\CODE\amsa_book\my_book"

# Delete _config.yml and _toc.yml if they exist to avoid confusion
for f in ["_config.yml", "_toc.yml"]:
    p = os.path.join(dest_book, f)
    if os.path.exists(p):
        os.remove(p)
        print(f"Removed old {f}")

# Define myst.yml contents
myst_config = {
    "version": 1,
    "project": {
        "title": "Giáo trình Phân tích Dữ liệu Đa biến Ứng dụng (AMSA)",
        "description": "Giáo trình hướng dẫn thực hành Phân tích Đa biến sử dụng Python",
        "authors": [
            {"name": "AMSA Team"}
        ],
        "toc": [
            {"file": "chapters/00_Loi_Noi_Dau.ipynb"},
            {"file": "chapters/00_Muc_Luc.ipynb"},
            {"file": "chapters/01_Chuong_1.ipynb"},
            {"file": "chapters/02_Chuong_2.ipynb"},
            {"file": "chapters/03_Chuong_3.ipynb"},
            {"file": "chapters/04_Chuong_4.ipynb"},
            {"file": "chapters/05_Chuong_5.ipynb"},
            {"file": "chapters/06_Chuong_6.ipynb"},
            {"file": "chapters/07_Chuong_7.ipynb"},
            {"file": "chapters/08_Chuong_8.ipynb"},
            {"file": "chapters/09_Chuong_9.ipynb"},
            {"file": "chapters/10_Chuong_10.ipynb"},
            {"file": "chapters/11_Tong_Ket.ipynb"},
            {"file": "chapters/99_Tai_Lieu_Tham_Khao.ipynb"}
        ]
    },
    "site": {
        "template": "book-theme"
    }
}

with open(os.path.join(dest_book, "myst.yml"), "w", encoding="utf-8") as f:
    yaml.dump(myst_config, f, default_flow_style=False, allow_unicode=True)
print("Created myst.yml configuration successfully.")
