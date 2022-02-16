class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=[]
        if not s:
            return True
        if (len(s)==1):
            return False
        for i in range(len(s)) :
            if(s[i]=='[' or s[i]=='{' or s[i]=='('):
                c.append(s[i])
            if(s[i]==']' or s[i]=='}' or s[i]==')'):
                flag=1
                if(len(c)==0):
                    return False
                ele=c.pop()
                if(ele=='{' and s[i]=='}' or ele=='[' and s[i]==']' or ele=='(' and s[i]==')'):
                    pass
                    
                else:
                    return False
        if(len(c)!=0):
            return False
        return True 
                    
                
            
                
        
            
        