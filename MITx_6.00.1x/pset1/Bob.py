"""

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""


s = 'azcbobobegghakl'
needle = 'bob'
pos, n = -1, 0;

while True:
    pos = s.find(needle, pos + 1);
    if pos == -1:
        break
    else :
        n += 1

print( 'Number of times {} occurs is: {}'.format(needle, n) )
