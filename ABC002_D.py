n, m = map(int, input().split())
#リスト作成
relations = [ [] for _ in range(n)]
for i in range(m):
  r1, r2 = map(int, input().split())
  relations[r1-1].append(r2-1)
  relations[r2-1].append(r1-1)
#print(relations)##

#全探索
ans = 1
for i in range(2**n):#全パターン
  num = 0
  flg_ng = False
  for j in range(n):
    if ((i >> j) & 1):
      num += 1
      for k in range(n):#メンバjについて他のメンバとの関係をチェック
        if not(k==j) and ((i >> k) & 1):
          if k not in relations[j]:
            flg_ng = True     
  if not(flg_ng):
    ans = max(num, ans)
print(ans)