#User function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        # Code here
        def print_ele(x):
            while x:
                print (x.data,end=' ')
                x=x.next
        x=head
        a1='aeiouAEIOU'
        vowel_start=vowel_end=c_start=c_end=None
        while head:
            cur=head.data
            if cur in a1:
                if not vowel_start:
                    vowel_start=head
                    vowel_end=vowel_start
                else:
                    vowel_end.next=head
                    vowel_end=vowel_end.next
            else:
                if not c_start:
                    c_start=head
                    c_end=c_start
                else:
                    c_end.next=head
                    c_end=c_end.next
            head=head.next
        if not vowel_start or not c_start:
            print_ele(x)
            return
        vowel_end.next=c_start
        c_end.next=None
        print_ele(vowel_start)

#{ 
#  Driver Code Starts


# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)

# } Driver Code Ends