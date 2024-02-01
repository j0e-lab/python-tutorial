# 文字列の変数からindexを指定して文字を取得できる
word = 'python'
print(word[0]) # pが出力される
print(word[-1]) # 最後のnが出力される

# インデックスの始点と終点を指定して取得（スライス）
print(word[0:2]) # py
print(word[:2]) # 0は省略できる

# 文字の置換
word = 'j' + word[1:] # jython

# 文字列の長さ
n = len(word)
