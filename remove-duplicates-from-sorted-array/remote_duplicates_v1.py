from typing import List

# 思考：为什么效率这么低下？
# 体现在执行用时很长，为什么？是因为 nums.pop() 操作吗？


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """快慢指针实现"""

        slow = 0
        fast = 1
        length = len(nums)
        while fast < length:
            if nums[slow] == nums[fast]:
                nums.pop(slow)
                length -= 1
            else:
                slow += 1
                fast += 1
        return length

if __name__ == "__main__":
    nums = [1, 1]
    obj = Solution()
    print(obj.removeDuplicates(nums))

