#回答の写経
N, L =map(int, input().split())
X = list(map(int, input().split()))
T1, T2, T3 = map(int, input().split())

#ハードルがある座標においてTrueとなるような配列
H = [False] * (L+1)
for x in X :
    H[x] = True

#cost[i]:座標iで行動を終了するまでの最小所要時間 
cost = [10**100] * (L+1) 
cost[0] = 0

#cost[1]より順に最小を求めていく
for i in range(1, L+1):
    #行動1
    cost[i] = min(cost[i], cost[i-1] + T1) ##これ、min無くても良い気がする
    #行動２
    if i >= 2:
        cost[i] = min(cost[i], cost[i-2] + T1 + T2)
    #行動3
    if i >= 4:
        cost[i] = min(cost[i], cost[i-4] + T1 + 3*T2)
    #移動した先にもしハードがあれば加算
    ##直感ではわかりにくかった部分（問題文を整理しよう）
    if H[i]:
        cost[i] += T3

#答えは座標Lにピッタリ止まるか、座標（L-3）～（L-1）からジャンプ中にゴールしたもの
##ジャンプ中にゴールした場合は走るのは0.5、ジャンプはx.5になる。
##ジャンプする距離を直に[0.5、1.5、2.5]としてしまっても良い気もするが、
##マジックナンバーを避けて考え方を式に表したと思われる。
ans = cost[L]
for i in [L-3, L-2, L-1]:
    if i >= 0:
        ans = min(ans, cost[i] + T1//2 + T2*(2*(L-i)-1)//2)
print(ans)


