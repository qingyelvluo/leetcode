#coding: utf8

# 取巧方法：
# 使用内置字符串函数 find()，直接获取字符串索引

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return haystack.find(needle)

if __name__ == "__main__":
    haystack = "hello"
    needle = ""
    obj = Solution()
    print(obj.strStr(haystack, needle))
