class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bt:
    def zigzaglevelorderTraversal(self,root):
        if not root:
            return []
        lokesh=[(root)]
        res=[]
        ans=1
        while lokesh:
            level=[]
            for i in range(len(lokesh)):
                node=lokesh.pop(0)
                level.append(node.data)
                if node.left is not None:
                    lokesh.append(node.left)
                if node.right is not None:
                    lokesh.append(node.right)
                if ans%2!=0:
                    level.reverse()
            ans +=1
            res.append(level)
        return res
n=node(1)
n.left=node(2)
n.right=node(3)
n.left.left=node(4)
n.left.left.left=node(5)
s=bt()
print(s.zigzaglevelorderTraversal(n))
