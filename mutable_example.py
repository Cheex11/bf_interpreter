#!/usr/bin/env python


global_scope = dict(animal='monkey')

def setter(some_scope):
	if 'fruit' not in some_scope:
		some_scope[0] = 0
		some_scope[1] = 0
		some_scope[2] = 0
		some_scope[3] = 0
		some_scope[4] = 0
		del global_scope['animal']


print('before calling setter:', global_scope)


setter(global_scope)

print('after calling setter:', global_scope)
print(global_scope[2])
