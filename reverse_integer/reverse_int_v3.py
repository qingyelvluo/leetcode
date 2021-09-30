#coding: utf8

# 解题思路
# 传统python思路，容易理解

'''
执行用时：36 ms, 在所有 Python3 提交中击败了58.48%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了11.54%的用户
'''

class Solution(object):
    def reverse(self, x):
        if x > 0:
            reverse_num = int(str(x)[::-1])
            return reverse_num if reverse_num < 2**31-1 else 0
        elif x < 0:
            reverse_num = -int(str(-x)[::-1])
            return reverse_num if reverse_num > -2**31 else 0
        return 0

if __name__ == "__main__":
    x = 1534236469
    obj = Solution()
    print(obj.reverse(x))

