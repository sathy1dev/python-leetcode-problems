class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        value = {}
        for i,n in enumerate(nums):
            if target - n in value:
                return value[target-n],i
            value[n] = i

array = [2,7,11,15]
target = 26
solve = Solution()
print(solve.twoSum(array,target))