#coding: utf8

# 解题思路
# 利用zip()函数
# 把输入看成二维数组，通过 *args 参数对二维数组解压，返回一个新的列表（元素个数等于最小长度的单词长度）
# 对列表的每个元素利用集合去重，
# 最后遍历列表，找到元素长度大于1之前的元素，拼接起来就是公共前缀

'''
执行用时：8 ms, 在所有 Python 提交中击败了99.75%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了37.32%的用户
通过测试用例：
123 / 123
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix_list = []
        zipped_list = list(zip(*strs))
        # 对zipped_list的每个元素(列表)去重
        zipped_list_set = map(set, zipped_list)
        for item in zipped_list_set:
            # 长度大于1的元素(列表)，说明存在不重合字母，不再符合条件
            if len(item) > 1:
                break
            prefix_list.extend(item)
        return ''.join(prefix_list) or ""

if __name__ == "__main__":
    strs = ["flower","flow","fle"]
    #strs = ['']
    instance = Solution()
    print(instance.longestCommonPrefix(strs))

