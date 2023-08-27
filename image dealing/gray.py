import os
import cv2
import numpy as np
def read_path(file_pathname):
    new_size = (512,512)
    for filename in os.listdir(file_pathname): # 返回这一路径下的所有文件名，得到的是一个列表
        img = cv2.imread(file_pathname+'/'+filename, 1) # 在前面要加上文件夹的路径，1是将图片按照彩色图来读
        img = cv2.resize(img, new_size,interpolation = cv2.INTER_AREA)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 彩色图转灰度图
        cv2.imwrite('D:/image/resize/' + filename, gray_img) # 保存灰度图；此处如果不改文件名，会覆盖原先的文件
read_path("D:/image/before/") # 图片目录