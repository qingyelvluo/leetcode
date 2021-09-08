# 解题思路
# 1、第一次遍历把元音字母过滤出来，放入列表
# 2、第二次遍历把元音字母倒序替换回去，使用pop()函数


def reverse_vowel(word):
    vowels = "aeiouAEIOU"
    vowel_list = [i for i in word if i in vowels]
    word_list = list(word)
    for index, item in enumerate(word):
        if item in vowels:
            word_list[index] = vowel_list.pop()

    return "".join(word_list)

word = "leetcode"
print(reverse_vowel(word))
