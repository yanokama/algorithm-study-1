#ABC 054　C問題を順列で解く別解。
#順列のライブラリはあえて使用しない
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

#順列を求める関数
def permutations(my_list):
    if len(my_list) == 1:
        return [my_list]
    else:
        result = [] #求めた順列を格納する配列
        for i, val in enumerate(my_list):
            #ループの値を除いた配列を渡す
            # スライスだとインデックスエラーが起きないので便利!
            rest = permutations( my_list[:i] + my_list[i+1:] )
            for rest_elem in rest:
                perm = [val] + rest_elem
                result.append(perm)
        return result

n_list = list(range(0,N,1))
perms = permutations(n_list[1:])
count = 0
for k in range(len(perms)):
    flg = True
    for l in range(N-1):
        #1番めの要素は0と接続している必要がある
        if l == 0:
            if perms[k][l] not in graph[0]:
                flg = False
                break
         #同様にn番目の要素はn-1番目の要素と接続している必要がある
        elif perms[k][l] not in graph[perms[k][l-1]]:
            flg = False
            break
    if flg:
        count += 1
print(count)



