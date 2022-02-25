class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                c.append(nums[i])
        for i in range(len(c)):
            nums[i]=c[i]
        for i in range(len(c),len(nums)):
            nums[i]=0
            