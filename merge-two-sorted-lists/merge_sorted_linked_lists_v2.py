# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_value_list(*linklist):
    list_ = []
    for item in linklist:
        while item:
            list_.append(item.val)
            item = item.next
    return list_


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list2 or list1
        tmp_list = get_value_list(list1, list2)
        tmp_list.sort()
        head = ListNode(tmp_list[0])
        cursor = head
        for i in range(1, len(tmp_list)):
            node = ListNode(tmp_list[i])
            cursor.next = node
            cursor = node
        return head
