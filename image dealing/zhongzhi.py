import cv2
import numpy as np
import os
input_dir = 'D:/image/resize/' # 存放灰度图的文件夹
output_dir = 'D:/image/resize/' # 存放滤波结果的文件夹
ksize = (5, 5) # 定义模板的大小，必须是元组
for filename in os.listdir(input_dir): # 遍历输入文件夹下的所有文件名
    print(filename) # 打印文件名
    img = cv2.imread(input_dir + filename, 0) # 读取灰度图
    dst = cv2.blur(img, ksize) # 对图像进行均值滤波
    cv2.imwrite(output_dir + filename, dst) # 保存滤波结果到输出文件夹