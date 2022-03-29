# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        c1=[]
        c2=[]
        def preOrder(root,c):
            if not root:
                return 
            if not root.left and not root.right:
                c.append(root.val)
            preOrder(root.left,c)
            preOrder(root.right,c)
        preOrder(root1,c1)
        preOrder(root2,c2)
        return c1==c2