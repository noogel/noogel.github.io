#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
@author: 'noogel'
@date: '2017-11-23'
@desc: config blog
"""
__author__ = 'noogel'

import os
import sys
import time
import yaml
import json
import logging
import datetime
import subprocess
import webbrowser

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s  @ %(message)s',
)

# BASE CONSTANT
HEXO_PORT = 1236
NOTEBOOK_PORT = 1235
NOTEBOOK_WORK_PATH = "notebook"
CHAPTER_SOURCE_PATH = "source/_posts"
IMAGE_SOURCE_PATH = "source/resource/img"
# START CONSTANT
IPYTHON_START_CMD = [
    'jupyter', 'notebook', '--notebook-dir={}'.format(NOTEBOOK_WORK_PATH),
    '--port={}'.format(NOTEBOOK_PORT)]

HEXO_START_CMD = ['hexo', 'server', '-g', '-p', str(HEXO_PORT)]
HEXO_GEN_CMD = "hexo generate"
HEXO_PUB_CMD = "hexo d -g && git add --all && git commit -am 'auto commit' && git push origin sources"
HEXO_START_URL = "http://localhost:{}".format(HEXO_PORT)
# BUILD CONSTANT
NPM_BUILD_CMD = (
    "npm install --registry=https://registry.npm.taobao.org",
    "pip install notebook==5.2.1")
# STACK CONFIG
CHAPTERS_DB = "db.json"
CHAPTERS_SUB_PATH = "_posts/"
BLOG_CONFIG = "_config.yml"
STACK_INDEX = "source/stack/index.md"


def blog():
    """start blog"""
    gen_stack()
    pro1 = subprocess.Popen(IPYTHON_START_CMD)
    pro2 = subprocess.Popen(HEXO_START_CMD)
    try:
        time.sleep(3)
        webbrowser.open_new_tab(HEXO_START_URL)
        pro1.wait()
        pro2.wait()
    except KeyboardInterrupt:
        pro1.kill()
        pro2.kill()


def gen_stack():
    """gen stack"""
    logging.info("Start generating db.json!")
    os.system(HEXO_GEN_CMD)
    logging.info("Start build stack!")
    with open(BLOG_CONFIG) as conf:
        path_config = yaml.load(conf)["pypermalink"]
    with open(CHAPTERS_DB) as chapters:
        chapters = json.loads("".join(chapters.readlines()))["models"]["Post"]

    extract_chapters, sorted_chapters, paths = [], [], set()
    for chapter in chapters:
        split_source = chapter["source"].replace(CHAPTERS_SUB_PATH, "").rsplit("/", 1)
        build_path = split_source[0] if len(split_source) > 1 else ""
        page_date = datetime.datetime.strptime(chapter["date"], "%Y-%m-%dT%H:%M:%S.%fZ") + datetime.timedelta(hours=8)
        node = {
            "title": chapter["title"],
            "deep": len(build_path.split("/")),
            "path": build_path,
            "page_path": "/{}".format(path_config.format(
                year=page_date.year, month=str(page_date.month).zfill(2), day=str(page_date.day).zfill(2),
                id=chapter["id"], _id=chapter["_id"]))
        }
        extract_chapters.append(node)

    for node in sorted(extract_chapters, key=lambda val: val["path"]):
        if node["path"] and node["path"] not in paths:
            sorted_chapters.append("\n{}* {} {}".format(" " * 4 * (node["deep"] - 1),
                                                        "#" * (
                                                            node["deep"] + 1 if node["path"] and node[
                                                                                                     "deep"] < 5 else 0),
                                                        node["path"].split("/")[-1].encode("utf-8")))
            paths.add(node["path"])
        sorted_chapters.append("{}* [{}]({})".format(" " * 4 * (node["deep"] if node["path"] else 0),
                                                     node["title"].encode("utf-8"),
                                                     node["page_path"]))

    head = """---
date: 2017-01-24 12:09:47
type: "stack"
---

{}
""".format("\n".join(sorted_chapters))

    with open(STACK_INDEX, "w") as wf:
        wf.write(head)

    logging.info("Rewrite stack/index.md ok!")


def push():
    gen_stack()
    os.system(HEXO_PUB_CMD)
    logging.info("Publish file ok!")


if __name__ == "__main__":
    op = sys.argv[-1]
    op_map = {
        "blog": blog,
        "stack": gen_stack,
        "push": push,
    }
    op_map[op]()
