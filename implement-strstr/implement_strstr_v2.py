#coding: utf8

# 滑动窗口算法(一种思想)：
# 以目的字符串(要匹配字符串)长度为窗口，逐步右移(step=1)，与目的字符串比较
# 如果相等，则返回索引值(自定义变量 i)。循环完成后，匹配不到的话，返回 -1
# 注意临界条件！

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if not needle:
            return 0
        i = 0
        first_str = needle[0]
        # 注意临界条件
        while i + n <= m:
            if haystack[i] == first_str:
                if haystack[i:i+n] == needle:
                    return i
            i += 1
        return -1

if __name__ == "__main__":
    haystack = ""
    needle = ""
    obj = Solution()
    print(obj.strStr(haystack, needle))
