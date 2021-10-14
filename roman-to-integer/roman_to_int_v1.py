#coding: utf8

# 解题思路：
# 1、从尾到头遍历元素，先取前两个元素拼接，判断是否在字典中；
# 2、如果拼接的元素存在，说明是特殊规则，计算结果，并向左移动两个下标；
# 3、拼接的元素不在字典，取最右元素（说明是常规罗马数字）计算结果，向左移动一个下标；

# 注意：索引为0时，不可再移动下标计算，否则索引变成-1，将取出来最后一个元素

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
                "IV": 4,
                "IX": 9,
                "XL": 40,
                "XC": 90,
                "CD": 400,
                "CM": 900,
                }
        result = 0
        end = len(s) - 1
        while end >= 0:
            # 索引为0时，取第一个元素作为key，避免-1取到最后一个元素
            if end == 0:
                key = s[end]
            else:
                key = s[end-1] + s[end]
            if mapping.has_key(key):
                result += mapping[key]
                end -= 2
            else:
                result += mapping[s[end]]
                end -= 1

        return result

if __name__ == "__main__":
    obj = Solution()
    print(obj.romanToInt("MMMCDXC"))

