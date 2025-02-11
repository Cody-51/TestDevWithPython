# Python独自の組み込み関数

# abs() / 数値の絶対値を求める
print(abs(-3.5))
# divmod(a, b) / aをbで割った結果を（商, 余り）のタプルで返す
print(divmod(800, 3))
# max() / 最大値を求める
print(max(5, 9, 2, -3))
# min() / 最小値を求める
print(min(5, 9, 2, -3))
# pow(x, y) / xのy乗を求める
print(pow(10, 4))
# round(数値, 桁数) / 数値を指定の桁数に丸める。桁数を省略すると整数に丸める。
print(round(3.1415, 2))

# chr(整数) / 整数が示すUnicodeを文字列で返す
print(chr(25))
# ord(1文字) / 文字に対するUnicodeを調べる
print(ord("z"))
# len() / 文字列で文字数を求める
print(len("aaaa"))
# str() / 値を文字列に変換
print(str(89898))

# input() / キーボードからの入力を受け取る
input("文字を入力してください")
# open() / テキストファイルを開く
file = "/Users/cody/local_repository/TestDevWithPython/app/back/app.py"
open(file)