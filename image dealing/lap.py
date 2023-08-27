import cv2
import numpy as np
import os
input_dir = 'D:/image/resize/' # 存放灰度图的文件夹
output_dir = 'D:/image/resize/' # 存放滤波结果的文件夹
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) # 定义3x3的拉普拉斯模板
for filename in os.listdir(input_dir): # 遍历输入文件夹下的所有文件名
    print(filename) # 打印文件名
    img = cv2.imread(input_dir + filename, 0) # 读取灰度图
    dst = cv2.filter2D(img, -1, kernel) # 对图像进行拉普拉斯滤波
    cv2.imwrite(output_dir + filename, dst) # 保存滤波结果到输出文件夹