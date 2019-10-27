#!/usr/bin/python
# coding: utf-8
"""
File: desensitization.py
Author: noogel <noogel@163.com>
Date: 2019-10-26 14:57
Description: 图像数据脱敏
"""
import os
from PIL import Image

TARGET_WIDTH = 1024
TARGET_DIR = "source/resource/img/"


def geometric_resize(size_tuple, target_width):
    """
    等比缩放
    :param size_tuple:
    :param target_width:
    :return:
    """
    source_width, source_height = size_tuple
    if source_width < target_width:
        return size_tuple
    return target_width, int(target_width / source_width * source_height)


def resize_and_desensitization(img_path):
    """缩放加基本脱敏"""
    if img_path.rsplit(".", 1)[-1] not in ("png", "jpg", "jpeg", "webp"):
        print("Error invalid img: {}".format(
            img_path
        ))
        return
    source_img = Image.open(img_path)
    source_size = source_img.size
    target_size = geometric_resize(source_size, TARGET_WIDTH)
    if (hasattr(source_img, "_getexif") and source_img._getexif()) or target_size[0] != source_size[0]:
        target_img = Image.new(source_img.mode, source_size)
        target_img.putdata(list(source_img.getdata()))
        source_img.resize(target_size)
        target_img.save(img_path)
        print("Success to desensitization img, size: {} -> {} path: {}".format(
            source_size, target_size, img_path
        ))


def run():
    """批量处理"""
    for root, dirs, files in os.walk(TARGET_DIR):
        for file_name in files:
            img_path = os.path.join(root, file_name)
            resize_and_desensitization(img_path)


def test():
    img_path = "source/resource/img/15552247425780.jpg"
    import pdb; pdb.set_trace()
    resize_and_desensitization(img_path)


if __name__ == "__main__":
    run()
