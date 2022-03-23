# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.val==key:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            if root.right and root.left:
                pnt=root.right
                while pnt.left:
                    pnt=pnt.left
                root.val=pnt.val
                root.right=self.deleteNode(root.right,pnt.val)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        return root