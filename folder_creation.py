import os
import shutil

folder_path = 'D:\\newfolder'
os.makedirs(folder_path, exist_ok=True)
shutil.copy2('image.png', os.path.join(folder_path, 'image.png'))