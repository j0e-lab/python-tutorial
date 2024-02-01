i = [1, 2, 3, 4, 5]

# iと同じ値を持った別の参照がcopyに代入される
copy = i.copy()

# 同じ参照
j = i

# idメソッドはオブジェクトに割り振られたidをreturn。下記は同じIDが入っている
print(id(i))
print(id(j))
