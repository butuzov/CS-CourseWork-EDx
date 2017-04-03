#Recall that input from a user is always in the form of a string.
#Write a function  called "input_type" that gets user input and
#determines what kind of string the user entered.
#
#Note that because you're getting user input, you will not be able
#to run this code: the only way you can test it is to submit it.
#When you submit your code, we'll test it with some simulated
#input.
#
#  - Your function should return "integer" if the string only
#    contains characters 0-9.
#  - Your function should return "float" if the string only
#    contains the numbers 0-9 and at most one period.
#  - You should return "boolean" if the user enters "True" or
#    "False".
#  - Otherwise, you should return "string".
#
#Remember, start by getting the user's input using the input()
#function.


#Write your function here!

def input_type(*args):
    s = args[0]
    if s == 'True' or s == 'False':
        return 'boolean';

    try :
        if str( float( s ) ) == s:
            return 'float'

        if str( int( s ) ) == s:
            return 'integer'

    except ValueError:
        return 'string'

    return 'string'
