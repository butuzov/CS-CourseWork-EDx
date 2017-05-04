from ps4 import *

Expectations = [
    ( [1961, 1962, 1963], [4.4,5.5,6.6], [1, 2] ),
    ( [1900, 1901, 1902, 1904, 2000], [32.0, 42.0, 31.3, 22.0, 33.0], [2] )
]

for expectation in Expectations:
    print( generate_models( *expectation ) )
