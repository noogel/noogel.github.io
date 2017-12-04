#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
@author: 'noogel'
@date: '2017-12-05'
@desc: gen stack
"""

import yaml
import json
import datetime

CHAPTERS_DB = "db.json"
CHAPTERS_SUB_PATH = "_posts/"
BLOG_CONFIG = "_config.yml"
STACK_INDEX = "source/stack/index.md"

with open(BLOG_CONFIG) as conf:
    PATH_CONFIG = yaml.load(conf)["pypermalink"]
with open(CHAPTERS_DB) as chapters:
    CHAPTERS = json.loads("".join(chapters.readlines()))["models"]["Post"]

EXTRACT_CHAPTERS, SORTED_CHAPTERS, PATHS = [], [], set()
for chapter in CHAPTERS:
    split_source = chapter["source"].replace(CHAPTERS_SUB_PATH, "").rsplit("/", 1)
    build_path = split_source[0] if len(split_source) > 1 else ""
    page_date = datetime.datetime.strptime(chapter["date"], "%Y-%m-%dT%H:%M:%S.%fZ") + datetime.timedelta(hours=8)
    node = {
        "title": chapter["title"],
        "deep": len(build_path.split("/")),
        "path": build_path,
        "page_path": "/{}".format(PATH_CONFIG.format(
            year=page_date.year, month=str(page_date.month).zfill(2), day=str(page_date.day).zfill(2),
            id=chapter["id"], _id=chapter["_id"]))
    }
    EXTRACT_CHAPTERS.append(node)

for node in sorted(EXTRACT_CHAPTERS, key=lambda val: val["path"]):
    if node["path"] and node["path"] not in PATHS:
        SORTED_CHAPTERS.append("\n{}* {} {}".format(" " * 4 * (node["deep"] - 1),
                                                    "#" * (
                                                    node["deep"] + 1 if node["path"] and node["deep"] < 5 else 0),
                                                    node["path"].split("/")[-1].encode("utf-8")))
        PATHS.add(node["path"])
    SORTED_CHAPTERS.append("{}* [{}]({})".format(" " * 4 * (node["deep"] if node["path"] else 0),
                                                 node["title"].encode("utf-8"),
                                                 node["page_path"]))

HEAD = """---
date: 2017-01-24 12:09:47
type: "stack"
---

{}
""".format("\n".join(SORTED_CHAPTERS))

with open(STACK_INDEX, "w") as wf:
    wf.write(HEAD)

print "ok!"
