import PIL.Image as Image
from tqdm import tqdm
import numpy as np
import os

file_path = "/home/aistudio/dataset/labels"
for _,_, files in os.walk(file_path):
    for f in tqdm(files):
        img_path = os.path.join(file_path, f)
        img = Image.open(img_path)
        img = np.asanyarray(img).copy()
        img[img == 255] = 1
        img = Image.fromarray(img)
        img.save(img_path)