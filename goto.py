#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
@author: 'noogel'
@date: '2017-11-23'
@desc: config blog
"""
__author__ = 'noogel'

import sys
import time
import subprocess
import webbrowser

# BASE CONSTANT
HEXO_PORT = 1236
NOTEBOOK_PORT = 1235
NOTEBOOK_WORK_PATH = "notebook"
CHAPTER_SOURCE_PATH = "source/_posts"
IMAGE_SOURCE_PATH = "source/resource/img"
# START CONSTANT
IPYTHON_START_CMD = [
    'jupyter', 'notebook', '--no-browser', '--notebook-dir={}'.format(NOTEBOOK_WORK_PATH), '--port={}'.format(NOTEBOOK_PORT)]
HEXO_START_CMD = ['hexo', 'server', '-g', '-p', str(HEXO_PORT)]
HEXO_START_URL = "http://localhost:{}".format(HEXO_PORT)
# BUILD CONSTANT
NPM_BUILD_CMD = (
    "npm install --registry=https://registry.npm.taobao.org",
    "pip install notebook==5.2.1")


def blog():
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


if __name__ == "__main__":
    op = sys.argv[-1]
    op_map = {
        "blog": blog
    }
    op_map[op]()
