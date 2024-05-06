def merge(left,right):
    merged=[]
    i=0
    j=0
    while len(left)>i and len(right)>j:
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])  
            j+=1
    merged+=left[i:]+right[j:]
    return merged
def mergesort(array):
    if len(array)==1:
        return array
    mid=len(array)//2
    left=mergesort(array[:mid])
    right=mergesort(array[mid:])
    return merge(left,right)
array=[4,2,1,6,7]
result=mergesort(array)
print(result)
