# 辞書の基本的な宣言。ちなみにkeyは数値でも可能
d = {'x': 10, 'y': 20}
d2 = dict(a=100, b=200)

print(d['x']) // 10

# keyを含んだリストをreturn
d.keys()

# valueを含んだリストをreturn
d.values()

# dのvalueをd2で上書き
d.update(d2)



