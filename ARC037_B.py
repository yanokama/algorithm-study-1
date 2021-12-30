#自力で解けなかったので、後日再チャレンジ
#行きがけ順で過去に訪れた場所に再度訪れる場合、それは閉路と判定される

def dfs(now, prev):
    global flag
    #今いる頂点からいける頂点を順にnextに入れてループ
    for next in g[now]:
        if next != prev:
            if memo[next]:
                #過去に訪れていれば閉路
                flag = False
            else:
                memo[next] = True
                dfs(next, now)

n, m = map(int, input().split())
#隣接リストを作成
g = [[] * n for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

#訪問済み塗りつぶし用
memo = [False for _ in range(n)]

ans = 0
#頂点をループ
for i in range(n):
    if not memo[i]:
        flag = True
        dfs(i, -1)
        if flag:
            ans += 1
print(ans)


