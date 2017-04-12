#Python, like most languages, actually uses numbers in the
#background to represent individual characters in a string.
#For example, "a" is assigned the numeric value of 97.
#We call this the ordinal value.
#
#Write a function called "ordinal_value" that determines if
#a given string of length one has an ordinal value of
#greater than 100 and less than 200. Return the boolean
#result.
#
#Hint: you can find the ordinal value of a character using
#a built in python function like so: ord("a").
#
#Note: you may not declare any strings in your solution.


#Write your function here!
def ordinal_value(string):
    return 100 < ord(string) < 200

#Uncomment the lines below to test your code. If your code
#is correct, the first should return False, and the second
#should return True. Comment these lines back out before
#submitting your code for grading.
#print(ordinal_value("a"))
#print(ordinal_value("o"))
