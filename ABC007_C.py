import queue
H, W = map(int, input().split())
sh, sw = map(int, input().split())
gh, gw = map(int, input().split())

maze = [list(input()) for _ in range(H)]
q = queue.Queue()
q.put([sh-1, sw-1]) # スタート地点を追加
maze[sh-1][sw-1] = 0 #スタート地点の距離
h_shift = [0, 1, 0, -1 ]
w_shift = [1, 0, -1, 0 ]
dist = 0
while not(q.empty()):
    h, w = q.get()
    dist = maze[h][w] + 1 
    for i in range(4):        
        next_h = h + h_shift[i]
        next_w = w + w_shift[i]        
        if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W or maze[next_h][next_w] != '.':
            continue
        if maze[next_h][next_w] == '.':
            maze[next_h][next_w] = dist
            q.put([next_h, next_w])

# print()            
# for i in range(H):
#     for j in range(W):
#         print(maze[i][j], end='')
#     print()

print(maze[gh-1][gw-1])





    
