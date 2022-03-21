#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        # Code here
        i,sign,result=0,1,0
        while string[i]==" ":
            i+=1
        if string[i]=='-' or string[i]=='+':
            sign=1-2*(string[i]=='-')
            i+=1
        while i<len(string):
            if string[i]>='0' and string[i]<='9':
                result=result*10+(ord(string[i])-ord('0'))
                i+=1
            else:
                return -1
        return sign*result

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends