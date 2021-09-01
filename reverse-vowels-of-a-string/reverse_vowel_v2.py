#coding: utf8

class Solution(object):

    def __init__(self):
        pass
    
    def reverse_vowel_core(self, word, left_list, right_list):
        """实现元音字母的对折，核心处理逻辑
        """
        word_list = list(word)
        left_list_length = len(left_list)
        right_list_length = len(right_list)
        small_length = left_list_length if left_list_length <= right_list_length else right_list_length
        for i in range(small_length):
            word_list[left_list[i].keys()[0]] = right_list[i].values()[0]
            word_list[right_list[i].keys()[0]] = left_list[i].values()[0]

        return "".join(word_list)

    def reverseVowels(self, word):
        """左右分别遍历给定字符串
        匹配到元音字母后，以索引为key，元音为value，组成字典分别追加到列表
        """
        vowels = "aeiouAEIOU"
        length = len(word)
        print("length: ", length)
        left_list = []
        right_list = []
        for i in range(length):
            print(i)
            if i == length/2:
                break
            print("from left: ", word[i])
            if word[i] in vowels:
                left_list.append({i: word[i]})
            print("from right: ", word[length-i-1])
            if word[length-i-1] in vowels:
                right_list.append({length-i-1: word[length-i-1]})
        if left_list and right_list:
            #word = self.reverse_vowel_core(word, left_list, right_list)
            #return word
            return left_list, right_list
        else:
            return word

if __name__ == "__main__":
    #word = "hello"
    word = "Marge, let's \"went.\" I await news telegram."
    obj = Solution()
    print(obj.reverseVowels(word))

