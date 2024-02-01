r = [1, 2, 3, 4, 5, 6, 7]

# sort
r.sort()
r.sort(reverse=True)
r.reverse()  # 上行とやってること同じ

# 空白を区切りにそれぞれの文字列を配列に格納
s = 'my name is hoge'
arr = s.split(' ')
print(s.split(' '))

# 逆に空白文字でlistの要素を結合
x = ' '.join(arr)
