class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        a={}
        for i in set(position):
            a[i]=0
        for i in range(len(position)):
            for j in range(len(position)):
                if(position[i]!=position[j]):
                    if(abs(position[i]-position[j])%2==0):
                        a[position[i]]+=1
        
        
        max1=max_pos=0
        for i,j in enumerate(a):
            if(a[j]>max1):
                max1=a[j]
                max_pos=j
        if(max_pos==0):
            a={}
            for i in set(position):
                a[i]=0
            for i in position:
                a[i]+=1
            for i,j in enumerate(a):
                if(a[j]>max1):
                    max1=a[j]
                    max_pos=j
        cost=0
        for i in position:
            
            if( i != max_pos):
                dist=abs(i-max_pos)
                if(dist%2==0):
                    pass
                else:
                    cost+=1
        return cost
            
        