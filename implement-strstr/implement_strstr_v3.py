#coding: utf8


# 解释说明：
# 效率低下，因为做了全量比对

'''
执行结果：通过
执行用时：
2872 ms, 在所有 Python 提交中击败了6.52%的用户
内存消耗：
14.6 MB, 在所有 Python 提交中击败了17.57%的用户
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        h_length, n_length = len(haystack), len(needle)
        for i in range(h_length+1):
            if needle in haystack[0:i]:
                return i - n_length
        return -1

if __name__ == "__main__":
    haystack = "helloelx"
    needle = "elx"
    obj = Solution()
    print(obj.strStr(haystack, needle))
