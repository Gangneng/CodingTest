N = input()
if '0' not in str(N) or sum([int(i) for i in N])%3!=0:
    print(-1)

else:
    print(''.join(sorted(str(N), reverse=True)))

    
    

