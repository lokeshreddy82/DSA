m=int(input(""))
while m:
   n=int(input(""))
   target=input("")
   ans=True
   up_countt=target.count("U")
   down_countt=target.count("D")
   if up_countt==0 or down_countt==0:
      print("No")
   else:
      array=list(target)
      for i in range(n):
         if len(array)==2:
            if ans:
               ans=False
            else:
               ans=True
            break
         elif up_countt==0 or down_countt==0:
            ans=False
            break
         else:
            if ans:
               p=array.pop(0)
               if p=="U":
                  p="D"
                  down_countt +=2
                  up_countt  -=1
               else:
                  p="U"
                  down_countt -=1
                  up_countt +=2
               array[0]=p
               array[-1]=p
               ans=False
            else:
               ans=True
               p=array.pop()
               if p=="U":
                  p="D"
                  down_countt +=2
                  up_countt  -=1
               else:
                  p="U"
                  down_countt -=1
                  up_countt +=2
               array[0]=p
               array[-1]=p
               ans=True
      if ans:
         print("Yes")
      else:
         print("No")
   m -=1