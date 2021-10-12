#coding: utf8

# 解题思路
# 常规思路：把整数转换为字符串，通过双指针遍历判断

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse_str_x = str(x)
        start, end = 0, len(reverse_str_x)-1
        while start < end:
            if reverse_str_x[start] == reverse_str_x[end]:
                start += 1
                end -= 1
            else:
                return False

        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome(0))

