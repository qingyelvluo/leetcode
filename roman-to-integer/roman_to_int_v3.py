#coding: utf8

# 解题思路：
# 1、替换掉特殊规则的罗马数字，以新的字符组成一个大的映射
# 2、遍历新的罗马数字字符串，累加求和

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace("IV", "Q")
        s = s.replace("IX", "W")
        s = s.replace("XL", "E")
        s = s.replace("XC", "R")
        s = s.replace("CD", "T")
        s = s.replace("CM", "Y")

        mapping = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
                "Q": 4,
                "W": 9,
                "E": 40,
                "R": 90,
                "T": 400,
                "Y": 900,
                }
        result = 0
        for i in s:
            result += mapping[i]

        return result

if __name__ == "__main__":
    obj = Solution()
    print(obj.romanToInt("II"))
    print(obj.romanToInt("IV"))
    print(obj.romanToInt("LVIII"))
    print(obj.romanToInt("MCMXCIV"))
    print(obj.romanToInt("MMMCDXC"))

