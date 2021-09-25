#coding: utf8

# 解题思路是什么样的？
# 

class Solution(object):
    def twoSum(self, nums, target):
        d = [target-i for i in nums]
        for index, num in enumerate(nums):
            if num in d and index!=d.index(num):
                return [index, d.index(num)]

if __name__ == "__main__":
    nums = [3, 2, 5]
    target = 7
    obj = Solution()
    print(obj.twoSum(nums, target))
