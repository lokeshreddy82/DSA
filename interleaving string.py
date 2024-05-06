#interleaving string
class solution:
    def answer(self,s1,s2,s3):
        k=""
        l=2
        r=len(s3)
        while l<=r:
            if l==2:
                k +=s1[0:l]+s2[0:l*2]
                l+=2
            else:
                k +=s1[l-2:l]+s2[(l-2)*2:l*2]
                l+=2
        if k==s3:
            return True
        elif len(s1)==len(s3):
            return True
        return False
s1="a"
s2=""
s3="a"
s=solution()
print(s.answer(s1,s2,s3))
