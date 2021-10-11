#coding: utf8

# 解题思路
# 常规思路：把整数转换为字符串进行判断
# 两行代码实现，return 可以更加巧妙

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse_str_x = str(x)[::-1]
        return reverse_str_x == str(x)

if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome(121))

