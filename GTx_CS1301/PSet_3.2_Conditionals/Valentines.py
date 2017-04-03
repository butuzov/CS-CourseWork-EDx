#Ever been at a loss for what to do for your S/O for Valentine's Day?
#We've started a function called chooseGift() that determines the perfect
#gift for your Valentine based on how long you've been together. Finish
#writing the function by filling in the conditionals based on the following
#criteria:

# If you've been dating for at least 4 years, give him/her a dog ("dog").
# If you've been dating for 1-4 years, give him/her a watch ("watch").
# If you've been dating for less than a year, but at least 6 months,
#    give him/her Bo Burhnam tickets ("Bo Burhnam tickets").
# If you've been dating for less than 6 months, give him/her flowers
#    ("flowers").
# If you're not actually dating, go big or go home -
#    give him/her a yacht to sail away together in ("yacht").

#Function: chooseGift(days,months,years)
#Takes three integer inputs: days, months, years
#Returns a string variable, gift, indicating what gift should be given.
#Do not modify any code already written.
def chooseGift(days, months, years):
	gift = ''
	if years == 0 and months == 0 and days == 0:
		gift = 'yacht'
	else :
		if years >= 4 :
			gift = 'dog';
		elif years >= 1 :
			gift = 'watch';
		elif months >= 6 :
			gift = "Bo Burnham tickets";
		else :
			gift = 'flowers'
	return gift

#You may change the code below to test your work
testDays = 24
testMonths = 5
testYears = 2
print(chooseGift(testDays, testMonths, testYears))
