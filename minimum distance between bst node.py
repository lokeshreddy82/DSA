class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.arr=[]
    def distance(self,root):
        if not root:
            return 0
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.arr.append(root.data)
            dfs(root.right)
        dfs(root)
        if len(self.arr)>=2:
            return abs(self.arr[1]-self.arr[0])    
n=node(4)
n.left=node(2)
n.right=node(6)
n.left.left=node(1)
n.left.right=node(3)
s=bst()
print(s.distance(n))
