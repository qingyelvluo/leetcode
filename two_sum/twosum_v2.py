#coding: utf8

# 解题思路：
# 1、先通过数组下标及对应元素构成字典，存入列表
# 2、对数组排序（以value排序，对应key自动保留记录）
# 3、使用双指针对有序数组分别遍历
# 优点：
#   思路清晰
# 缺点：
#   执行用时：36 ms, 在所有 Python 提交中击败了56.48%的用户
#   内存消耗：16.2 MB, 在所有 Python 提交中击败了5.06%的用户

class Solution(object):
    def twoSum(self, nums, target):
        tmp_list = []
        for i, j in enumerate(nums):
            tmp_dict = {}
            tmp_dict[i] = j
            tmp_list.append(tmp_dict)
        tmp_list = sorted(tmp_list, key=lambda x: x.values()[0])
        start, end = 0, len(tmp_list)-1
        while start < end:
            if tmp_list[start].values()[0] + tmp_list[end].values()[0] == target:
                return [tmp_list[start].keys()[0], tmp_list[end].keys()[0]]
            elif tmp_list[start].values()[0] + tmp_list[end].values()[0] > target:
                end -= 1
            elif tmp_list[start].values()[0] + tmp_list[end].values()[0] < target:
                start += 1
        return None

if __name__ == "__main__":
    nums = [3,2,4]
    target = 7
    obj = Solution()
    print(obj.twoSum(nums, target))
