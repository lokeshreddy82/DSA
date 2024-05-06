a=int(input("enter a value"))
b=int(input("enter a value"))
try:
    print(a/b)
except TypeError:
    print("its not wrong")
except ZeroDivisionError :
    print("Zero division error")
finally:
    print("lokesh reddy")
