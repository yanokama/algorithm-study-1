from collections import deque
H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

deq = deque()
deq.append([0,0]) #開始位置
maze[0][0] = 0 
dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]

while len(deq) > 0:
    h, w = deq.popleft()
    for i in range(4):
        next_h = h + dh[i]
        next_w = w + dw[i]
        if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W or maze[next_h][next_w] == '#':
            continue
        if  maze[next_h][next_w] == '.':
            deq.append([next_h, next_w])
            maze[next_h][next_w] = maze[h][w] + 1

count = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == '#':
            count += 1
if maze[H-1][W-1] == '.':
    print(-1)
else :
    dist = maze[H-1][W-1]
    ans =  H * W - ( dist + count ) - 1
    print(ans)
