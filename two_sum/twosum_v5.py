#coding: utf8

# 解题思路：
#  暴力解法，两个循环，每两个数相加判断结果，时间复杂度O(n^2)
#  效率不高，但是思路最容易理解！
#  执行用时：1864 ms, 在所有 Python 提交中击败了34.71%的用户
#  内存消耗：13.8 MB, 在所有 Python 提交中击败了53.59%的用户


class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 8
    obj = Solution()
    print(obj.twoSum(nums, target))
