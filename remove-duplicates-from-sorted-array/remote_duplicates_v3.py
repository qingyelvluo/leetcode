from typing import List

# 每两个元素相比，如果不相等则原地修改数组，把不重复的元素塞入定位器。
# 定位器加1（说明符合条件的数组长度+1）。
# 如果两个元素相等，则定位器不动，继续遍历元素，循环此判断，直到跳出循环

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """双指针实现"""

        cursor = 0
        locator = 1
        length = len(nums) - 1
        while cursor < length:
            if nums[cursor] != nums[cursor+1]:
                nums[locator] = nums[cursor+1]
                # 每两个元素不等，则计数 +1
                locator += 1
            cursor += 1
        return locator

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 4]
    obj = Solution()
    print(obj.removeDuplicates(nums))
