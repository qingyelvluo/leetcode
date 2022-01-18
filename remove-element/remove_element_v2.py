#coding: utf8

# 说明：此代码并没有修改原数组，为什么可以检测通过？
# 例如：
# 输入: [3,2,2,3], 3
# 代码运行后长度为2，但是数组为[2, 2, 2, 3]，为什么可以检测通过？不应该是[2, 2]吗？


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 记录不等于 val 的元素个数
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
