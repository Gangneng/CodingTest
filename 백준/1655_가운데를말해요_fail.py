import heapq

T = int(input())
left = []
right = []

for i in range(T):
    N = int(input())
    if len(left)==len(right):
        heapq.heappush(left, (-N, N))
    else:
        heapq.heappush(right, (N, N))

    if right and left[0][1]>right[0][0]:
        min=heapq.heappop(right)[0]
        max=heapq.heappop(left)[1]

        heapq.heappush(left, (-min, min))
        heapq.heappush(right, (max, max))
    print(left, right)
    print(left[0][1])
    
    
