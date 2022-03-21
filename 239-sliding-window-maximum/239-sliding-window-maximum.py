class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        ans=[]
        dq=deque()
        for i in range(len(nums)):
            if len(dq)!=0 and dq[0]==(i-k):
                dq.popleft()
            while len(dq)!=0 and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                ans.append(nums[dq[0]])
        return ans