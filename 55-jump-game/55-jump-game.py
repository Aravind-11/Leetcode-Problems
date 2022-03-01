class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i=len(nums)-1
        if len(nums)==1:
            return True
        if not nums[0]:
            return False
       
        if nums[0]>=len(nums)-1:
            return True
        
        while i>=0:
            
            if i==1 or i==0:
                return True
            
            max_j=-1
            
            j=i-1
            
            while j>-1:
                
                if j+nums[j]>=i:
                    max_j=j
                    break
                j-=1
            if max_j==-1:
                return False
            else:
                
                i=max_j
                    
        return False
            
                    
        