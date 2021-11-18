#coding: utf8

# 单向链表实现
# 参考网址：https://zhuanlan.zhihu.com/p/60057180

from link_node import Node


class LinkList(object):
    """实现单向链表及常用操作"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """返回链表是否为空"""

        return self.head is None

    def length(self):
        """返回链表长度"""

        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next_
        return count

    def iter_items(self):
        """遍历链表节点，返回生成器"""

        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next_

    def add(self, item):
        """向链表头部增加节点"""

        n = Node(item)
        if self.head is None:
            self.head = n
        else:
            n.next_ = self.head
            self.head = n

    def append(self, item):
        """向链表尾部追加节点"""

        n = Node(item)
        if self.head is None:
            self.head = n
        else:
            cur = self.head
            while True:
                if cur.next_ is None:
                    cur.next_ = n
                    break
                cur = cur.next_

    def insert(self, index, item):
        """插入链表节点

        如何理解插入点？是否类似于列表插入：Insert object before index ?
        注意：当前实现方式类似于列表 insert() 方法: Insert object before index.
        
        Args:
            index: 插入点位置
            item: 需要插入的元素

        """

        # 如果插入点在链表最左侧，在头部加入节点
        if index <= 1:
            self.add(item)
        # 如果插入点在链表最右侧，在尾部加入节点
        elif index > self.length():
            self.append(item)
        # 插入点 2, 不可以走遍历方式，直接修改第一个节点的next_（即 self.head 指针）
        # 因为self.head已经是第一个节点
        elif index == 2:
            n = Node(item)
            cur = self.head
            n.next_ = cur.next_
            cur.next_ = n
        # 插入点 >=3, 进行遍历，遍历次数index-2
        else:
            n = Node(item)
            cur = self.head
            # 因为 cur 当前已经指向第一个节点，index-1 是因为需要找到插入点的上一个节点
            for _ in range(1, index-1):
                cur = cur.next_
            n.next_ = cur.next_
            cur.next_ = n

    def remove(self, item):
        """删除链表节点"""

        # 当前节点
        cur = self.head
        # 上一个节点
        pre = None
        while cur is not None:
            # 命中第一个节点
            if cur.value == item:
                if not pre:
                    # 链表头指向第一个节点后的节点
                    self.head = cur.next_
                else:
                    pre.next_ = cur.next_
                return True
            else:
                # 记录上一个节点
                pre = cur
                # 当前节点后移
                cur = cur.next_

if __name__ == "__main__":
    n1 = Node(11)
    n2 = Node(22)
    n3 = Node(33)
    n4 = Node(44)
    n1.next_ = n2
    n2.next_ = n3
    n3.next_ = n4
    l_list = LinkList()
    l_list.head = n1
    print(l_list.length())
    l_list.insert(1, 55)
    l_list.append(66)
    print(l_list.length())
    for i in l_list.iter_items():
        print(i)
