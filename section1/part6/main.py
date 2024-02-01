s = 'My name is hoge.'

# 'My'で始まっているか確認
is_start = s.startswith('My')

# 指定した文字列のindexをreturn
point = s.find('name')  # 3

# 後ろから検索
point = s.rfind('name')

# 該当する文字の数を出力
print(s.count('is'))

print(s.title())  # 'My Name Is Hoge.'
