# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def helper(root,temp,ans):
            if not root:return 
            if not root.left and not root.right:
                temp+=str(root.val)
                ans.append(temp)
                return
            temp+=str(root.val)+'->'
            helper(root.left,temp,ans)
            helper(root.right,temp,ans)
        temp=''
        ans=[]
        helper(root,temp,ans)
        return ans
            
        