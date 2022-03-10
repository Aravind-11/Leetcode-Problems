class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        def find_pivot(nums):
            l,h=0,len(nums)-1
            pos=None
            while l<=h:
                m=(l+h)//2
                if nums[m]<nums[0]:
                    pos=m
                    h=m-1
                else:
                    l=m+1
                
            return pos
        pos=find_pivot(nums)
        if not pos:
            return nums[0]
        return nums[pos]
        