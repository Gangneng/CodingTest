T = int(input())

num = []
for _ in range(T):
    num.append(int(input()))

num = sorted(num)

for i in num:
    print(i)
