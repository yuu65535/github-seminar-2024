#!/usr/bin/env python3

from testcase import is_all_int

ok = [1, 2, 3]
ng = [1, "a", 3]

print(f"{is_all_int(ok)=}")

print(f"{is_all_int(ng)=}")
