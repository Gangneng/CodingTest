N, B = input().split()

B = int(B)

num = {}

for i in range(26):
    num[chr(ord('A')+i)]=10+i

N = N[::-1]

answer = 0

for i in range(len(N)):
    if N[i] in num.keys():
        answer+=num[N[i]]*B**i
    else:
        answer+=int(N[i])*B**i
print(answer)
