---
title: 208. 实现 Trie (前缀树)
date: 2019-08-29
tags: [算法, leetcode]
id: 1
---

## 题目


实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。


## 分析

前缀树
Trie
字典树

## 解答

```
public class Trie {
    private final int SIZE = 26;
    private Node root;

    private class Node {
        private boolean isStr;
        private int num;
        private Node[] child;

        public Node() {
            child = new Node[SIZE];
            isStr = false;
            num = 1;
        }
    }

    public Trie() {
        root = new Node();
    }

    public void insert(String word) {
        if (null == word || word.isEmpty()) {
            return;
        }
        Node pNode = this.root;
        for (int i = 0; i < word.length(); i++) {
            int index = word.charAt(i) - 'a';
            if (pNode.child[index] == null) {
                Node tmp = new Node();
                pNode.child[index] = tmp;
            } else {
                pNode.child[index].num++;
            }
            pNode = pNode.child[index];
        }
        pNode.isStr = true;
    }

    public boolean search(String word) {
        if (null == word || word.isEmpty()) {
            return false;
        }
        Node pNode = this.root;
        for (int i = 0; i < word.length(); i++) {
            int index = word.charAt(i) - 'a';
            if (pNode.child[index] == null || (word.length() - i == 1 && pNode.child[index].isStr == false)) {
                return false;
            }
            pNode = pNode.child[index];
        }
        return true;
    }

    public boolean startsWith(String prefix) {
        if (null == prefix || prefix.isEmpty()) {
            return false;
        }
        Node pNode = this.root;
        for (int i = 0; i < prefix.length(); i++) {
            int index = prefix.charAt(i) - 'a';
            if (pNode.child[index] == null) {
                return false;
            }
            pNode = pNode.child[index];
        }
        return true;
    }
}

```
