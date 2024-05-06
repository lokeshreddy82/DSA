class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bt:
    def solution(self,inorder,postorder):
        
inorder=[9,3,15,20,7]
postorder=[9,15,7,20]
b=bt()
print(b.solution(inorder,postorder))
