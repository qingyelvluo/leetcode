#coding: utf8

class Solution(object):
    """针对输入的字符串，逆序输出
    提示：通过双指针实现
    """
    def reverse(self, word):
        length = len(word)
        word_list = list(word)
        # 双指针的首位索引
        i, j = 0, length-1
        while i < j:
            word_list[i], word_list[j] = word_list[j], word_list[i]
            i += 1
            j -= 1
            
        return "".join(word_list)
    
if __name__ == "__main__": 
    word ="hello"
    obj = Solution()
    print(obj.reverse(word))
