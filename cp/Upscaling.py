n=int(input(""))
res=[]
for i in range(n):
    every=[]
    t=int(input(""))
    e=1
    prev=True
    for j in range(t):
        st=""
        for k in range(t):
            if prev:
                st +="##"
                prev=False
            else:
                st +=".."
                prev=True
        every.append(st)
        every.append(st)
        print(st)
        if e==1:
            prev=False
            e==0
        else:
            prev=True
            e==1
    res.append(every)
print(res)
            
        
