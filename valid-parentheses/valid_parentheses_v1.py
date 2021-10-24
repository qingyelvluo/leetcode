#coding: utf8

# 解题思路：
# 有效括号必然是成对的() [] {}
# 反复替换直到字符串不再包含上面有效括号
# 最终字符串为空说明是有效的，非空说明无效字符串
# 问题：
# 方法巧妙，效率低下。时间复杂度高，in复杂度为N，replace复杂度为N
'''
执行用时：64 ms, 在所有 Python 提交中击败了10.19%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了57.15%的用户
通过测试用例：
91 / 91
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')

        return s == ""

if __name__ == "__main__":
    instance = Solution()
    print(instance.isValid('{()[({})]}'))
