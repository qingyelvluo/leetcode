#coding: utf8

# 解题思路，双指针滑动窗口算法：
# 定义两个指针：左指针和右指针，左指针起始位置为0，右指针起始位置为模式字符串长度
# 指针间距离(窗口)大小即模式字符串长度，以该长度切片文本字符串，与模式字符串比较
# 如果相等，则返回左指针(即匹配到的索引位置)；不等的话，左右指针分别+1(右移)，进行滑动
# 临界条件：右指针等于文本字符串长度；不满足该条件时返回 -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        left = 0
        right = len(needle)
        while right <= len(haystack):
            if needle == haystack[left:right]:
                return left
            left += 1
            right += 1
        return -1

if __name__ == "__main__":
    haystack = "hello"
    needle = "lo"
    obj = Solution()
    print(obj.strStr(haystack, needle))
