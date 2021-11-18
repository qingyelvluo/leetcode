#coding: utf8


class Node(object):
    """单向链表节点"""

    def __init__(self, value):
        self.value = value
        self.next_ = None
