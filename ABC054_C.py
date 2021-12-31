#帰りがけの処理が抜けていたハマった。
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


ans = 0
def g_search(num , count, reached):
    global graph ,ans
    reached[num] = True
    count += 1
    if count == N: #全て訪問した場合
      #print(num, count, reached, '@@@') ###
      ans += 1
    for j in range(len(graph[num])):
        if not(reached[graph[num][j]]):
            g_search(graph[num][j], count, reached)
    #帰りがけに訪問済み、カウントを戻す        
    count -= 1
    reached[num] = False

for i in range(len(graph[0])):
  reached = [False] * N
  reached[0] = True
  g_search(graph[0][i], 1, reached)

print(ans)

