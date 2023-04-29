A, P = map(int, input().split())
D = {}
D[A] = 1

def dfs(A, P, D):
    flag = 0
    for i in str(A):
        flag+=int(i)**P

    if flag in D.keys():
        print(D[flag]-1)
        return 
    else:
        D[flag]=D[A]+1
        dfs(flag, P, D)

dfs(A, P, D)