#coding: utf8

# 解题思路
# 对输入整数x进行拆解，逐层计算出每一级值，最后求和。有技巧性，不容易理解记忆。
# 需要注意的是python针对负数的除法、取模机制！！！

'''
执行用时：36 ms, 在所有 Python3 提交中击败了58.48%的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了95.42%的用户
通过测试用例：1032 / 1032
'''

class Solution(object):
    def reverse(self, x):
        n = 0
        while x != 0:
            if x > 0:
                # 取余（取模）
                n = n*10 + x%10
                # 取整数
                x = x // 10
            else:
                # 如果x为负数，转为正数运算。避开python针对负数的取整 取余处理逻辑
                n = n*10 - abs(x)%10
                # 取整数
                x = -(abs(x) // 10)

        left_num_border = -pow(2, 31)
        right_num_border = pow(2, 31) - 1
        # 32 位的有符号整数的范围判断
        if n < left_num_border or n > right_num_border:
            return 0
        else:
            return n

if __name__ == "__main__":
    x = 1534236469
    obj = Solution()
    print(obj.reverse(x))

