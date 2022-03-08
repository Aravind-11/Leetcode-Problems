# your task is to complete this function
# function should return a list of the
# two new heads
def mergeList(head1, head2):
    # Code here
    list1_start=list2_start=list1_end=list2_end=None
    x=head1
    y=head2
    while x and y:
        if not list1_start:
            list1_start=x
            list1_end=list1_start
        else:
            list1_end.next=list2_end
            list1_end=x
        if not list2_start:
            list2_start=y
            list2_end=list2_start
        else:
            list2_end.next=x
            list2_end=y
        x=x.next
        y=y.next
    list1_end.next=list2_end
    head2=list2_end.next
    list2_end.next=None
    
    if y:
        list1_end.next=list2_end
    if x:
        list1_end.next=list2_end
        list2_end.next=x
    
    
    return [head1, head2]

#{ 
#  Driver Code Starts
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node
        
def printList(head):
    while head:
        print(head.data, end=' ')
        head=head.next
    print()

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head2 = createList(arr, n)
        head = mergeList(head1, head2)
        printList(head[0])
        printList(head[1])
# Contributed by: Harshit Sidhwa

# } Driver Code Ends