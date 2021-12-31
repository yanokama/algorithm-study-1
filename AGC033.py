from collections import deque
H, W = map(int, input().split())
board = [list(input()) for _ in range(H)]

q = deque()
for i in range(H):
    for j in range(W):
        if board[i][j] == '#':
            q.append( [ i, j] )
            board[i][j] = 0 #距離を0にする
#右下左上
dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]
ans = 0
while len(q) > 0:
    h, w = q.popleft()
    for k in range(4):
        next_h = h + dh[k]
        next_w = w + dw[k]
        if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
            continue
        if board[next_h][next_w] == '.':
            q.append([next_h, next_w])
            board[next_h][next_w] = board[h][w] + 1
            ans = max(ans, board[h][w] + 1)
print(ans)

