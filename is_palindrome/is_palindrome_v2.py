#coding: utf8

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0:
            return False
        res = 0
        tmp_x = x
        while tmp_x != 0:
            if tmp_x > 0:
                quyu = tmp_x % 10
                res = res*10 + quyu
                tmp_x = tmp_x // 10

        if res == x:
            return True
        else:
            return False

if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome(121))
