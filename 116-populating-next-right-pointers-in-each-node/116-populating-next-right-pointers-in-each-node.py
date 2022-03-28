"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return 
        queue=[]
        queue.insert(0,root)
        
        while len(queue)!=0:
            
            n=len(queue)
            level=[]
            
            for i in range(n):
                temp=queue[-1]
                if temp.left:
                    queue.insert(0,temp.left)
                if temp.right:
                    queue.insert(0,temp.right)
                level.append(temp)
                queue.pop()
            for i in range(len(level)-1):
                level[i].next=level[i+1]
            level[-1].next=None
        return root
        
                
                
                
                
                