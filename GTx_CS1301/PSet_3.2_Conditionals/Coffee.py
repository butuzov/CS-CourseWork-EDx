#Atlanta is full of great coffee places. Unfortunately, great coffee places
#are usually local, and local cafes are usually expensive.

#We've started a function called coffee() for you #that helps you decide if
#you can afford your morning jolt.

#You're a responsible student with a coffee budget, and decide that certain
#conditions must be met in order to spend some of your budget.

#The following conditions are:
#	If your balance is $8 or more, you can buy coffee anywhere
#   If you have at least $6, you can buy coffee at Dunkin or Starbucks, but
#       not Octane.
#   If you have at least $2, you can buy coffee at Dunkin, but not Starbucks
#       or Octane.
#   If you have less than $2, you cannot buy coffee anywhere.

#If the right conditions are met, change result to True.
#If you can't afford your coffee today, change the result to False.


#Function coffee(balance,cafe)
#Takes as input two variables: balance (a float value) and cafe (a string -
#"Octane", "Starbucks", or "Dunkin").
#Returns result variable, which is set to True if you can afford coffee,
#and false otherwise.
def coffee(balance, cafe):

	#Add your code here. When your code is done running, there should exist a
	#variable called result with the boolean value True or False according to
	#the logic described above.
	result = False
	if balance >= 8 :
		result = True;
	elif balance >= 6 and cafe in ["Dunkin", "Starbucks"] :
		result = True
	elif balance >= 2 and cafe == "Dunkin" :
		result = True;



	return result


#You may modify the values of the variables below to test out your answer.
testBalance = 12
testCafe = "Octane"
print("Result:", coffee(testBalance, testCafe))
