class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def count_bit(x):
            y=1
            c=0
            for i in range(32):
                if  y&x:
                    c+=1
                y=y<<1
            return c
        ans=[]
        for i in range(n+1):
            ans.append(count_bit(i))
        return ans
        