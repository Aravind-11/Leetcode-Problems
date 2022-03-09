class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def bSearch(nums,target):
            l,h=0,len(nums)-1
            while l<=h:
                m=(l+h)//2
                if nums[m]==target:
                    return True
                elif nums[m]<target:
                    l=m+1
                else:
                    h=m-1
            return False
        i=0
        while i<len(matrix):
            if target<=matrix[i][len(matrix[0])-1]:
                return bSearch(matrix[i],target)
            else:
                i+=1
        
        return False