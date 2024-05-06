n=int(input(""))
res=0
for i in range(n):
    inp=input("")
    if inp[0]=="+" or inp[1]=="+":
        res +=1
    else:
        res -=1
print(res)
