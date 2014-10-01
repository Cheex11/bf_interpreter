

in_global_scope = 0

def setter(in_global_scope):
    in_global_scope = in_global_scope + 1
    print('in setter function:', in_global_scope)

print('in main code:', in_global_scope)

setter(in_global_scope)

print('in main code after call to setter:', in_global_scope)


def setter2():
    global in_global_scope
    in_global_scope = in_global_scope + 1
    print('in setter2 function:', in_global_scope)

setter2()


print('in main code after call to setter 2:', in_global_scope)

#the reason why you cannot change the value of the integer variable you are passing in to your functions
# is because integers are immutable.   We were able to get it to stick by specifying the variable as global
# on line 18
