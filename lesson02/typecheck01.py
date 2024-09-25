#!/usr/bin/env python3
# 注意: このファイルはいじらないでください

import typing
from missmatch import add_one

assert typing.get_type_hints(add_one)["x"] == int, "引数xの型ヒントがintではありません"
assert (
    typing.get_type_hints(add_one)["return"] == int
), "戻り値の型ヒントがintではありません"
