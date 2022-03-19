class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        max_so_far=-3*10**4
        min_so_far=3*10**4
        max_ending_here=0
        min_ending_here=0
        for i in nums:
            
            max_ending_here+=i
            if max_so_far<max_ending_here:
                max_so_far=max_ending_here
            if max_ending_here<0:
                max_ending_here=0
            
            min_ending_here+=i
            if min_so_far>min_ending_here:
                min_so_far=min_ending_here
            if min_ending_here>0:
                min_ending_here=0
                
        if sum(nums)==min_so_far:
            return max_so_far
        return max(max_so_far,(sum(nums)-min_so_far))
        
        
        
        