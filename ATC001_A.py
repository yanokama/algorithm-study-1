import sys
sys.setrecursionlimit(1000000)
h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]
reached = [[False]*w for _ in range(h)]

def root_search(y, x):
  if x < 0 or w <= x or y < 0 or h <= y or maze[y][x] =='#':
    return
  if reached[y][x]:
    return  
  if maze[y][x] == 'g':
    print('Yes')
    exit()
    
  reached[y][x] = True
  root_search( y, x + 1 ) #右
  root_search( y, x - 1 ) #左
  root_search( y + 1, x ) #下
  root_search( y - 1, x ) #上  

sy = 0
sx = 0 
gy = 0
gx = 0 

for i in range(h):
  for j in range(w):
    if maze[i][j] == 's':
      sy = i
      sx = j
  
root_search(sy, sx)
print('No')    