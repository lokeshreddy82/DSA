class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class linking:
    def __init__(self):
        self.head=None
    def addf(self,data):
        n=Node(data)
        if self.head==None:
            self.head=n
        else:
            n.next=self.head
            self.head.prev=self.head
            self.head=n
    def addl(self,data):
        n=Node(data)
        if self.head==None:
            self.head=n
        else:
            t=self.head
            while t.next:
                t=t.next
            t.next=n
            n.prev=t
    def delf(self):
        if self.head==None:
            print("isempty")
        elif self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None
    def dell(self):
        if self.head==None:
            print("isempty")
        elif self.head.next is None:
            self.head=None
        else:
            t=self.head
            while t.next:
                t=t.next
                t.prev.next=None
                t.prev=None
    def display(self):
        t=self.head
        while t:
            print(t.data,end="---->")
            t=t.next
l=linking() 
l.addf(10)
l.addf(20)
l.addf(30)
l.addf(40)
l.delf()
l.dell()
l.display()

