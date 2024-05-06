#queue
class lokesh:
    def __init__(self,maxx):
        self.data=[]
        self.maxx=maxx
    def enqueue(self,items):
        self.data.insert(0,items)
    def dequeue(self):
        self.data.pop()
    def isempty(self):
        if self.data:
            return len(self.data)
        else:
            return "empty"
g=lokesh()
g.enqueue(10)
g.enqueue(20)
print(g.isempty())




        
    
        
