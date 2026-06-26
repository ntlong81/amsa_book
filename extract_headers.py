import json
import glob
import os

chapters_dir = r"d:\CODE\amsa_book\chapters"
notebooks = sorted(glob.glob(os.path.join(chapters_dir, "*.ipynb")))

with open(r"d:\CODE\amsa_book\headers.txt", "w", encoding="utf-8") as out:
    for nb_path in notebooks:
        if "Tai_Lieu_Tham_Khao" in nb_path:
            continue
        out.write(f"\n--- {os.path.basename(nb_path)} ---\n")
        try:
            with open(nb_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                
            for cell in data.get("cells", []):
                if cell.get("cell_type") == "markdown":
                    source = cell.get("source", [])
                    if isinstance(source, list):
                        text = "".join(source)
                    else:
                        text = source
                    
                    for line in text.split('\n'):
                        if line.strip().startswith('#'):
                            out.write(line.strip() + "\n")
        except Exception as e:
            out.write(f"Error: {e}\n")
