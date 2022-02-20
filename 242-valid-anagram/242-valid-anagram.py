class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False
        a={}
        for i in s:
            a[i]=0
        for i in s:
            a[i]+=1
        counter=len(a)
        end=0
        while(end<len(t)):
            endchar=t[end]
            if(endchar in a):
                a[endchar]-=1
                if(a[endchar]==0):
                    counter-=1
            end+=1
        return not counter
        
        