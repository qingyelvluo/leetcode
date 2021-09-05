#coding: utf8

# 删除有序数组中重复的元素

def del_duplicate_item(array):
    """对于给定的有序数组，删除重复元素
    双指针思路，快慢指针分别进行：
        如果快指针跟慢指针不同，说明不重复元素，赋值到慢指针位置
        否则，说明有重复元素，进行删除同时指针位置减1，总长度减1
    """
    length = len(array)
    slow = 0
    fast = 1
    while fast < length:
        if array[slow] != array[fast]:
            slow += 1
            array[slow] = array[fast]
        else:
            del array[fast]
            fast -= 1
            length -= 1
        fast += 1

    return array

array = list("1233456")
print(del_duplicate_item(array))
