#coding: utf8

# 取巧方法：
# 调用语言api，直接获取字符串索引

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
