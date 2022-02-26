class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i=0
        list1=[]
        while i <(len(nums)-2):
            ele=nums[i]
            j=i+1
            k=len(nums)-1
            while j<k:
                
                if ele+nums[j]+nums[k]==0:
                    if [ele,nums[j],nums[k]] not in list1:
                        list1.append([ele,nums[j],nums[k]])
                    j+=1
                    k-=1
                elif ele+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k-=1
            i+=1
    
        
        
        
        return list1
    
                    