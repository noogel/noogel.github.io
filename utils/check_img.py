#!/usr/bin/python
# coding: utf-8
"""
File: check_img.py
Author: noogel <noogel@163.com>
Date: 2020-05-15
Description: 检查图片
"""
import os
import re

POST_PATH = "source/"
POST_IMG_PATH = "source/resource/img"
FILTER_IMG_EXT = [".jpg", ".png", ".jpeg", ".gif"]

PATTEN = re.compile(r"!\[[\s\S]*?\]\(([\s\S]*?[.png|.jpg|.jpeg|.gif]+?)[\s]*?\)")


def get_post_img_file():
    collect_list = []
    for path, _, file_names in os.walk(POST_IMG_PATH):
        for file_name in file_names:
            if any([file_name.lower().endswith(val) for val in FILTER_IMG_EXT]):
                collect_list.append("{}/{}".format(path, file_name))
    return collect_list

def get_post_img_use():
    md_list = []
    collect_list = []

    for path, _, file_names in os.walk(POST_PATH):
        for file_name in file_names:
            if file_name.lower().endswith(".md"):
                md_list.append("{}/{}".format(path, file_name))
    for item in md_list:

        with open(item, "r") as rf:
            content = rf.readlines()
            for tt in content:
                res = PATTEN.search(tt)
                if res and res.group(1):
                    collect_list.append("source" + res.group(1))
    return collect_list

if __name__ == "__main__":
    res = list(set(get_post_img_file()) - set(get_post_img_use()))
    for item in res:
        os.remove(item)
        print(item)
