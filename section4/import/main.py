# importの書き方はいくつかあるがメソッド指定でのimportは非推奨（エラーやバグの原因）
# import lessson.utils
# from lesson imoprt utils
# from lesson.utils import method

# エイリアスも使えるが非推奨。よほど長い場合のみ使用したほうがいい
# from lesson imoprt utils as u


# これでstring内にある各文字をキー、数をvalueとした辞書ができる
from collections import defaultdict
dict = defaultdict(int)
string = 'fjaoisnvaoiejfioqa'

for i in string:
  dict[i] += 1
print(dict)
