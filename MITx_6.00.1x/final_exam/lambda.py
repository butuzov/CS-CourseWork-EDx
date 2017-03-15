"""
Write a function called general_poly, that meets the specifications below.

For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because

	1∗10^3+2∗10^2+3∗10^1+4∗10^0
"""

def general_poly(L):
	"""
	L, a list of numbers (n0, n1, n2, ... nk)
	Returns a function, which when applied to a value x, returns the value
	n0 * x^k + n1 * x^(k-1) + ... nk * x^0
	"""
	L.reverse()
	return lambda x : sum([ item * (x ** key) for key, item in enumerate( L ) ])

"""
	Testing our Code
"""

Expectations = [
  ( 384,  2,  [2,4,8,16,32,64] ),
  ( 1234, 10, [1,2,3,4] )
]

for Item in Expectations:
	result = general_poly(Item[2])(Item[1])
	Message = ' general_poly({})({}) is {} '.format( Item[2], Item[1], Item[0] )

	if result == Item[0]:
		print( f'\033[1;102;30m (Test Passed) \033[0;102;30m {Message} \033[0m' )
	else:
		print( f'\033[1;101;30m (Test Failed) \033[0;101;30m {Message} \033[0m' )
