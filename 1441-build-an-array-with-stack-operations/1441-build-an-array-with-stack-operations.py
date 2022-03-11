class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        check_list=[]
        out=[]
        beg_list=[]
        for i in range(1,n+1):
            beg_list.append(i)
        x=0
        g=len(beg_list)
        for i in range(g):
            if x==len(target):
                break
            check_list.append(beg_list[i])
            
            if check_list[x]==target[x]:
                out.append('Push')
                x+=1
            else:
                check_list.pop()
                out.append('Push')
                out.append('Pop')
            
            
        return out
            
        