#Write a while loop that computes the sum of all numbers between 0 and
#mysteryValue (excluding bounds). Then print the result. "Excluding
#bounds" means that if mysteryValue is 4, you should find the sum of
#1, 2, and 3.
#
#Hint: Don't forget negative numbers! It's easy to hit an infinite loop
#on this question if mysteryValue is negative.

import sys
mysteryValue = int(sys.argv[1])
print("~ testing with mysteryValue = {} ~".format(mysteryValue))

#Do not edit the above code!

#When you Run your code, we'll test it with mysteryValue = 4. When you Submit
#your code, we'll test it with some other values as well.

n = mysteryValue;
sum = 0;
while n != 0  :
	sum += n;
	if mysteryValue > 0 :
		n -= 1
	else :
		n += 1


sum -= mysteryValue;

print(sum)
