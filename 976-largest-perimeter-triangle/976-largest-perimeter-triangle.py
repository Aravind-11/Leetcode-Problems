class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def checkTriangle(a,b,c):
            if(a+b<=c or b+c<=a or c+a<=b):
                return False
            return True
        nums.sort(reverse=True)
        
            
        max_peri=0
        i=0
        while(i+2<len(nums)):
            a,b,c=nums[i],nums[i+1],nums[i+2]
            if checkTriangle(a,b,c):
                return(a+b+c)
        
            i+=1
        return max_peri
                    
                