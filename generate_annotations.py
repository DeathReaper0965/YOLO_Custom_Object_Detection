import os
from matplotlib.widgets import RectangleSelector
import numpy as np
import matplotlib.pyplot as plt
import cv2
from generate_xml import create_xml

img_dir = "combined_images"
anno_dir = "annotations"
obj = "technotip pen"
savedir = "annotations"

tl_list = []
br_list = []
img = None
obj_list = []

def rec_select_callback(click, rls):
    global tl_list
    global br_list
    global obj_list
    global obj

    obj_list.append(obj)
    tl_list.append((int(click.xdata), int(click.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))

def toggle_selector(event):
    toggle_selector.RS.set_active(True)

def onkeypress(event):
    global tl_list
    global br_list
    global img
    global obj_list

    if event.key == "q":
        create_xml(img_dir, img, obj_list, tl_list, br_list, savedir)
        tl_list = []
        br_list = []
        obj_list = []
        img = None
        plt.close()

if __name__ == "__main__":

    for i, img_file in enumerate(os.scandir(img_dir)):
        img = img_file
        fig, ax = plt.subplots(1)
        image = cv2.imread(img_file.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)
        toggle_selector.RS = RectangleSelector(
            ax, rec_select_callback,
            drawtype="box", minspanx=5,
            minspany=5, useblit=True, spancoords="pixels",
            button=[1], interactive=True
        )
        bound_box = plt.connect("key_press_event", toggle_selector)
        key_press = plt.connect("key_press_event", onkeypress)

        plt.show()