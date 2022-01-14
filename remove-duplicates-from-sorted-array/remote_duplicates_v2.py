#coding: utf8

# 两个指针：
# 一个是游标功能，负责遍历整个数组，一个是定位器功能，
# 如果有相等的则表示定位器目前指向的元素是重复的，定位器不动，等待游标往下找到不重复的数填充进来。
# 因为游标会遍历整个数组且总是比定位器快，所以数组中的一个元素被游标遍历后就没用了，
# 直接把不重复的数塞到定位器位置，定位器同步往后挪，最后定位器的位置 +1 就是去重数组的长度

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        locator = 1 
        for cursor in range(1, len(nums)):
            if nums[cursor] != nums[cursor-1]:
                nums[locator] = nums[cursor]
                locator += 1
        return locator
