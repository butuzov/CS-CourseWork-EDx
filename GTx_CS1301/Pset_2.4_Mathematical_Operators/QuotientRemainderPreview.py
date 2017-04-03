#In the code below, you're given part of a program that calculates
#the quotient and remainder given two numbers. Complete the code
#where indicated such that the value of quotient will be the quotient
#of divisor and dividend, and the remainder will be the remainder
#when dividing dividend by divisor.

def quotientAndRemainder(dividend, divisor):
	quotient =  int( dividend / divisor	)
	remainder = dividend % divisor
	return (quotient, remainder)

#You may modify these two variables to test your code
testDividend = 7
testDivisor = 3

#Don't modify these lines; they're used to test your code above!
(quo, rem) = quotientAndRemainder(testDividend, testDivisor)
print("The quotient is", quo)
print("The remainder is", rem)
