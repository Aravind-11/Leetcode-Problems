# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.diameter=0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find_height(root):
            if not root:
                return 0
            lh=find_height(root.left)
            rh=find_height(root.right)
            self.diameter=max(self.diameter,lh+rh)
            
            return 1+max(lh,rh)
        
        find_height(root)
        return self.diameter
        