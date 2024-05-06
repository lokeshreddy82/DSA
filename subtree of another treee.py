class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class sub:
    def solution(self,root,subtree): 
        if not root and not subtree:
            return True
        if root.data==subtree:
            return self.dfs(root,subtree)
        self.solution(root.left,subtree)
        self.solution(root.right,subtree)
    def dfs(self,root,subtree):
        if not root and not subtree:
            return True
        if root!=subtree:
            return False
        return self.dfs(root.left,subtree.left) and self.dfs(root.right,subtree.right)
n=node(3)
n.left=node(4)
n.right=node(5)
n.left.right=node(2)
n.left.left=node(1)
s=node(4)
s.left=node(1)
s.right=node(2)
p=sub()
print(p.solution(n,s))
