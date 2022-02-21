class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        n=len(nums)
        nums.sort()
        while((i+n//2)<n):
            if(nums[i]==nums[i+n//2]):
                return nums[i]
            i+=1
        