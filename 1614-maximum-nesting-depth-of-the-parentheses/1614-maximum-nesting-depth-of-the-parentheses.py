class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxC=0
        c=0
        stack=[]
        for i in s:
            if i=='(':
                c+=1
                stack.append(i)
            
            if i==')':
                c-=1
                stack.pop()
                
            maxC=max(maxC,c)
            
            if len(stack)==0:
                c=0
        return maxC