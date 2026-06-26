import os
import shutil
import yaml

src_chapters = r"d:\CODE\amsa_book\chapters"
dest_book = r"d:\CODE\amsa_book\my_book"
dest_chapters = os.path.join(dest_book, "chapters")

# 1. Create directories
os.makedirs(dest_chapters, exist_ok=True)
print("Created directories.")

# 2. Copy chapters files and images recursive
if os.path.exists(src_chapters):
    # Copy everything inside chapters to my_book/chapters
    for item in os.listdir(src_chapters):
        s = os.path.join(src_chapters, item)
        d = os.path.join(dest_chapters, item)
        if os.path.isdir(s):
            if item == ".ipynb_checkpoints":
                continue
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)
    print("Copied chapters and images.")

# Copy references.bib
src_bib = r"d:\CODE\amsa_book\references.bib"
if os.path.exists(src_bib):
    shutil.copy2(src_bib, os.path.join(dest_book, "references.bib"))
    print("Copied references.bib")

# 3. Create _config.yml
config = {
    "title": "Giáo trình Phân tích Dữ liệu Đa biến Ứng dụng (AMSA)",
    "author": "AMSA Team",
    "logo": "",
    "execute": {
        "execute_notebooks": "off"
    },
    "html": {
        "use_issues_button": False,
        "use_repository_button": False
    }
}

with open(os.path.join(dest_book, "_config.yml"), "w", encoding="utf-8") as f:
    yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
print("Created _config.yml")

# 4. Create _toc.yml
toc = {
    "format": "jb-book",
    "root": "chapters/00_Loi_Noi_Dau",
    "chapters": [
        {"file": "chapters/00_Muc_Luc"},
        {"file": "chapters/01_Chuong_1"},
        {"file": "chapters/02_Chuong_2"},
        {"file": "chapters/03_Chuong_3"},
        {"file": "chapters/04_Chuong_4"},
        {"file": "chapters/05_Chuong_5"},
        {"file": "chapters/06_Chuong_6"},
        {"file": "chapters/07_Chuong_7"},
        {"file": "chapters/08_Chuong_8"},
        {"file": "chapters/09_Chuong_9"},
        {"file": "chapters/10_Chuong_10"},
        {"file": "chapters/11_Tong_Ket"},
        {"file": "chapters/99_Tai_Lieu_Tham_Khao"}
    ]
}

with open(os.path.join(dest_book, "_toc.yml"), "w", encoding="utf-8") as f:
    yaml.dump(toc, f, default_flow_style=False, allow_unicode=True)
print("Created _toc.yml")
