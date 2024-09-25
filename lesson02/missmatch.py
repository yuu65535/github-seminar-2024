# 型のミスマッチが起こすバグの例


def add_one(x: int) -> int:
    """引数に1を足して返すだけの関数"""
    return x + 1


# リストの中身が全てint型であることを確認する関数
def is_int_list(lst: list[any]) -> bool:
    for item in lst:
        if not isinstance(item, int):
            return False
    return True


if __name__ == "__main__":
    pass  # ここにadd_one()を呼び出すコードを書く
