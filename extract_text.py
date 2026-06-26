import json
import glob
import os

chapters_dir = r"d:\CODE\amsa_book\chapters"
notebooks = sorted(glob.glob(os.path.join(chapters_dir, "*.ipynb")))

output_file = r"d:\CODE\amsa_book\all_text.txt"

with open(output_file, "w", encoding="utf-8") as out:
    for nb_path in notebooks:
        if "Tai_Lieu_Tham_Khao" in nb_path:
            continue
        out.write(f"\n\n{'='*50}\n")
        out.write(f"FILE: {os.path.basename(nb_path)}\n")
        out.write(f"{'='*50}\n\n")
        
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
                    out.write(text + "\n\n")
        except Exception as e:
            out.write(f"Error reading {nb_path}: {e}\n")

print("Extraction complete.")
