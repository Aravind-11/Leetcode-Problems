class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=0
        d={0:1}
        presum=0
        for i in nums:
            presum+=i
            
            if presum-k in d:
                ans+=d[presum-k]
                
            if presum not in d:
                d[presum]=1
            else:
                d[presum]+=1
        return ans