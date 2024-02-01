# インデックスで文字列埋め込み
print('hoge is {0} {1}'.format(1, 2))

# 変数で文字列埋め込み
print('hoge is {hoge} {fuga}'.format(hoge=1, fuga=2))


# 変数で文字列埋め込み（最新の書き方）
hoge = 'stupid'
fuga = 'genious'
print(f"hoge is {hoge}")
print(f"fuga is {fuga}")
