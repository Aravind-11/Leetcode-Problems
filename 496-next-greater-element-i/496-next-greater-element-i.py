class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c=[]
        flag=-1
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j]==nums1[i]:
                    flag=0
                    for k in range(j+1,len(nums2)):
                        if nums2[k]>nums2[j]:
                            flag=1
                            c.append(nums2[k])
                            break
                        
                    if flag==0:
                        c.append(-1)
        return c