import os
import random

# 原始图片列表
original_images = []

# 遍历文件夹获取所有的原始图片
for _,_, f in os.walk("/home/aistudio/dataset/images"):
    if len(f) > 0:
        for fi in f:
            original_images.append(fi)


# 标记图片
label_images = []

# 遍历文件夹获取所有的原始图片
for _,_, f in os.walk("/home/aistudio/dataset/labels"):
    if len(f) > 0:
        for fi in f:
            label_images.append(fi)

# 测试图片列表
test_images = []

# 遍历文件夹获取所有的原始图片
for _,_, f in os.walk("/home/aistudio/dataset/test"):
    if len(f) > 0:
        for fi in f:
            test_images.append(fi)

# 划分训练集和验证集
val_rate = 0.2

# 随机数种子
random.seed()

# 提取验证集
val_list = random.sample(original_images, int(len(original_images)*val_rate))

# 提取训练集
train_list = []
for file_name in original_images:
    if file_name not in val_list:
        train_list.append(file_name)

# 生成训练集文件列表文件
with open("/home/aistudio/dataset/train_list.txt", "w") as f:
    for train_file in train_list:
        for label_file in label_images:
            if train_file[:-4] == label_file[:-4]:
                f.write("images/"+train_file + " " + "labels/"+label_file+"\n")
f.close()

# 生成验证集文件列表文件
with open("/home/aistudio/dataset/val_list.txt", "w") as f:
    for val_file in val_list:
        for label_file in label_images:
            if val_file[:-4] == label_file[:-4]:
                f.write("images/"+val_file + " " + "labels/"+label_file+"\n")
f.close()

# 生成测试集文件列表文件
with open("/home/aistudio/dataset/test_list.txt", "w") as f:
    for test_file in test_images:
        f.write("test/"+test_file+"\n")
f.close()
