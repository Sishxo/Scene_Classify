import cv2
import os
import numpy as np


def rotate(image, angle):
    height, width, channel = image.shape
    center = (width/2, height/2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    nW = int((height*sin)+(width*cos))
    nH = int((height*cos)+(width*sin))

    M[0, 2] += (nW / 2) - width/2
    M[1, 2] += (nH / 2) - height/2
    img = cv2.warpAffine(image, M, (nW, nH))
    return img


def getFrameInVideo(readPath, savePath, interval):
    video_list = os.listdir(readPath)
    i = 0
    j = 141

    for path, dir_list, file_list in os.walk(readPath):
        # print(file_list)
        for video_name in file_list:
            k = 0
            print(video_name)
            path = os.path.join(readPath, video_name)
            cap = cv2.VideoCapture(path)
            image_num = int(round(cap.get(cv2.CAP_PROP_FRAME_COUNT)/interval))
            # print(fps)
            while True:
                ret, frame = cap.read()
                if ret != 1:
                    print(video_name+" done.")
                    break
                height, width, channel = frame.shape
                # center=(width/2,height/2)
                # print(frame.shape)
                if(width > 1080):
                    frame = rotate(frame, -90)
                i += 1
                if(i % interval == 0):
                    save_name = 'clear_no_'+str(j)+'.jpg'
                    j += 1
                    k += 1
                    save_path = os.path.join(savePath, save_name)
                    cv2.imwrite(save_path, frame)
                    print('GET PROCESS:  '+str(k)+" / "+str(image_num))


if __name__ == "__main__":
    readPath = "/home/sishxo/project/scene/清洁卫生不合格"
    if not os.path.exists(readPath):
        os.makedirs(readPath)
    savePath = "/home/sishxo/project/scene/clear_no_image"
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    getFrameInVideo(readPath, savePath, 10)
