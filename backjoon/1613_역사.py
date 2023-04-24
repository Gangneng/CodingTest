import sys
ip = sys.stdin.readline

n, k =map(int, ip().split())

history = [[0]*n for _ in range(n)]

for _ in range(k):
    f_case, s_case = map(int, input().split())
    history[f_case-1][s_case-1]=1


for i in range(n): # 중간
    for j in range(n): # 시작
        for k in range(n): # 끝
            if history[j][k]==0:
                if history[j][i] and history[i][k]:
                    history[j][k]=1

for _ in range(int(input())):
    f_case, s_case = map(int, ip().split())
    if history[f_case-1][s_case-1]:
        print(-1)
    elif history[s_case-1][f_case-1]:
        print(1)
    else:
        print(0)
