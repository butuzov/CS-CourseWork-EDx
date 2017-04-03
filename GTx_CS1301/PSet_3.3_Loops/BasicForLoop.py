#Write a for loop that prints every third number from 1 to 50 (including 1
#and 50).
#
#Hint: There are multiple ways to do this! You might use the modulus
#operator, or you could use an extra input to range().

for i in range(1,50) :
	if i % 3 == 1 :
		print(i)
