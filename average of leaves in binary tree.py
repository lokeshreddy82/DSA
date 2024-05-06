#average levels of a binary tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bt:
    def solution(self,root):
        res=[]
        if not root:
            return res
        ite=[(root)]
        ans=[]
        while ite:
            level=[]
            for i in range(len(ite)):
                node=ite.pop(0)
                level.append(node.data)
                if node.left is not None:
                    ite.append(node.left)
                if node.right is not None:
                    ite.append(node.right)
            res.append(level)
        for i in range(len(res)):
            ans.append(sum(res[i])/len(res[i]))
        return ans
n=node(3)
n.left=node(9)
n.right=node(20)
n.right.left=node(15)
n.right.right=node(7)
s=bt()
print(s.solution(n))
