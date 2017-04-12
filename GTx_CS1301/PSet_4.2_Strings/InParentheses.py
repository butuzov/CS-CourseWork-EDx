#Write a function called "in_parentheses" that accepts a
#single argument. You can expect that the function will
#given a sentence which contains some words in parentheses.
#Your function should return the contents of the
#parentheses.

#For example:
#in_parentheses("This is a sentence (words!)") -> "words!"

#You may assume there is only one set of parentheses in the
#string. If both parentheses do not appear, return an empty
#string.


#Write your function here!
def in_parentheses(s):
    if s.find("(") == -1 or s.find(")") == -1:
        return "";

    open_p = s.find("(", 0);
    close_p = s.find(")", open_p);
    return s[open_p+1:close_p]

#You can test your function using the lines of code below.
#If your function is working, these should print "words!",
#a blank line, and then "as he is doing right now".
#Remember to comment these back out before attempting to
#submit your code, though!
print(in_parentheses("This is a sentence (words!)."))
print(in_parentheses("No parentheses here!"))
print(in_parentheses("David tends to speak in a lot of parentheticals (as he is doing right now). It tends to be quite annoying."))
