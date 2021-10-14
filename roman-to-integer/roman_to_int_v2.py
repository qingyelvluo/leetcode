#coding: utf8

# 解题思路如何理解？
# 充分利用罗马数字顺序排列及特定规则，不太容易理解

class Solution(object):
    def romanToInt(self, s):
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        length = len(s)
        for i in range(length):
            if i < length -1 and a[s[i]] < a[s[i+1]]:
                result -= a[s[i]]
            else:
                result += a[s[i]]

        return result

if __name__ == "__main__":
    obj = Solution()
    print(obj.romanToInt("II"))
    print(obj.romanToInt("IV"))
    print(obj.romanToInt("LVIII"))
    print(obj.romanToInt("MCMXCIV"))

