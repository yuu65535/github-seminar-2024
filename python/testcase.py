# リストの要素が全て整数値であることを判定する

def is_all_int(item: list[any]) -> bool:
    """リストの要素が全てint型かどうかを判定する

    >>> is_all_int([1, 2, 3])
    True
    >>> is_all_int([1, "a", 3])
    False
    """

if __name__ == "__main__":
    import doctest
    print("testing")
    doctest.testmod()

