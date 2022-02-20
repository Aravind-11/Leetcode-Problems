class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x=''
        
        dict1={}
        if(len(list(set(s)))!=len(list(set(t)))):
            return False
        for i in range(len(s)) :
            dict1[s[i]]=t[i]
        for i in s:
            x+=dict1[i]
        if(x==t):
            return True
        return False
            
        