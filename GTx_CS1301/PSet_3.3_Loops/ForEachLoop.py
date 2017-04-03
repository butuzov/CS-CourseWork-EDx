#This one is tricky! Think carefully about for-each loops, conditionals, and
#strings. How can you track what character you're currently looking for?

#Write a for each loop that counts how many times the word "cat" occurs in
#mysteryString. Print the result.

import sys
mysteryString = sys.argv[1]
print("~ testing with mysteryValue = \"{}\" ~".format(mysteryString))

#Don't modify the code above!

#When you run your code, we'll test it with the string "my cat your cat".
#When you Submit your code, we'll test it with some other strings, too.

match = "";
count = 0;
found = False;

for i in mysteryString :
	if found == False and i == "c":
		found = True
		match = i;
	elif found == True and match == "c" and i == "a" :
		match += i;
	elif found == True and match == "ca" and i == "t" :
		match = "";
		found = False;
		count += 1;
	else :
		found = False;
		match = "";

print(count);
