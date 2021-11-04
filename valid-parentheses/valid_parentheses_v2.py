#coding: utf8

# 解题思路：
# 栈：后入先出，先入的元素在栈底。只允许在一端进行操作（出栈、入栈）
# 利用栈结构，遍历字符串，先入栈每种括号的另一半，当遍历到非匹配括号时，对出栈元素判断
# 注意一些特例情况 "(" "(("

'''
执行用时：32 ms, 在所有 Python3 提交中击败了70.33%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了15.79%的用户
通过测试用例：91 / 91
'''

class Solution(object):
    def isValid(self, s: str) -> bool:
        stack_list = []
        for i in s:
            if i == "(":
                stack_list.append(")")
            elif i == "[":
                stack_list.append("]")
            elif i == "{":
                stack_list.append("}")
            # 对出栈元素判断，不相等直接返回False
            # 出栈元素判断前，需判断栈是否为空（如"([]))"），为空返回False
            elif not stack_list or i != stack_list.pop():
                return False

        # "(" "((" 等不会再做出栈操作（已经退出遍历），此处增加判断
        # 非空直接返回False，否则返回True
        return False if stack_list else True

if __name__ == "__main__":
    str_ = "([{)}])"
    obj = Solution()
    print(obj.isValid(str_))

