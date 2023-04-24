n, m = map(int, input().split())

arr = []

for i in range(n):
    ele = input()
    eles =[]
    for j in ele:
        eles.append(int(j))
    arr.append(eles)

answer = 0

if n!=1 and m!=1:
    for i in range(1, n):
        if 1 in arr[i] and answer==0:
            answer=1
        for j in range(1, m):
            if arr[i][j]==1:    
                arr[i][j]=min(arr[i-1][j-1], arr[i][j-1], arr[i-1][j])+1
                if arr[i][j]>answer:
                    answer = arr[i][j]

else:
    for i in arr:
        if 1 in i:
            answer= 1

print(answer**2)
