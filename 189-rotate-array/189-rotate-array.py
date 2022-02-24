class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        if len(nums)==1:
            return
        c=nums[-k:]
        b=nums[:len(nums)-k]
        j=0
        
        for i in range(k):
            nums[i]=c[j]
            j+=1
        j=0
        for i in range(k,len(nums)):
            nums[i]=b[j]
            j+=1
        
            
        