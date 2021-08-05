import PIL.Image as Image
from tqdm import tqdm
import numpy as np
import os

file_path = "/home/aistudio/PaddleSeg/output/result/pseudo_color_prediction"
for _,_, files in os.walk(file_path):
    for f in tqdm(files):
        img_path = os.path.join(file_path, f)
        img = Image.open(img_path)
        img = np.asanyarray(img).copy()
        img[img == 0] = 255
        img[img == 1] = 0
        img = Image.fromarray(img)
        img.save(img_path)
