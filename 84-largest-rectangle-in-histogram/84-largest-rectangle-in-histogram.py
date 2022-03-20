class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        left_smaller=[0]*len(heights)
        right_smaller=[len(heights)-1]*len(heights)
        def find_left(left_smaller,heights):
            stack=[]
            for i in range(len(heights)):
                while len(stack)!=0 and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                if len(stack)!=0:
                    left_smaller[i]=stack[-1]+1
                stack.append(i)
            return left_smaller
        def find_right(right_smaller,heights):
            stack=[]
            n=len(heights)
            for i in range(n-1,-1,-1):
                while len(stack)!=0 and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                if len(stack)!=0:
                    right_smaller[i]=stack[-1]-1
                stack.append(i)
            return right_smaller
        left_smaller=find_left(left_smaller,heights)
        right_smaller=find_right(right_smaller,heights)
        maxA=0
        print left_smaller
        print right_smaller
        #print left_smaller
        for i in range(len(heights)):
            maxA=max(maxA,(right_smaller[i]-left_smaller[i]+1)*heights[i])
        return maxA
                
                
        
        