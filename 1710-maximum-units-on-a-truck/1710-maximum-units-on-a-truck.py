class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        for i in range(len(boxTypes)):
            
            for j in range(len(boxTypes)-i-1):
                
                if boxTypes[j][1]<boxTypes[j+1][1]:
                    
                    boxTypes[j],boxTypes[j+1]=boxTypes[j+1],boxTypes[j]
        
        max_unit=0
        
        for i in range(len(boxTypes)):
            
            
            for j in range(0,boxTypes[i][0]):
                
                if not truckSize:
                    return max_unit
                max_unit+=boxTypes[i][1]
                truckSize-=1
        return max_unit
            
                