import torch
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import ImageGrab
import time
import pyautogui


# 加载本地yolov5模型，路径自己调
model = torch.hub.load('D:\\OneDrive - mail2.sysu.edu.cn\\class\\DIP\\yolov5', 'custom',
                       path='D:\\OneDrive - mail2.sysu.edu.cn\\class\\DIP\\yolov5\\runs\\train\\exp3\\weights\\best.pt', source='local', device='0')
# 不设置这个可能会报agg错误
matplotlib.use('TkAgg')

while True:
    # 截图桌面图片
    image_array = np.array(ImageGrab.grab())
    # 获取框框的坐标
    bboxes = np.array(model(image_array[:, :, ::-1]).xyxy[0].cpu())

    for bbox in bboxes:
        conf = bbox[4]
        classID = int(bbox[5])
        # 判断是否为0，如果为0则是人，进入循环把人干掉，然后退出循环，寻找下一位
        if classID == 0:
            x0, y0, x1, y1 = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
            # 移动鼠标
            pyautogui.moveTo(x0+(x1-x0)/2.0, y0+(y1-y0)/2.0)
            time.sleep(1)
            break

    if 0xFF == ord('7'):
        break

