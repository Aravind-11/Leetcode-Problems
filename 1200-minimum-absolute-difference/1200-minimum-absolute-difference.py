class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        min_diff=10**9
        arr.sort()
        c=[]
        for i in range(len(arr)-1):
            if(abs(arr[i]-arr[i+1])<=min_diff):
                #c.append([arr[i],arr[i+1]])
                min_diff=abs(arr[i]-arr[i+1])
        for i in range(len(arr)-1):
            if(abs(arr[i]-arr[i+1])==min_diff):
                c.append([arr[i],arr[i+1]])
        return c