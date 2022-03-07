#User function Template for python3
class Solution:

	def findSum(self,a, b):
		# code here
		c1=c2=''
	    for i in a:
	        c1+=str(i)
	    for i in b:
	        c2+=str(i)
		return list(str(int(c1)+int(c2)))

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findSum(a, b)
        for i in ans:
            print(i, end=" ")
        print()
        tc -= 1

# } Driver Code Ends