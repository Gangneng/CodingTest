K, N = map(int, input().split())
lan = []

for i in range(K):
    lan.append(int(input()))

lo = 1
hi = max(lan)
mid = hi

while lo <= hi:
    mid = (lo+hi)//2
    total = sum([i//mid for i in lan])
    if total>=N:
        lo = mid+1
    else:
        hi = mid-1
        
print(hi)
