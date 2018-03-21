import cv2
import numpy as np
import os
from darkflow.net.build import TFNet
import time

options = {"model": "cfg/tiny-yolo-voc-1c.cfg", "load": "bin/yolo.weights", "gpu": 1.0, "threshold": 0.1}
tfnet = TFNet(options)

video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 720)

colors = [tuple(np.random.rand(3)*255) for _ in range(100)]

while True:
    start_time = time.time()
    ret, frame = video.read()
    returns = tfnet.return_predict(frame)

    if ret:
        for c, r in zip(colors, returns):
            tl = (r["topleft"]["x"], r["topleft"]["y"])
            br = (r["bottomright"]["x"], r["bottomright"]["y"])
            label = "{}: {:.0f}%".format(r["label"], r["confidence"]*100)
            frame = cv2.rectangle(frame, tl, br, c, 4)
            frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, c, 2)

        cv2.imshow("frame", frame)
        print("FPS {:.1f}".format(1/(time.time()-start_time)))

    else:
        video.release()
        break

