from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    str_arr = input()
    arr = deque(str_arr[1:-1].split(',')) if str_arr!='[]' else deque([])
    result = ""
    rev = 0
    for i in p:
        if i=='R':
            rev+=1
        if i=='D':
            if arr:
                if rev%2==1:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                result = "error"

    if result == "":
        if rev%2==1:
            arr.reverse()
        result+='['
        for i in range(len(arr)):
            result+=str(arr[i])
            if i!=len(arr)-1:
                result+=','
        result+=']'
        print(result)
    else:
        print(result)
