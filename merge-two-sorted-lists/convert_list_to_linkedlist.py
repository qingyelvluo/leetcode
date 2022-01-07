#coding: utf8


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def convert_list_to_linked.py(list_):
    """列表转换链表，返回head（实例对象）"""

    if len(list_) == 0:
        return []
    head = ListNode(list_[0]) 
    if len(list_) == 1:
        return head
    p = head
    for i in range(1, len(list_)):
        p.next = ListNode(list_[i])
        p = p.next
        return head

if __name__ == "__main__":
    a = []
    b = [1]
    c = [1,2,4]
    d = [1,2,3,4,5,5,5,5,5,5,6]
    l1 = convert_list_to_linked.py(a)
    l2 = convert_list_to_linked.py(b)
    l3 = convert_list_to_linked.py(c)
    l4 = convert_list_to_linked.py(d)
    print(l1)
    print(l2.val)
    print(l2.next)
    print(l3.val)
    print(l3.next)
    print(l3.next.val)
