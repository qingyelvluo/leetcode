class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse_str_num = str(x)[::-1]
        if reverse_str_num.endswith("-"):
            reverse_str_num = "-" + reverse_str_num[-2::-1][::-1]
        return int(reverse_str_num)

if __name__ == "__main__":
    x = 123
    obj = Solution()
    print(obj.reverse(x))
