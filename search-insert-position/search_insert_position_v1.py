# 解题思路：
# 各种特殊情况匹配判断，效率低下

'''
执行用时：44 ms, 在所有 Python3 提交中击败了5.13%的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了5.12%的用户
'''

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if not nums:
            return 0
        if length == 1:
            if nums[0] == target:
                return 0
            elif nums[0] > target:
                return 0
            else:
                return 1
        i = 0
        while i < length - 1:
            first_diff = nums[i] - target
            second_diff = nums[i+1] - target
            if first_diff > 0:
                return 0
            if first_diff == 0:
                return i
            if second_diff == 0:
                return i + 1
            if first_diff < 0 and second_diff > 0:
                return i + 1
            i += 1
        return i + 1

if __name__ == "__main__":
    obj = Solution()
    nums = [1, 3, 4]
    target = 7
    print(obj.searchInsert(nums, target))
