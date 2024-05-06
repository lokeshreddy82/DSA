class solution:
    def answer(self,s,k):
        res=[]
        rev=s[::-1]
        st=""
        an=0
        low=0
        high=len(s)-1
        while low<=high:
            n=s.count(s[low])
            if s[low] not in res and n>=k:
                res.append(s[low])
                an +=n
                low +=1
            low +=1
        return an
s="aaabb"
k=3
l=solution()
print(l.answer(s,k))
        
                
