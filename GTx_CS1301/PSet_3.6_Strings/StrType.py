#Write a function called 'str_type' which accepts one string
#argument and determines what type of string it is.
#
#If the string is a single character, return "character".
#If the string contains a single word, return "word".
#If the String contains a whole sentence, return "sentence".
#
#You may assume a sentence is anything with more than one word
#in it, and that multiple words will always be separated by
#spaces. You may also assume the string has at least one
#character (no blank strings).


#Write your function here!
def str_type(s):
    if len(s) == 1:
        return "character"
    if s.find(" ") != -1:
        return "sentence"
    return "word";

#If you'd like to test out your code, you can add test cases
#below. You may need to remove or comment them out before
#submitting, though, as the autograder may think you're
#circumventing it.
