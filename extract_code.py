import json
import glob
import os

chapters_dir = r"d:\CODE\amsa_book\chapters"
notebooks = sorted(glob.glob(os.path.join(chapters_dir, "*.ipynb")))

with open(r"d:\CODE\amsa_book\code_extract.txt", "w", encoding="utf-8") as out:
    for nb_path in notebooks:
        if "Tai_Lieu_Tham_Khao" in nb_path:
            continue
        out.write(f"\n--- {os.path.basename(nb_path)} ---\n")
        try:
            with open(nb_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                
            code_lines = []
            for cell in data.get("cells", []):
                if cell.get("cell_type") == "code":
                    source = cell.get("source", [])
                    if isinstance(source, list):
                        code_lines.extend(source)
                    else:
                        code_lines.extend(source.split('\n'))
            
            # Print lines containing 'import', 'read_', 'pd.', 'np.', 'DataFrame'
            for i, line in enumerate(code_lines):
                if any(x in line for x in ['import pandas', 'read_', 'np.random', 'DataFrame']):
                    out.write(f"{line.strip()}\n")
        except Exception as e:
            out.write(f"Error: {e}\n")
