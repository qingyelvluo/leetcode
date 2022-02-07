# 解题思路，二分法查找：
# 先算出来中间索引值，然后与 target 比较，根据 target 大、小分别向右或者左遍历比较
# 注意：
# 1、边界条件设定，右指针为数组长度减 1，同时 left 与 right 相等；
#    如 nums = [1, 3, 5, 8], target = 4，需要指针往右再遍历比较一次
# 2、计算出来 left right 后，需要再算一次中间值，作为返回下标

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        # 注意边界条件
        while left <= right:
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
            mid = (left + right) // 2
        return mid + 1

if __name__ == "__main__":
    nums = [2, 3, 5, 6]
    target = 7
    obj = Solution()
    print(obj.searchInsert(nums, target))
