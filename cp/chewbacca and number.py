n=input("")
listt=[int(i) for i in n]
for i in range(len(listt)):
    s=9-listt[i]
    if s==0 and i==0:
        continue
    elif s<listt[i]:
        listt[i]=s
res=0
for j in listt:
    res=res*10+j
print(res)
