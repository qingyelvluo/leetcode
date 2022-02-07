# 解题思路，快慢指针：
# 首先判断首尾元素，符合条件的话直接返回
# 然后定义快慢指针，每两两元素比较，符合条件的话，返回对应位置

'''
执行用时：36 ms, 在所有 Python3 提交中击败了42.83%的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了9.08%的用户
'''

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if not nums or nums[0] >= target:
            return 0
        if nums[length-1] < target:
            return length
        slow = 0
        fast = 1
        while fast < length:
            if nums[slow] == target:
                return slow
            if nums[fast] == target:
                return fast
            if nums[slow] < target and nums[fast] > target:
                return fast
            slow += 1
            fast += 1

if __name__ == "__main__":
    obj = Solution()
    nums = [1, 3, 4]
    target = 5
    print(obj.searchInsert(nums, target))
