#3-4
def do_twice(func, value):
    func(value)
    func(value)

def print_twice(string):
    print(string)
    print(string)

def do_four(func, value):
    do_twice(func, value)
    do_twice(func, value)
    
#do_twice(print_twice, 'spam')
#do_four(print_twice, 'spam')

#3-5



#3-5-2
