class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        end=0
        begin=0
        a={}
        for i in set(s1):
            a[i]=0
        for i in s1:
            a[i]+=1
        counter=len(a)
        while(end<len(s2)):
            endchar=s2[end]
            
            if(endchar in a):
                a[endchar]-=1
                
                if(a[endchar]==0):
                    counter-=1
            
            end+=1
           
            
            while(counter==0):
                if(end-begin==len(s1)):
                    return True
                
                startchar=s2[begin]
                if( startchar in a):
                    a[startchar]+=1
                    if(a[startchar]>0):
                        counter+=1
                begin+=1
        return False