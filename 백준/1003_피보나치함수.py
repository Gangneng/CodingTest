call = int(input())
num = []

for _ in range(call):
    num.append(int(input()))

z = [1,0,1]
o = [0,1,1]


for i in num:
    while True:
        if len(z)-1<i:
            for _ in range(2, i):
                z.append(z[-2]+z[-1])
                o.append(o[-2]+o[-1])
        else:
            print(z[i], o[i])
            break
