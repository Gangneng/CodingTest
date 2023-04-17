def one_fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return one_fib(n-1)+one_fib(n-2)

def zero_fib(n):
    if n==0:
        return 1
    elif n==1:
        return 0
    else:
        return zero_fib(n-1)+zero_fib(n-2)
    

call = 2
num=[0, 1, 3]

for i in num:
    print(zero_fib(i), one_fib(i))
