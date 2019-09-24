'''
快速排序
version:0.1
author:小雨
date:2019.09.22
'''
import sys

class Node(object):
    def __init__(self,value = None, next = None):
        self.value =value
        self.next =next


class LingkedList(object):
    def __init__(self,maxsize = None):
        self.root =Node()
        self.maxsize = maxsize
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def sppend(self,value):
        node = Node(value)
        if len(self) > self.maxsize and self.maxsize is not None:
            raise Exception('full')
        if self.tailnode is None:
            self.root.next = node
        else:
            self.tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendLeft(self,value):
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        yield curnode

    def iter(self):
        for node in self.iter_node():
            yield node.value

    def remove(self,value): #O(n)
        prevnode = self.root
        curnode = self.root.next
        while curnode is not None:
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailnode:
                    self.tailnode = prevnode
                del curnode
                self.length -= 1
                return

    def find(self, value):
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def popLeft(self):
        if self.root.next is None:
            raise Exception('empty')
        headnode = self.root.next
        self.root.next = headnode.next
        value = headnode.value
        del headnode
        self.length -= 1
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0

