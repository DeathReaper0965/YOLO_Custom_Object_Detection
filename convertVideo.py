import cv2
import numpy as np

video = cv2.VideoCapture("cars.mp4")
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
codec = cv2.VideoWriter_fourcc(*'DIVX')
output = cv2.VideoWriter('cars_low_fps_x20.avi', codec, 60.0, size)

i = 0
rate = 3

while(video.isOpened()):
    ret, frame = video.read()

    if ret:
        if i%rate == 0:
            output.write(frame)
            i += 1
        else:
            i+=1

    else:
        break

video.release()
output.release()