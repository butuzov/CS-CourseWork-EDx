#Write a for loop that finds the sum of every odd number between 0 and
#mysteryValue (excluding bounds) and prints the result. "Excluding bounds"
#means that if mysteryValue is 9, then you should add 1, 3, 5, and 7, but not
#9.
#
#Hint: There are multiple ways to do this!

import sys
mysteryValue = int(sys.argv[1])
print("~ testing with mysteryValue = {} ~".format(mysteryValue))

#Don't modify the code above!

#When you Run your code, we'll test it with mysteryValue = 9. When you Submit
#your code, we'll test it with some other values as well.

#
sum = 0;
for i in range(mysteryValue) :
	if i % 2 == 1 :
		sum += i;
print(sum)
