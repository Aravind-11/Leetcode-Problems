class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,h=0,len(numbers)-1
        while l<h and l>=0 and h>=0:
            
            sum1=numbers[l]+numbers[h]
            if sum1==target:
                return [l+1,h+1]
            elif sum1>target:
                h-=1
            else:
                l+=1
        
            
            
            
        