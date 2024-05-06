class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bt:
    def __init__(self):
        self.arr=[]
        self.ans=""
    def twosum(self,root,k):
        if not root:
            return
        res=[]
        for i in range(len(self.arr)):
            if self.arr[i]+root.data==k:
                res.append("True")
        self.arr.append(root.data)
        self.twosum(root.left,k)
        self.twosum(root.right,k)
n=node(5)
n.left=node(3)
n.right=node(6)
n.left.left=node(2)
n.left.right=node(4)
n.right.right=node(7)
k=9
b=bt()
print(b.twosum(n,k))
