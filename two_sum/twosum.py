#coding: utf8

# 解题思路：
# 1、先通过数组下标及对应元素构成二维数组，存入列表
# 2、对二维数组排序（以元素排序，对应下标自动保留记录）
# 3、使用双指针对有序数组分别遍历
# 优点：
#   思路清晰
# 缺点：
#   执行用时：24 ms, 在所有 Python 提交中击败了69.88%的用户
#   内存消耗：14.8 MB, 在所有 Python 提交中击败了5.06%的用户

class Solution(object):
    def twoSum(self, nums, target):
        tmp_list = []
        # 以数组下标 元素构成二维数组，放入列表
        for i, j in enumerate(nums):
            tmp_list.append([i, j])
        # 先对二维数组排序（以元素排序，记录下来下标）
        tmp_list = sorted(tmp_list, key=lambda x: x[1])
        start, end = 0, len(tmp_list)-1
        # 双指针前后分别遍历
        while start < end:
            if tmp_list[start][1] + tmp_list[end][1] == target:
                return [tmp_list[start][0], tmp_list[end][0]]
            elif tmp_list[start][1] + tmp_list[end][1] > target:
                end -= 1
            elif tmp_list[start][1] + tmp_list[end][1] < target:
                start += 1
        return None

if __name__ == "__main__":
    nums = [3,2,4]
    target = 5
    obj = Solution()
    print(obj.twoSum(nums, target))
