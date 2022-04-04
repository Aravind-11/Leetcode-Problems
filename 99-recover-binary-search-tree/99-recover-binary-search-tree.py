# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.first=None
        self.middle=None
        self.end=None
        self.prev=None
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        
        def helper(root):
            if not root:
                return
            
            helper(root.left)
            
            if self.prev and root.val<self.prev.val:
                if not self.first:
                    self.first=self.prev
                    self.middle=root
                else:
                    self.end=root
            self.prev=root
            helper(root.right)
        helper(root)
        if self.end:
            self.first.val,self.end.val=self.end.val,self.first.val
        elif self.first:
            self.first.val,self.middle.val=self.middle.val,self.first.val
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        