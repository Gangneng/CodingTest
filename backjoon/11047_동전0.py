N, K = map(int, input().split())

coins = []
answer = 0

for i in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

for i in coins:
    answer+=K//i
    K = K%i

print(answer)
