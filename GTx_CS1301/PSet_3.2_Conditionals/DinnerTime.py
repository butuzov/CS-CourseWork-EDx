#We've created a function called dinnerTime(). This functions takes in an
#integer variable that corresponds to a panda's hunger level and returns out
#how much bamboo the panda should eat based on its hunger level.
#
#Complete the commented parts of the code so it sets the bamboo variable the
#correct number of bamboo stalks to feed the panda:
#
# Hunger Level: 1-3				# Stalks of Bamboo: 4
# Hunger Level: 4-7				# Stalks of Bamboo: 8
# Hunger Level: 8 or more		# Stalks of Bamboo: 12

#Don't worry about negative numbers.

#Function dinnerTime(hungerLevel)
#Takes as input one integer: hungerLevel.
#Returns the number of stalks of bamboo to feed your panda.
def dinnerTime(hungerLevel):
	bamboo = 0

	#Add your code here. When your code is done running, the variable bamboo
	#should have a value according to the logic described above.
	if hungerLevel >= 8 :
		bamboo = 12
	elif hungerLevel >= 4 and hungerLevel <= 7 :
		bamboo = 8
	elif hungerLevel >= 1 and hungerLevel <= 3 :
		bamboo = 4

	return bamboo


#You may modify the values below to test your code
testHunger = 3
print("Result:", dinnerTime(testHunger))
