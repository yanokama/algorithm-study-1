# qiita　@__poweller__　さんの記事
def permutations(my_list):
    if len(my_list) == 1:
        return [my_list]                                      # 1. 要素数1の順列を返す
    else:
        result = []                                     # 順列の組を保存しておくためのリスト
        for i, val in enumerate(my_list):                     # 1. 数字の組から1つ取り出す
            rest = permutations(my_list[:i] + my_list[i+1:])  # 2. 残りの数字の組から順列の組を作る
            for rest_perm in rest:
                perm = [val] + rest_perm                      # 3. 求まった順列の先頭に1で取り出した数字をくっつける
                result.append(perm)
        return result                                   # 順列の組を返す

if __name__ == "__main__":
    my_list = [1, 2, 3]
    perms = permutations(my_list)

    print(perms)