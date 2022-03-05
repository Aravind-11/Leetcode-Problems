"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverse(self,head, k):
        # Code here
        def reverse_list(y,c):
            c=c[::-1]
            for i in c:
                y.data=i
                y=y.next
                if not y:
                    return 
        x=head
        i=0
        c=[]
        y=None
        while x:
            
            i+=1
            c.append(x.data)
            if i%k==1:
                y=x
            if i%k==0 and y:
                reverse_list(y,c)
                c=[]
                
            x=x.next
        x=head
        
        n=i-i%k+1
        c=0
        ele=[]
        while x:
            c+=1
            if c==n:
                y=x
            if c>=n:
                ele.append(x.data)
            x=x.next
        reverse_list(y,ele)
        
        
        return head

#{ 
#  Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends