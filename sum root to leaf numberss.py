class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class binarytree:
    def __init__(self):
        self.arr=[]
    def sum_root_to_leaf_numbers(self,root):
        if not root:
            return
        def dfs(root,st):
            if not root:
                return
            st +=str(root.data)
            if root.left==None and root.right==None:
                self.arr.append(st)
            dfs(root.left,st)
            dfs(root.right,st)
        st=""
        dfs(root,st)
        currsum=0
        for i in range(len(self.arr)):
            currsum +=int(self.arr[i])
        return int(currsum)
n=node(4)
n.left=node(9)
n.right=node(0)
n.left.right=node(1)
b=binarytree()
print(b.sum_root_to_leaf_numbers(n))
