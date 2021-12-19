import sys
sys.setrecursionlimit(2000000)
islands = [list(input()) for _ in range(10)]
count_org = 0
for i in range(10):
    for j in range(10):
        if islands[i][j] == 'o':
            count_org += 1

def dfs(h, w):
    if h < 0 or 10 <= h or w < 0 or 10 <= w or islands[h][w] == 'x':
        return
    if reached[h][w] == 1:
        return
    reached[h][w] = 1

    dfs(h, w+1 ) #right
    dfs(h, w-1 ) #left
    dfs(h-1, w ) #up
    dfs(h+1, w ) #down

for i in range(10):
    for j in range(10):
        flg_add = False
        count_sim = 0
        reached = [[0]*10 for _ in range(10)] 
        if islands[i][j] == 'x':
            flg_add = True
            count_org += 1
            islands[i][j] = 'o'
        reached[i][j] = 1    
        dfs(i, j+1)
        dfs(i, j-1)
        dfs(i-1, j)
        dfs(i+1, j)         
        for k in range(10):
            for l in range(10):
                if reached[k][l] == 1:
                    count_sim += 1
        if count_sim == count_org :
            print('YES')
            exit()
        if flg_add:
            count_org -= 1
            islands[i][j] = 'x'
print('NO')


