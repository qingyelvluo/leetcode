#coding: utf8

# 代码完美解决问题
# 使用双指针，从最左、最右相向进行遍历，同时利用python的语法特性，交换赋值时无需中间变量。
# 需要注意临界条件，如while循环的判断变量不能相等，避免数组索引溢出

class Solution(object):

    def reverseVowels(self, word):
        """双指针进行遍历
        """
        vowels = "aeiouAEIOU"
        length = len(word)
        i, j = 0, length-1
        word_list = list(word)
        while i < j:
            if word_list[i] in vowels and word_list[j] in vowels:
                word_list[i], word_list[j] = word_list[j], word_list[i]
                i += 1
                j -= 1

            if word_list[i] not in vowels:
                i += 1

            if word_list[j] not in vowels:
                j -= 1

        return "".join(word_list)

if __name__ == "__main__":
    word = "leetcode"
    obj = Solution()
    print(obj.reverseVowels(word))

