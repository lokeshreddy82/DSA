n=int(input(""))
res=[]
for i in range(n):
    every=[]
    t=int(input(""))
    normal=True
    prev=normal
    for j in range(t):
        st=""
        col=prev
        for k in range(t):
            if col:
                st +="##"
                col=False
            else:
                st +=".."
                col=True
        every.append(st)
        every.append(st)
        if prev:
            prev=False
        else:
            prev=True
    res.append(every)
for i in res:
    for j in i:
        print(j)
