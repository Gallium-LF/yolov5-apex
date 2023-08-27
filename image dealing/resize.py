import cv2
import os
path = "D:/image/before/" # 源文件夹路径
new_path = "D:/image/resize/" # 目标文件夹路径
new_size = (400,514) # 新的图像大小

for file_name in os.listdir(path):
    if file_name.endswith(".png"): # 只处理png格式的图像
        img = cv2.imread(path + file_name, cv2.IMREAD_UNCHANGED) # 打开图像，保持透明度
        img = cv2.resize(img, new_size,interpolation = cv2.INTER_AREA) # 调整大小
        cv2.imwrite(new_path + file_name, img) # 保存到目标文件夹