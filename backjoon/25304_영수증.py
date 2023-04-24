X = int(input())
N = int(input())

total_cost = 0
for i in range(N):
    a, b = map(int, input().split())

    total_cost+=a*b

if X==total_cost:
    print('Yes')
else:
    print('No')
    
