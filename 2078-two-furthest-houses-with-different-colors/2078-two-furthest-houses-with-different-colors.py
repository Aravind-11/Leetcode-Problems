class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        max_d=0
        for i in range(len(colors)):
            house1=colors[i]
            for j in range(len(colors)):
                if house1!=colors[j]:
                    max_d=max(max_d,abs(j-i))
        return max_d
        