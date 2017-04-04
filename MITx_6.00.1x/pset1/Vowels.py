"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

"""

s = 'azcbobobegghakl' 
print( "Number of vowels: {}".format(sum([1 for char in s if char in 'aeiou'])) )
