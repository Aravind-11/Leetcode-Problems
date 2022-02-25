class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        c=1
        i=1
        k=len(nums)
        while i<len(nums):
            if nums[i]==nums[i-1]:
                c+=1
            if c>2:
                del nums[i]
                c-=1
                i-=1
            if nums[i]!=nums[i-1]:
                c=1
            i+=1
        
                
        