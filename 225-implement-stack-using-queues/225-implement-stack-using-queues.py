class MyStack(object):

    def __init__(self):
        self.queue=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.insert(0,x)

    def pop(self):
        """
        :rtype: int
        """
        if not len(self.queue):
            return 
        x=self.queue[0]
        del self.queue[0]
        return x
        
    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        if not len(self.queue):
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()