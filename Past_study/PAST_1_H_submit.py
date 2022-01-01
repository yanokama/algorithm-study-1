#TLEだったが、NG回答例として保存する。
N = int(input())
C = list(map(int, input().split()))
Q = int(input())
S = [list(map(int, input().split())) for _ in range(Q)]
#print(S)###
count = 0
for i in range(Q):
    if S[i][0] == 1:
        if ( C[S[i][1]-1] - S[i][2] ) >= 0:
            C[S[i][1]-1] -= S[i][2]
            count += S[i][2]
    elif S[i][0] == 2:#奇数全て->偶数全て
        flg = True
        for j in range(0, len(C), 2):
            if ( C[j] - S[i][1] ) < 0:
                flg = False
        if flg:
            for j in range(0, len(C), 2):
                C[j] -= S[i][1]
                count += S[i][1]
    elif S[i][0] == 3:
        flg = True
        for k in range(len(C)):
            if ( C[k] - S[i][1] ) < 0:
                flg = False
        if flg:
            for k in range(len(C)):
                C[k] -= S[i][1]
                count += S[i][1]
#    print(i, ':', C)###
print(count)
