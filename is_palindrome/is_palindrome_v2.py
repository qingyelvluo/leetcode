#coding: utf8

# 解题思路：
# 利用上一题整数反转的思路，把输入的整数反转，对比反转后的值
# 关键是整数反转一块的代码，如何理解

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        res = 0
        tmp_x = x
        while tmp_x != 0:
            if tmp_x > 0:
                quyu = tmp_x % 10
                res = res*10 + quyu
                tmp_x = tmp_x // 10

        return res == x

if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome(123))

