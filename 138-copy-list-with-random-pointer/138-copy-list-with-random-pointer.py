"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        a={}
        x=head
        c=0
        while x:
            c+=1
            a[x]=c
            x=x.next
        b={}
        x=head
        c=0
        while x:
            c+=1
            if x.random:
                b[c]=a[x.random]
            else:
                b[c]=None
            x=x.next
    
        
        x=head
        y=Node(0)
        z=y
        c=0
        f={} 
        

        while x:
            c+=1
            
            y.next=Node(x.val)
            y=y.next
            f[c]=y
            x=x.next
        z1=z.next
        c=0
        while z1:
            c+=1
            if not b[c]:
                z1.random=None
            else:
                z1.random=f[b[c]]
            z1=z1.next
        return z.next
        