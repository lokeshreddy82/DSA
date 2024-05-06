n=int(input(""))
res=[]
for i in range(n):
    size=int(input(""))
    arr=input()
    if arr.count("1")%2!=0:
        print("NO")
    elif arr.count("1")==2 and "11" in arr:
        print("NO")
    else:
        print("YES")
