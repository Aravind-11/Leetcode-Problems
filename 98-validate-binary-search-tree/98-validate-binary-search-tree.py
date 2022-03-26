# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        
        if not root.left and not root.right:
            return True
        def checkVal(root,min_val,max_val):
            if not root:
                return True
            if root.val>=max_val or root.val<=min_val:
                return False
            if checkVal(root.left,min_val,root.val) and checkVal(root.right,root.val,max_val):
                return True
        if checkVal(root,-sys.maxsize,sys.maxsize):
            return True
        