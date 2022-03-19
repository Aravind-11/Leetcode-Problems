class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nge=[0]*len(nums)
        st=[]
        n=len(nums)
        for i in range(2*n-1,-1,-1):
            while len(st)!=0 and st[-1]<=nums[i%n]:
                st.pop()
            if i<n:
                if len(st)!=0:
                    
                    nge[i%n]=st[-1]
                else:
                    nge[i%n]=-1
                
            st.append(nums[i%n])
        return nge
        