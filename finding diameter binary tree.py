class bt:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class binarytree:
    def diameter(self,root):
        if not root:
            return 0
        return self.lef(root.left)+self.ref(root.right)+1
    def lef(self,root):
        if not root:
            return 0
        left=self.lef(root.left)
        right=self.lef(root.right)
        return max(left,right)+1
    def ref(self,root):
        if not root:
            return 0
        left=self.ref(root.left)
        right=self.ref(root.right)
        return max(left,right)+1
       
b=bt(1)
b.left=bt(2)
b.right=bt(3)
b.left.left=bt(5)
b.left.right=bt(4)
s=binarytree()
print(s.diameter(b))
