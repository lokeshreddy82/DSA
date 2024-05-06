
import heapq as hq
# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
hq.heapify(li)

# printing created heap
print("The created heap is:", li)
hq.heappush(li,10)
hq.heappush(li,-10)
print(li)
hq.heappop(li)
minn=hq.heappop(li)
print(li)
print(minn)
l1=[1,3,5,7,-1]
l2=[4,6,7,2,9,0]
hq.heapify(l1)
hq.heapify(l2)
print(l1,l2)
res=hq.heappushpop(l1,20)
print(l1)
print(res)
print(hq.heapreplace(l1,8))
print(l1)
print(hq.nlargest(4,l1)[-1])
print(l1)
print(hq.nsmallest(1,l1))
#They are limites functions in python
#heapify,heappush,headppop,heappushpop,headpreplace,heap.nlargest,heap.nsmallest
