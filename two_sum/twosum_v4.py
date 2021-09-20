#coding: utf8

# 解题思路：
# 1、遍历数组，取出下标和对应元素
# 2、以元素为key，索引为value，把列表转为字典
# 3、两数之和，以其中一元素为key，必然可以取出对应下标

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            # 以元素为key，索引为value，把列表转为字典
            hashmap[num] = index
        return None

if __name__ == "__main__":
    obj = Solution()
    nums = [3, 2, 4]
    target = 6
    print(obj.twoSum(nums, target))
