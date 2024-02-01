hoge = True

if hoge:
	print('hoge')

# Javaでいうところのnull
is_none = None

if is_none is None: # ==での判定は望ましくない（pythonでも数値の比較のみイコールで比較するのかも、、、）
	print('none')

# isはオブジェクトの型動詞の比較をしてるっぽい
print(1 == True) # True
print(1 is True) # False

