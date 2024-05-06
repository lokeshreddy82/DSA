class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # x is the start of array nums, so minus n by 1 
        n -= 1
        binary_x = list(bin(x)[2:])
        binary_n = list(bin(n)[2:])
        print(binary_n)
        cur_n = len(binary_n) - 1
        # Step 1 & 2: traverse reversely, filling all binary_n bits into 0 bits in x
        for i in range(len(binary_x)-1, -1, -1):
            # leave bits of 1 alone
            if binary_x[i] == "1": continue
            binary_x[i] = binary_n[cur_n]
            cur_n -= 1
            # if there is no binary_n bit left   
            if cur_n == -1: break
        # Step 3: if n bits left, fill the left binary_n to the head of x
        if cur_n >= 0:
            binary_x = binary_n[0:cur_n+1] + binary_x
        # Finally just convert result to integer
        print(binary_x)
        return int("".join(binary_x), 2)
s=Solution()
print(s.minEnd(10,4))