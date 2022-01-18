#coding: utf8

# 简单粗暴：
# 遍历元素，命中中删除


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                nums.pop(i)
                length -= 1
            else:
                i += 1
        return length
