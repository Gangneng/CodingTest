nums = [18, 4, 6, 9, 11]

for num in nums:
    answer = [num//5, num%5//3]
    flag = -1

    while answer[0]>=0:
        if answer[0]*5+answer[1]*3==num:
            flag=1
            print(sum(answer))
            break
        else:
            answer[0] = answer[0]-1
            answer[1] = (num-answer[0]*5)//3

    if flag==-1:
        print(-1)

