import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET


def create_xml(dir, img_name, objects, tl, br, savedir):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    image = cv2.imread(img_name.path)
    height, width, depth = image.shape

    annotation = ET.Element("annotation")
    ET.SubElement(annotation, "folder").text = dir
    ET.SubElement(annotation, "filename").text = img_name.name
    ET.SubElement(annotation, "segmented").text = "0"

    size = ET.SubElement(annotation, "size")
    ET.SubElement(size, "width").text = str(width)
    ET.SubElement(size, "height").text = str(height)
    ET.SubElement(size, "depth").text = str(depth)

    for obj, obj_tl, obj_br in zip(objects, tl, br):
        object = ET.SubElement(annotation, "object")
        ET.SubElement(object, "name").text = obj
        ET.SubElement(object, "pose").text = "Unspecified"
        ET.SubElement(object, "truncated").text = "0"
        ET.SubElement(object, "difficult").text = "0"
        bndbox = ET.SubElement(object, "bndbox")
        ET.SubElement(bndbox, "xmin").text = str(obj_tl[0])
        ET.SubElement(bndbox, "ymin").text = str(obj_tl[1])
        ET.SubElement(bndbox, "xmax").text = str(obj_br[0])
        ET.SubElement(bndbox, "xmin").text = str(obj_br[1])

    xml_string = ET.tostring(annotation)
    root = etree.fromstring(xml_string)
    xml_string = etree.tostring(root, pretty_print=True)

    save_path = os.path.join(savedir, img_name.name.replace("png", "xml"))

    with open(save_path, "wb") as temp_file:
        temp_file.write(xml_string)


if __name__ == "__main__":
    dir = "combined_images"
    img_name = [img for img in os.scandir(dir) if "000001" in img.name][0]
    objects = ["technotip pen"]
    tl = [(20, 30)]
    br = [(100, 10)]
    savedir = "annotations"
    create_xml(dir, img_name, objects, tl, br, savedir)
