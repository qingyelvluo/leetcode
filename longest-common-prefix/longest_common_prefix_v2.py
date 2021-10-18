#coding: utf8

# 解题思路
# 利用max()和min()，在Python里字符串是可以比较的，按照ascII值排，举例abb, aba, abac最大为abb，最小为aba
# 所以只需要比较最大最小的公共前缀，就得到整个数组的公共前缀

'''
执行用时：20 ms, 在所有 Python 提交中击败了58.68%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了42.32%的用户
通过测试用例：
123 / 123
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_str = min(strs)
        max_str = max(strs)
        # enumerate 既取到下标，又得到元素值
        for index, str_ in enumerate(min_str):
            if str_ != max_str[index]:
                # 巧妙利用切片，避免构造列表存储匹配到的字符串
                return min_str[:index]
        return min_str

if __name__ == "__main__":
    strs = ["flower","flow","fle"]
    strs = ['']
    instance = Solution()
    print(instance.longestCommonPrefix(strs))

