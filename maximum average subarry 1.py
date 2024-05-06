#finding maximum average subarray
class solution:
    def findaverage(self,nums,k):
        low=1
        avr=sum(nums[:k])/k
        for i in range(k+1,len(nums)+1):
            avr=max(avr,sum(nums[low:i])/k)
            low +=1
        return avr
nums=[1,12,-5,-6,50,3]
k=4
s=solution()
print(s.findaverage(nums,k))
            
