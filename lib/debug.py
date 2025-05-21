#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

engineering = Department.create("Engineering", "Kisumu")
print(engineering)

agric = Department.create("Agriculture", "Meru")
print(agric)


ipdb.set_trace()
