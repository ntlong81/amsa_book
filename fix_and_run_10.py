import json
import os
import subprocess
import shutil
import glob

path = r'd:\CODE\amsa_book\chapters\10_Chuong_10.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for cell in data.get('cells', []):
    if cell.get('cell_type') == 'code':
        if 'outputs' not in cell:
            cell['outputs'] = []

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=1)

print("Fixed notebook structure for chapter 10.")
try:
    subprocess.run([
        "jupyter", "nbconvert", "--to", "notebook", 
        "--execute", "--inplace", "--allow-errors",
        "--ExecutePreprocessor.timeout=-1", path
    ], check=True)
    print("Successfully executed chapter 10.")
except subprocess.CalledProcessError as e:
    print(f"Error executing chapter 10: {e}")

# move images
chapters_dir = r"d:\CODE\amsa_book\chapters"
images_dir = os.path.join(chapters_dir, "images")
os.makedirs(images_dir, exist_ok=True)
image_exts = ["*.png", "*.jpg", "*.jpeg", "*.svg"]

for ext in image_exts:
    for img_path in glob.glob(os.path.join(chapters_dir, ext)):
        img_name = os.path.basename(img_path)
        dest_path = os.path.join(images_dir, img_name)
        if os.path.exists(dest_path):
            os.remove(dest_path)
        shutil.move(img_path, dest_path)
        print(f"Moved {img_name} to images/")
print("Done with chapter 10.")
