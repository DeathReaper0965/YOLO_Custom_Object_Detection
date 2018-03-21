import os

images_dir = "combined_images"

if not os.path.isdir(images_dir):
    os.mkdir(images_dir)

techno_folders = [folder for folder in os.listdir(".") if "techno" in folder]

i = 0
for folder in techno_folders:
    for img in os.scandir(folder):
        os.rename(img, os.path.join(images_dir, "{:06}.png".format(i)))
        i+=1