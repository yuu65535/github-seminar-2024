# doctestの練習(テストケース)
# 関数is_leap_yearを考えてみましょう
# この関数は、引数で受け取った年がうるう年かどうかを判定する関数です
# うるう年の条件は以下の通りです
# 1. 西暦が4で割り切れる年はうるう年
# 2. ただし、西暦が100で割り切れる年はうるう年ではない
# 3. ただし、西暦が400で割り切れる年はうるう年


def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False


# いわゆるFizzBuzz問題
# 指定された数値までの数値の結果をリストで返しましょう
# ルール: 3の倍数は'fuzz'、5の倍数は'buzz'、3と5の倍数は'fizzbuzz'とする
# それ以外の値は数値を文字列にして返す(list[str]となる)
# fb_list(5) -> ['1', '2', 'fizz', '4', 'buzz']


def fb_list():
    pass
