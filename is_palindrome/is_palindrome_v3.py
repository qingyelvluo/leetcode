#coding: utf8

# 解题思路：
# 遍历一半 x 的数字长度，最后根据偶数位、奇数位判断返回

class Solution(object):
    def isPalindrome(self, x):
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        # 记录 x 后一半的翻转，如 x = 4334，reversed = 43；x = 54345，reversed = 54
        reverse_num = 0
        # 只需遍历一半 x 的数字长度
        while x > reverse_num:
            reverse_num = reverse_num * 10 + x % 10
            x //= 10
        # x == reverse_num 成立一定是偶数位，x == reverse_num // 10 成立一定是奇数位
        return x == reverse_num or x == reverse_num // 10

if __name__ == "__main__":
    x = 12221
    obj = Solution()
    print(obj.isPalindrome(x))

