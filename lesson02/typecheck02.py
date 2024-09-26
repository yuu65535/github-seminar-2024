#!/usr/bin/env python3
# 注意: このファイルはいじらないでください

import typing
from missmatch import is_int_list

# is_int_list()の型ヒントを確認する
assert (
    typing.get_type_hints(is_int_list)["lst"] == list[any]
), "引数lstの型ヒントがlist[any]ではありません"
# is_int_list()の戻り値がboolであることを確認する
assert (
    typing.get_type_hints(is_int_list)["return"] == bool
), "戻り値の型ヒントがboolではありません"
