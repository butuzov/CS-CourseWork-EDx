from die import *


print( getAverage( Die( [ 1 ] ), 10, 1000) )
print( getAverage( Die( [ 1, 1 ] ), 10, 1000) )
print( getAverage( Die( [ 1, 2, 3, 4, 5, 6]), 50, 1000) )
print( getAverage( Die( [ 1, 2, 3, 4, 5, 6, 6, 6, 7]), 50,  1000) )
print( getAverage( Die( [ 1, 2, 3, 4, 5, 6, 6, 6, 7]), 1,   1000) )
print( getAverage( Die( [ 1, 2, 3, 4, 5, 6, 6, 6, 7]), 500, 10000) )
