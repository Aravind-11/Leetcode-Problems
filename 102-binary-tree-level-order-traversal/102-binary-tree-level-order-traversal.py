# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root
        queue=[]
        result=[]
        level=[]
        queue.insert(0,root)
        while len(queue)!=0:
            
            c=[]
            
            n=len(queue)
            for i in range(n):
                temp=queue[-1]
                queue.pop()
                if temp.left:
                    queue.insert(0,temp.left)
                if temp.right:
                    queue.insert(0,temp.right)
                c.append(temp.val)
            result.append(c)
        return result
        