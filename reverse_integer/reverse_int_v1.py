#coding: utf8

# 解题思路：
# 1. 通过内置函数，转变整数为str类型，逆序输出
# 2. 如果是有符合整数，重新处理一次
# 3. 注意需要判断是否超过32位的有符号整数的范围
'''
执行用时：36 ms, 在所有 Python3 提交中击败了58.48%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了8.47%的用户
通过测试用例：1032 / 1032
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse_str_num = str(x)[::-1]
        if reverse_str_num.endswith("-"):
            # 有符号整数，把"-"放回头部
            reverse_str_num = "-" + reverse_str_num[-2::-1][::-1]
        reverse_num = int(reverse_str_num)
        left_num_border = -pow(2, 31)
        right_num_border = pow(2, 31)
        # 32 位的有符号整数的范围判断
        if reverse_num < left_num_border or reverse_num > right_num_border:
            return 0
        else:
            return reverse_num

if __name__ == "__main__":
    x = 123
    obj = Solution()
    print(obj.reverse(x))

