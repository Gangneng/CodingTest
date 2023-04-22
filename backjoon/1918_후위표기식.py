exp = input()

stack = []
answer = ''

for i in exp:
    if i =='(':
        stack.append(i)
    elif i==')':
        while stack[-1]!='(':
            answer+=stack.pop(-1)
        stack.pop(-1)
    elif i=='*' or i=='/':
        if len(stack)!=0:
            if stack[-1]=='*' or stack[-1]=='/':
                answer+=stack.pop(-1)
        stack.append(i)
    elif i=='+' or i=='-':
        if len(stack)!=0:
            while len(stack)!=0:
                if stack[-1]!='(':
                    answer+=stack.pop(-1)
                else:
                    break
        stack.append(i)
    else:
        answer+=i

while len(stack)!=0:
    answer+=stack.pop(-1)
    
print(answer)
