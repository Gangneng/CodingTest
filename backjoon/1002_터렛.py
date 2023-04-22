import math

T = int(input())
testcase = [[0,0,13,40,0,37],[0,0,3,0,7,4],[1,1,1,1,1,5]] 

for test in testcase:
    d = math.sqrt((test[0]-test[3])**2+(test[1]+test[4])**2) # 두 중심점 사이 거리
    p_case = test[2]+test[5]
    m_case = abs(test[2]-test[5])
    if d==0:
        if test[2]!=test[5]:
            print(0)
        else:
            print(-1)
    else:
        if p_case>d>m_case:
            print(2)
        elif p_case == d or m_case == d:
            print(1)
        else:
            print(0)
