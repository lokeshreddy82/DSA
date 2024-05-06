t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = input().strip()
    b = input().strip()
    
    i, j = 0, 0
    
    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
        j += 1
    
    # i is the number of characters from a that we could match in b as a subsequence
    print(i)
