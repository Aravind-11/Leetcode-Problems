class LRUCache:

    def __init__(self, capacity):
        self.dict={}
        self.capacity=capacity
        self.list=[]

    def get(self, key):
        res=self.dict.get(key,-1)
        if res!=-1:
            
            self.list.remove(key)
            self.list.append(key)
        return res
        
        
    def put(self, key, value):
        if self.dict.get(key,-1)!=-1:
            self.dict[key]=value
            self.list.remove(key)
            self.list.append(key)
        else:
            if len(self.dict.keys())+1<=self.capacity:
                self.dict[key]=value
                self.list.append(key)
            
            else:
                del self.dict[self.list[0]]
                self.list.pop(0)
                self.dict[key]=value
                self.list.append(key)
        

        
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)