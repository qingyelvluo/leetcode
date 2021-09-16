'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # sort array first
        #nums = sorted(nums)
        start, end = 0, len(nums)-1
        while start < end:
            if nums[start] + nums[end] == target:
                return [start, end]
            elif nums[start] + nums[end] > target:
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
        return None
if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    obj = Solution()
    print(obj.twoSum(nums, target))
'''
class Solution(object):
    def twoSum(self, nums, target):
        tmp_dict = {}
        for i, j in enumerate(nums):
            tmp_dict[i] = j
        return tmp_dict

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    obj = Solution()
    print(obj.twoSum(nums, target))
