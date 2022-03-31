#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        # Code here
        if not root:
            return []
        c_left=[]
        c_right=[]
        c_leaves=[]
        def preOrder_left(root,c_left):
            if not root:
                return 
            c_left.append(root.data)
            if not root.left:
                preOrder_left(root.right,c_left)
            preOrder_left(root.left,c_left)
        
        def preOrder_right(root,c_right):
            if not root:
                return 
            c_right.append(root.data)
            if not root.right:
                preOrder_right(root.left,c_right)
            preOrder_right(root.right,c_right)
            
        def find_leaves(root,c_leaves):
            if not root:
                return 
            
            find_leaves(root.left,c_leaves)
            if not root.left and not root.right:
                c_leaves.append(root.data)
            find_leaves(root.right,c_leaves)
        
        if not root.left and not root.right:
            return [root.data]
            
        if not root.right:
            preOrder_left(root,c_left)
            
        elif not root.left:
            c_left.append(root.data)
            preOrder_right(root.right,c_right)
            
        else:
            preOrder_left(root,c_left)
            preOrder_right(root.right,c_right)
        find_leaves(root,c_leaves)
        c_right=c_right[::-1]
        if len(c_right):
            c_leaves=c_leaves[:len(c_leaves)-1]
        if len(c_left):
            c_leaves=c_leaves[1:]
        #print (c_left)
        #print(c_right)
        
        #print(c_leaves)
        return c_left+c_leaves+c_right
        
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
#{ 
#  Driver Code Starts
import sys

import sys
sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        obj = Solution()
        res = obj.printBoundaryView(root)
        for i in res:
            print (i, end = " ")
        print('')
# } Driver Code Ends