#One important formula in finance and accounting is the formula for continually
#compounding interest. This formula takes as input an amount of money invested,
#an interest rate, and an amount of time (in years), and returns the value of
#the investment after that period of time.
#
#The formula, shown above, is Amount = Principal * e ^ (Rate * Time).
#
#In the code below, we have created a function called CalculateAmount. This
#function has access to three variables: Principal, Rate, and Time. Note that
#e is a constant; you may access it with math.e. Complete this function by
#completing the marked lines so that the function returns the value of an
#investment given a certain Principal, Rate, and Time.

import math

def CalculateAmount(Principal, Rate, Time):
	#If you want, you may add additional code here. Note that in the code you
	#write here, you have access to three variables: Principal, Rate, and Time.

	amount = Principal * ( math.e ** ( Rate *Time ))


	#We'll round the answer to the nearest dollar to avoid long decimals.
	return round(amount)

#You may modify the variables below to test your code above.
testPrincipal = 5000
testRate = 0.05
testTime = 5

testAmount = CalculateAmount(testPrincipal, testRate, testTime)

print("After", testTime, "years invested with a", testRate, "interest rate, a", testPrincipal, "dollar investment will be worth", testAmount, "dollars.")
