# Definition for singly-linked list.

# 说明：通过模拟链表在本地运行失败
# 可能原因：
# 1、列表转换链表程序有问题
# 2、合并链表代码有问题


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def convert_list_to_linked(list_):
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


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)
        node = res
        while l1 and l2:
            if l1.val<l2.val:
                node.next,l1 = l1,l1.next
            else:
                node.next,l2 = l2,l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next  


if __name__ == "__main__":
    l1 = [1,2,4]
    l2 = [1,3,4]
    l1 = convert_list_to_linked(l1)
    l2 = convert_list_to_linked(l2)
    obj = Solution()
    head = obj.mergeTwoLists(l1, l2)
    while head is not None:
        print(head.val)
        head = head.next
