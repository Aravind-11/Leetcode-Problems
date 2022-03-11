class MyStack(object):

    def __init__(self):
        self.arr=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.arr.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.arr.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if not len(self.arr):
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()