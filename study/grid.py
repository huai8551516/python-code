"""
grid.py
2x2打印
+----+----+----+----+
|         |         |
|         |         |
|         |         |
|         |         |
+----+----+----+----+
|         |         |
|         |         |
|         |         |
|         |         |
+----+----+----+----+
"""

def do_twice(func):
    func()
    func()
    
def do_four(func):
    do_twice(func)
    do_twice(func)
    
def print_duanhang():
    print('+----',end='')

def print_shu4space():
    print('|    ', end='')

def print_row1():
    do_four(print_duanhang)
    print('+')

def print_row2():
    do_four(print_shu4space)
    print('|')

def print_row3():
    print_row1()
    do_four(print_row2)

def grid():
    do_four(print_row3)
    print_row1()
    
grid()
    
