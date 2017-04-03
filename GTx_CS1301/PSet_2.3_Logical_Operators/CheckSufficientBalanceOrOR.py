#In the code below, we've created a function called
#checkSufficientBalanceOrOD(). Don't worry that this syntax
#is unfamiliar! You don't have to work with the unfamiliar
#part. Just know that on the line you're writing, you'll
#have access to two floats, balance and price, and one
#boolean, overdraftProtection.
#
#Complete the commented line of code such that the variable
#'result' is:
#
# - True if overdraftProtection is true.
# - True if balance is greater than or equal to price.
# - False if both the above conditions are false.
#
#The only line you should have to edit is the line starting
#with 'result'. Edit this line so that 'result' receives a
#value corresponding to the reasoning above. You can add
#additional lines of code before it if you'd like, of
#course, but you don't have to in order to complete this
#exercise. Note that if you do add additional lines, they
#should be indented with the same number of spaces as the
#current line.

#Function checkSufficientBalanceOrOD(balance, price, overdraftProtection)
#Takes as input two floats, balance and price, and a
#boolean, overdraftProtection, and returns True if price is
#less than or equal to balance, True if overdraftProtection
#is true, or False if neither of those conditions are true.
def checkSufficientBalanceOrOD(balance, price, overdraftProtection):

	result = overdraftProtection or ( balance >= price )

	return result

#You may modify the values of the variables below to test out your answer.
testBalance = 20.0
testPrice = 19.0
testOverdraftProtection = False
print("Result:", checkSufficientBalanceOrOD(testBalance, testPrice, testOverdraftProtection))
