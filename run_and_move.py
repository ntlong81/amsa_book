import os
import glob
import subprocess
import shutil

chapters_dir = r"d:\CODE\amsa_book\chapters"
images_dir = os.path.join(chapters_dir, "images")

os.makedirs(images_dir, exist_ok=True)

notebooks = sorted(glob.glob(os.path.join(chapters_dir, "*.ipynb")))

for nb in notebooks:
    print(f"Executing {os.path.basename(nb)}...")
    try:
        subprocess.run([
            "jupyter", "nbconvert", 
            "--to", "notebook", 
            "--execute", 
            "--inplace", 
            "--allow-errors",
            "--ExecutePreprocessor.timeout=-1",
            nb
        ], check=True)
        print(f"Finished {os.path.basename(nb)}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute {os.path.basename(nb)}: {e}")

# Move all images
image_exts = ["*.png", "*.jpg", "*.jpeg", "*.svg"]
for ext in image_exts:
    for img_path in glob.glob(os.path.join(chapters_dir, ext)):
        img_name = os.path.basename(img_path)
        dest_path = os.path.join(images_dir, img_name)
        # overwrite if exists
        if os.path.exists(dest_path):
            os.remove(dest_path)
        shutil.move(img_path, dest_path)
        print(f"Moved {img_name} to images/")
print("Execution and moving completed.")
