#coding: utf8

# 解题思路
# 以第一个单词为标准，遍历每个字母与后面每个单词的每个字母做比较

'''
执行用时：16 ms, 在所有 Python 提交中击败了86.47%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了67.82%的用户
通过测试用例：123 / 123
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix_list = []
        index = 0
        first_str = strs[0]
        first_str_len = len(first_str)
        while index < first_str_len:
            for str_ in strs[1:]:
                try:
                    if first_str[index] != str_[index]:
                        # 首字母相同，后面的字母不同时，需要返回已匹配公共前缀
                        return ''.join(prefix_list) or ""
                # 存在下标溢出的情况，捕获异常直接返回
                except IndexError:
                    return ''.join(prefix_list) or ""
            prefix_list.append(first_str[index])
            index += 1

        return ''.join(prefix_list)

if __name__ == "__main__":
    strs = ["flower","flow","fle"]
    instance = Solution()
    print(instance.longestCommonPrefix(strs))
