import sys
ip = sys.stdin.readline

N = int(input())
M = int(input())

maps = [[0]*N for _ in range(N)]

for _ in range(M):
    f, s = map(int, input().split())
    maps[f-1][s-1]=1
    maps[s-1][f-1]=-1

for i in range(N): # 중간
    for j in range(N): # 시작
        for k in range(N): # 끝
            if maps[j][k]==0:
                if maps[j][i]+maps[i][k]==2:
                    maps[j][k]=1
                elif maps[j][i]+maps[i][k]==-2:
                    maps[j][k]=-1

    
for i in range(N):
    print(maps[i].count(0)-1)
