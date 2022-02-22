class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        perm=[]
        max_d=len(s)
        min_i=0
        for i in s:
            if(i=='D'):
                perm.append(max_d)
                max_d-=1
            else:
                perm.append(min_i)
                min_i+=1
        for i in range(len(s)+1):
            if i not in perm:
                perm.append(i)
        return perm
        
        