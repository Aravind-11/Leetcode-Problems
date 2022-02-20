class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        sum1=0
        while(i<len(nums)-1):
            sum1+=min(nums[i],nums[i+1])
            i+=2
        return sum1