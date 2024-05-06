#Third maximum number
#Input: nums = [3,2,1]
#Output: 1
def lokesh(inputt):
    listt=list(set(inputt))
    maximum=[]
    listt.sort()
    if len(listt)==2:
        return max(listt)
    k=listt[::-1]
    return k[2]
inputt=[3,2,1]
print(lokesh(inputt))
