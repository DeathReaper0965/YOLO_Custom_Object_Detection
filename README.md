# YOLO for Custom Object Detection

This repo contains the code that can be used to detect "a ballpoint or a gel pen" that is placed in front of the webcam.
The `generate_annotations.py` file calls a function `create_xml()` of `generate_xml.py` file which generates a "xml" file that is in-turn used for generating the annotations of objects(which in our case "pens"). You can even use this repo's scripts to train your own model to detect any custom object.

## How to use your own images to train the model for detecting custom objects

First clone the darkflow repo(https://github.com/thtrieu/darkflow) and add the files of this repo inside the darkflow repo as we need the yolo model for the detection, also add `tiny-yolo-voc-1c.cfg` file of this repo to darkflow repo's "cfg/" folder.

Now, you can use `imageWebScrapper.py` file to download and save images into your local system by just entering the search term, for each search-term an individual forlder gets created. Once you download all the required images to their respective folders, you need to change the `images_dir` value and "folder names to take images from" in `images_concatenation.py` file. Now, change the value of `img_dir` value in `generate_annotations.py` file to the one you specified above and also change the `savedir`, `anno_dir`, `obj` values to something you like/something on which you are training on.

That is everything, now all you have to do is run the `generate_annnotations.py` file and create some annotations (just by clicking and dragging on the images) as these will be used to train our custom yolo model. After creating annotations, run the command `python flow --model cfg/tiny-yolo-voc-1c.cfg --load bin/tiny-yolo-voc.weights --train --annotation <your_annotations-folder-name> --dataset <your_images_dataset_folder_name> --gpu 1.0 --epoch 250`

This will start the training process, once the process completes the weights will be updated and you can now change the "load" value inside `yolo_detection.py` file to the no. of checkpoints created(Note: you can check them in "ckpt/" directory), also add your object name to `labels.txt` file and run `yolo_detection.py`. By, running the file you can see a webcam window popped up, all that is left is to keep your trained object in front of the webcam and "boom!!" you can see the object along with its confidence score gets detected.

PS, training the model takes lot of computational power, so train it on some external GPU or cloud.
