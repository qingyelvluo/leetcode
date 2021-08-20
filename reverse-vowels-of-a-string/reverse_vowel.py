#coding: utf8

class Solution(object):

    def reverse_vowel_core(self, word, vowel_index_list):
        """实现元音字母最近两字母置换
        """
        word_list = list(word)
        vowel_length = len(vowel_index_list)
        for j in range(0, vowel_length, 2):
            tmp_list = []
            # 反转字典key value，取出索引
            tmp_list.extend([(v, k) for k, v in vowel_index_list[j].iteritems()])
            tmp_list.extend([(v, k) for k, v in vowel_index_list[j+1].iteritems()])
            word_list[tmp_list[0][0]] = tmp_list[1][1]
            word_list[tmp_list[1][0]] = tmp_list[0][1]

        return ''.join(word_list)

    def reverseVowels(self, word):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        length = len(word)
        vowel_index_list = []
        for i in range(length):
            if word[i] in vowels:
                tmp_dict = {}
                tmp_dict[word[i]] = i
                vowel_index_list.append(tmp_dict)

        # vowel_index_list为空，说明word不含元音字母，原路返回
        if not vowel_index_list:
            return word
        
        k = 0
        vowel_length = len(vowel_index_list)
        while k < vowel_length-1:
            # 取偶数索引元素
            if k % 2 == 0:
                # 如果最近的两个字典的key一样，删除第一个
                if vowel_index_list[k].keys() == vowel_index_list[k+1].keys():
                    del vowel_index_list[k]
                    vowel_length -= 1
            k += 1

        if vowel_index_list and len(vowel_index_list) % 2 == 0:
            # 偶数个元素，最近两个字母置换
            reversed_word = self.reverse_vowel_core(word, vowel_index_list)
        if vowel_index_list and len(vowel_index_list) % 2 == 1:
            # 奇数个元素，把最后一个剔除，然后做置换
            vowel_index_list.pop(-1)
            reversed_word = self.reverse_vowel_core(word, vowel_index_list)
        
        return reversed_word

if __name__ == "__main__":
    ret = Solution().reverseVowels("race car")
    print(ret)

