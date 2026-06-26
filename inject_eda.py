import json
import glob
import os

chapters_dir = r"d:\CODE\amsa_book\chapters"
notebooks = sorted(glob.glob(os.path.join(chapters_dir, "*.ipynb")))

eda_markdown = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "### Phân tích Khám phá Dữ liệu (EDA)\n",
        "\n",
        "Bước Phân tích Khám phá Dữ liệu giúp chúng ta có cái nhìn tổng quan về phân phối, các giá trị khuyết thiếu và cấu trúc tương quan giữa các biến trước khi tiến hành mô hình hóa."
    ]
}

def get_eda_code(df_name, suffix=""):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "\n",
            "# Cài đặt style\n",
            "sns.set_theme(style='whitegrid')\n",
            "\n",
            "# 1. Thông tin cơ bản\n",
            f"print('--- Thông tin cơ bản {df_name} ---')\n",
            f"{df_name}.info()\n",
            f"display({df_name}.describe())\n",
            "\n",
            "# 2. Trực quan hóa Ma trận Tương quan\n",
            f"numeric_cols = {df_name}.select_dtypes(include=['float64', 'int64']).columns\n",
            "if len(numeric_cols) > 1:\n",
            "    plt.figure(figsize=(10, 8))\n",
            f"    sns.heatmap({df_name}[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)\n",
            f"    plt.title('Ma trận Tương quan - {df_name}')\n",
            f"    plt.savefig('eda_correlation{suffix}.png', dpi=300, bbox_inches='tight')\n",
            "    plt.show()\n",
            "\n",
            "# 3. Trực quan hóa Phân phối của biến đầu tiên\n",
            "if len(numeric_cols) > 0:\n",
            "    plt.figure(figsize=(8, 5))\n",
            f"    sns.histplot({df_name}[numeric_cols[0]], kde=True, color='blue')\n",
            f"    plt.title(f'Phân phối của biến {{numeric_cols[0]}}')\n",
            f"    plt.savefig('eda_distribution{suffix}.png', dpi=300, bbox_inches='tight')\n",
            "    plt.show()\n"
        ]
    }

mapping = {
    "01_Chuong_1.ipynb": "df_case",
    "02_Chuong_2.ipynb": "df_raw",
    "04_Chuong_4.ipynb": "df",
    "05_Chuong_5.ipynb": "df",
    "06_Chuong_6.ipynb": "df_roi",
    "07_Chuong_7.ipynb": "df_credit",
    "08_Chuong_8.ipynb": "df_survey",
    "09_Chuong_9.ipynb": "df",
    "10_Chuong_10.ipynb": "df",
}

for nb_path in notebooks:
    filename = os.path.basename(nb_path)
    if filename not in mapping and filename != "03_Chuong_3.ipynb":
        continue
        
    with open(nb_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    cells = data.get("cells", [])
    new_cells = []
    injected = False
    
    if filename == "03_Chuong_3.ipynb":
        for cell in cells:
            new_cells.append(cell)
            if not injected and cell.get("cell_type") == "code":
                source_str = "".join(cell.get("source", []))
                if "y = 2 * X[:, 0]" in source_str:
                    new_cells.append(eda_markdown)
                    ch3_code = get_eda_code("df_temp", "_03")
                    ch3_code["source"].insert(0, "import pandas as pd\n")
                    ch3_code["source"].insert(1, "df_temp = pd.DataFrame({'X': X.flatten(), 'y': y.flatten()})\n")
                    new_cells.append(ch3_code)
                    injected = True
    else:
        df_name = mapping[filename]
        for cell in cells:
            new_cells.append(cell)
            if not injected and cell.get("cell_type") == "code":
                source_str = "".join(cell.get("source", []))
                if (f"{df_name} = pd.DataFrame" in source_str or 
                    f"{df_name} = pd.read_csv" in source_str or 
                    (f"{df_name}['" in source_str and "np.random" in source_str) or 
                    (f"{df_name} = pd.DataFrame({{" in source_str.replace('\n', ''))):
                    new_cells.append(eda_markdown)
                    new_cells.append(get_eda_code(df_name, suffix=f"_{filename[:2]}"))
                    injected = True
                    
    data["cells"] = new_cells
    
    if injected:
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1)
        print(f"Injected EDA into {filename}")
    else:
        print(f"Could not find injection point for {filename}")
