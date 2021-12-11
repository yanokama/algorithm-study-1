#arc029_A
#git test
#git test2
n = int(input())
t = [int(input()) for _ in range(n)]
result = -1
for i in range(2**n):
  a = 0
  b = 0  
  for j in range(n):
    if ((i >> j) & 1):
      a += t[j] 
    else:
      b += t[j]
  
  if result == -1 or result > max(a, b):
    result = max(a, b)
print(result)