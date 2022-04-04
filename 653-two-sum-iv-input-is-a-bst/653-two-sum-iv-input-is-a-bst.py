# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        d={}
        if not root.left and not root.right:
            return False
        def helper(root,d,k):
            if not root:
                return 
            helper(root.left,d,k)
            d[k-root.val]=root.val
            helper(root.right,d,k)
        helper(root,d,k)
        def preOrder(root,d,k):
            if not root:
                return
            if root.val in d and root.val!=k-root.val:
                return True
            return preOrder(root.left,d,k) or preOrder(root.right,d,k)
            
        return preOrder(root,d,k)
            
        