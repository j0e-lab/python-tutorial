# 引数と返り値に型を指定した関数定義
def add_num(a: int, b: int) -> int:
    print(a, b)


# これなんとエラーにならずに普通に出力される（型指定してる意味、、）
r = add_num("a", "b")


# 基本的なメソッド宣言。渡した引数の通りの順番に使用する必要がある
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)


# キーワード指定での宣言（キーワード指定の場合、処理の順番関係なく使用できる）
def menu(entree="beef", drink="juice", dessert="ice"):
    print(entree)
    print(drink)
    print(dessert)


# NOTE デフォルト引数に空のlistを渡してはいけない最初に生成されたlistを常に参照するため


# 引数が多い場合は以下のように省略することができる（argsはタプル）
def hello(*args):
    for arg in args:
        print(arg)


# メソッドに対してhelpを実行するとメソッドのdoc（コメント）が出力される
help(hello)
# これでも上と同じことできる
hello.__doc__

"""
# クロージャー
関数の中に関数を定義し、実行タイミングをコントロールすることができる。
javaのabstractみたいな共通処理があるけど扱いたい値が微妙に違うみたいなときに使えそう
"""


# @helloはデコレーター。hogeが実行されるときにhogeをhelloメソッドの引数に渡して処理が実行される。
@hello
def hoge(a, b):
    return a + b


# ラムダ（要は無名関数。関数定義不要で関数っぽい動きができる。2行ぐらいの簡素なメソッドなら有効）

"""
# ジェネレータ
listのように再起処理できるが、一度に要素をすべてメモリに読み込まない分メモリの節約にはなる。
listとの違いとしてはループ中に処理の遅延ができる
"""

"""
リストの内包表記
以下の記述をすることでタプルからリストへの変換が1行でできる
記載も短いし処理も速いらしい
条件が複数あったりforのネストが深い場合は可読性落ちる
"""
nums = (1, 2, 3, 4, 5)
list = [i for i in nums if i % 2 == 0] // [2, 4]

animal = "cat"

# locals()やglobals()で変数のスコープを確認できる
