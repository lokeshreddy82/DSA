class Solution(object):
    def diagonalSum(self, mat):
        countt=0
        if len(mat)<2:
            return mat
        for i in range(len(mat)):
            countt +=mat[1][i]
        for j in range(len(mat)-1,-1,-1):
            countt +=mat[1][j]
        if len(mat)<=3:
            countt -=mat[2][2]
            return countt
        else:
            return countt
a=Solutio
