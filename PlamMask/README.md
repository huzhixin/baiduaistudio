# 飞桨常规赛：PALM眼底彩照视盘探测与分割-7月第2名方案

## 赛题介绍
本赛题原型为ISBI2019PALM眼科大赛。 近视已成为全球公共卫生负担。在近视患者中，约35%为高度近视。近视导致眼轴长度的延长，可能引起视网膜和脉络膜的病理改变。随着近视屈光度的增加，高度近视将发展为病理性近视，其特点是病理改变的形成:(1)后极，包括镶嵌型眼底、后葡萄肿、视网膜脉络膜变性等;(2)视盘，包括乳头旁萎缩、倾斜等;(3)近视性黄斑，包括漆裂、福氏斑、CNV等。病理性近视对患者造成不可逆的视力损害。因此，早期诊断和定期随访非常重要。

视网膜由黄斑向鼻侧约3mm处有一直径约1.5mm、境界清楚的淡红色圆盘状结构，称为视神经盘，简称视盘。视盘是眼底图像的一个重要特征，对其进行准确、快速地定位与分割对利用眼底图像进行疾病辅助诊断具有重要意义。

- $\color{red}{注意：本次比赛需要选手使用环境：飞桨PaddlePaddle 2.1.0版本}$

- $\color{red}{注意：AI Studio上运行需要使用32G内存的高级版，本地运行同样需要配置较大的内存空间。}$

### [点击跳转至赛题页面](https://aistudio.baidu.com/aistudio/competition/detail/87)

### [AIStusio项目代码](https://aistudio.baidu.com/aistudio/projectdetail/2250547)

### [赛题数据集](https://aistudio.baidu.com/aistudio/datasetdetail/101358)

### [PaddleSeg包](https://aistudio.baidu.com/aistudio/datasetdetail/102868)

## 解题思路
本文通过PaddleSeg的配置方式使用UNet模型完成该任务。
PaddleSeg是基于飞桨PaddlePaddle开发的端到端图像分割开发套件，涵盖了高精度和轻量级等不同方向的大量高质量分割模型。通过模块化的设计，提供了配置化驱动和API调用两种应用方式，帮助开发者更便捷地完成从训练到部署的全流程图像分割应用。
![](https://ai-studio-static-online.cdn.bcebos.com/e9d5ad1086a045828a04be3e93148bb918e38ff2405743dd89d4b7e5e6ff05d0)

图1 UNet结构图（图片来源：https://github.com/PaddlePaddle/PaddleSeg/blob/release/2.2/docs/models/unet.md）


### 配置项 [官方文档](https://github.com/PaddlePaddle/PaddleSeg/blob/release/2.2/docs/design/use/use_cn.md)
- $\color{red}{注意：本文使用自定义数据集，配置文件中train_dataset和val_dataset的属性 type: Dataset。}$
----
### train_dataset
* 训练数据集
----
### val_dataset
* 验证数据集

----
### batch_size
* 单张卡上，每步迭代训练时的数据量。一般来说，你所使用机器的显存越大，可以相应的调高batch_size的值。

----
### iters
* 使用一个 batch 数据对语义分割模型进行一次参数更新的过程称之为一次训练，即一次迭代。iters 即为训练过程中的迭代次数。

----
### optimizer
* 训练优化器

----
### lr_scheduler
* 学习率

----
### loss
* 损失函数

----
### model
* 待训练模型
---
### export
* 模型导出配置