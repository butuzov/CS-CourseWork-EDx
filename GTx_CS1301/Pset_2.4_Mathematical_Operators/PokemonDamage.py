#In the Pokemon game franchise, damage is calculated using this formula:
#https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@DamageCalc.png
#
#In that formula, the variable Modifier is calculated using this formula:
#https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@ModifierCalc.png
#
#In the code below, we have defined two functions: CalculateDamage and CalculateModifier.
#
#CalculateModifier has access to four variables: STAB, Type, Critical, Other, and Random.
#You don't need to worry about what these variables represent: all you need to know is
#that each of these variables will be a floating point number.
#
#CalculateDamage has access to five variables: Level, Attack, Defense, Base, and Modifier.
#You don't need to worry about what these variables represent: all you need to know is
#that each of these variables will be either a floating point number or an integer.
#You should also note that the value of Modifier will be whatever is calculated by your
#answer to CalculateModifier.
#
#Complete the two functions such that damage is correct calculated. You can complete this
#by only modifying the indicated lines, but you are free to add more code before those
#lines if you'd like.

def CalculateModifier(STAB, Type, Critical, Other, Random):
	#You may add code here to separate your calculations into multiple lines if you'd like.
	#Make sure to keep any code you add here at this level of indentation.

	modifier = STAB * Type * Critical * Other * Random

	return modifier

def CalculateDamage(Level, Attack, Defense, Base, Modifier):
	#You may add code here to separate your calculations into multiple lines if you'd like.
	#Make sure to keep any code you add here at this level of indentation.
	#
	#HINT: You don't have to calculate the answer all on one line! You can calculate each
	#little part of the answer separately, then put them together.

	damage = ( ( ( 2 * Level + 10 ) / 250 ) * ( Attack / Defense ) * Base + 2 ) * Modifier

	#TIP: In Pokemon, damage is always an integer. So, we apply the round() function to
	#the result to get the final answer.
	return round(damage)


#You may change the values of the variables shown below to test out your code!
testSTAB = 1
testType = 0.25
testCritical = 2
testOther = 1
testRandom = 1

testLevel = 50
testAttack = 125
testDefense = 110
testBase = 60

testModifier = CalculateModifier(testSTAB, testType, testCritical, testOther, testRandom)
testDamage = CalculateDamage(testLevel, testAttack, testDefense, testBase, testModifier)
print("Modifier:", testModifier)
print("Damage:", testDamage)
