#User function Template for python3

class Solution:
	def minimum_difference(self,nums):
	    arr=nums
    # Write your code here
        min_diff=10**9
        arr.sort()
        for i in range(len(arr)-1):
            min_diff=min(min_diff,abs(arr[i]-arr[i+1]))
        return min_diff
		# Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.minimum_difference(nums)
		print(ans)
# } Driver Code Ends