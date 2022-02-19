class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        
        if not n:
            return True
        i=1
        if(len(flowerbed)==1):
            if(flowerbed[0]==0):
                n-=1
        while(i<len(flowerbed)):
            if(i==1 and flowerbed[i-1]==0 and flowerbed[i]==0):
                flowerbed[i-1]=1
                i+=1
                n-=1
            elif(i==(len(flowerbed)-1) and flowerbed[i]==0 and flowerbed[i-1]==0):
                flowerbed[i]=1
                i+=2
                n-=1
            elif(i!=(len(flowerbed)-1) and flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0):
                flowerbed[i]=1
                i+=2
                n-=1
            else:
                i+=1
                
            """
        prev=0
        
        for i in flowerbed:
            if(i==1):
                if(prev==1):
                    n+=1
                
                prev=1
            else:
                if(prev!=1):
                    n-=1
                    prev=1
                else:
                    prev=0
                
        
            
                
            
        if n<=0:
            return True
        return False
        