class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class solution:
    def __init__(self):
        self.arr=[]
    def right_side(self,root):
        if not root:
            return self.arr
        self.arr.append(root.data)
        self.right_side(root.right)
        return self.arr
p=Node(1)
p.right=Node(2)
s=solution()
print(s.right_side(p))
                
        
