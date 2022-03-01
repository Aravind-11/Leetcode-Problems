class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=len(nums)-1
        if len(nums)==1:
            return 0
       
       
        if nums[0]>=len(nums)-1:
            return 1
        steps=0
        while i>=0:
            
            if i==1:
                steps+=1
                return steps
            if i==0:
                return steps
            
            max_j=-1
            
            j=i-1
            
            while j>-1:
                
                if j+nums[j]>=i:
                    max_j=j
                j-=1
            
            
            steps+=1
            i=max_j
                    
        
        