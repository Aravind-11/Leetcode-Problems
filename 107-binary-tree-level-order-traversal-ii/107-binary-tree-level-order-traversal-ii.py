# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return
        ans=[]
        queue=[]
        queue.insert(0,root)
        while len(queue):
            level=[]
            n=len(queue)
            for _ in range(n):
                temp=queue[-1]
                if temp.left:
                    queue.insert(0,temp.left)
                if temp.right:
                    queue.insert(0,temp.right)
                level.append(temp.val)
                queue.pop()
            ans.append(level)
        return ans[::-1]
        