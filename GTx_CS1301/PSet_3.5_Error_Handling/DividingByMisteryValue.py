#Write a program that divides mysteryValue by mysteryValue
#and print the result. If that operation results in an
#error, divide it by (mysteryValue - 5) and print the
#result. If that still fails, multiply mysteryValue by 5
#and print the result. You may assume one of those three
#things will work.
#
#You may not use any conditionals.
#
#Hint: You're going to want to test one try/except structure
#inside another! Think carefully about whether the second
#one should go inside the try block or the except block.

import sys
try:
	mysteryValue = int(sys.argv[1])
except:
    mysteryValue = sys.argv[1]
print("~ testing with mysteryValue = {} ~".format(mysteryValue))

#Do not edit anything above this line! When you click Run,
#we'll test your code with mysteryValue = 5. When you click
#Submit, we'll test it with a few other values, too.

try:
    result = mysteryValue / mysteryValue;
except ZeroDivisionError:
    result = mysteryValue / (mysteryValue - 5);
except TypeError:
    result = mysteryValue * 5;

print(result)
