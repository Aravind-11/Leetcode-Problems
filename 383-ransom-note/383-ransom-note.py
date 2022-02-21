class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote)>len(magazine):
            return False
        a={}
        for i in set(ransomNote):
            a[i]=0
        for i in ransomNote:
            a[i]+=1
        counter=len(a)
        end=0
        while(end<len(magazine)):
            endchar=magazine[end]
            if endchar in a:
                a[endchar]-=1
                if(a[endchar]==0):
                    counter-=1
            end+=1
        if counter<=0:
            return True
        return False