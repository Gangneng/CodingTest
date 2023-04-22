n= int(input())

fibo = [0,1]

if n==0:
    print(0)
elif n==1:
    print(1)

else:
    while(len(fibo)!=n+1):
        fibo.append(fibo[-1]+fibo[-2])

    print(fibo[-1])
