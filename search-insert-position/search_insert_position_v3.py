# 解题思路：
# 粗暴解法，遍历数组，判断每一个元素，最后返回符合条件的下标

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] >= target:
                return i
        return length
