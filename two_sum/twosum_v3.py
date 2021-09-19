#coding: utf8

# 解题思路：
#   直接对索引（下标）排序，有下标也就定位到原始元素位置
#   代码更简单，理解起来稍微有点绕

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 先对索引（下标）以元素值从小到大排序
        sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
        head = 0
        tail = len(nums) - 1
        # sorted_id 是排序后的索引列表，记录了原始元素位置
        # head tail实际为原始元素位置
        sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        while head < tail:
            if sum_result == target:
                return [sorted_id[head], sorted_id[tail]]
            if sum_result > target:
                tail -= 1
            elif sum_result < target:
                head += 1
            sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        return None
if __name__ == "__main__":
    obj = Solution()
    sums = [3, 2, 4]
    target = 6
    print(obj.twoSum(sums, target))
