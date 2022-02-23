class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j=0
        for i in range(len(nums1)-len(nums2),len(nums1)):
            if nums1[i]==0:
                nums1[i]=nums2[j]
                j+=1
        nums1.sort()
        '''
        i=j=k=0
        arr=[]
        for i in nums1:
            if i!=0:
                arr.append(nums1[i])
        while i<len(arr) and j<n:
            if arr[i]<nums2[j]:
                nums1[k]=arr[i]
                i+=1
                k+=1
            else:
                nums1[k]=nums2[j]
                j+=1
                k+=1
        while i < len(arr):
            nums1[k]=arr[i]
            i+=1
            k+=1
        while j < n:
            nums1[k]=nums2[j]
            j+=1
            k+=1
        '''
        
        