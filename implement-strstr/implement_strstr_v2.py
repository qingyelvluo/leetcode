#coding: utf8

# 滑动指针(一种思想)：
# 以目的字符串（要匹配字符串）长度为窗口，逐步右移，与目的字符串比较
# 如果相等，则返回索引值。循环完成后，匹配不到的话，返回 -1
# 注意临界条件！

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if m < n:
            return -1
        i = 0
		# 注意临界条件
        while i+n <= m:
            if haystack[i:i+n] == needle:
                return i
            i += 1
        return -1
        

if __name__ == "__main__":
    haystack = "helloelx"
    needle = "lx"
    obj = Solution()
    print(obj.strStr(haystack, needle))
