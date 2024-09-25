# 型のミスマッチが起こすバグの例


def add_one():
    """引数に1を足して返すだけの関数"""
    pass  # ここにコードを書きます


# リストの中身が全てint型であることを確認する関数
def is_int_list(lst: list[any]) -> bool:
    for item in lst:
        if not isinstance(item, int):
            return False
    return True


if __name__ == "__main__":
    pass  # ここにadd_one()を呼び出すコードを書く
