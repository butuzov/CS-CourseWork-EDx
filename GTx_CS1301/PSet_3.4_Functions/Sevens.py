#Write a function called luckySevens() that takes in one
#parameter, a string variable named aStr. Your function
#should return True if there are exactly three '7's in aStr.
#If there are less than three  or more than three '7's, the
#function should return False.
#
#For example:
#  - luckySevens("happy777bday") should return True.
#  - luckySevens("h7app7ybd7ay") should also return True.
#  - luckySevens("happy77bday") should return False.
#  - luckySevens("h777appy777bday") should also return False.

#Write your function here!

def luckySevens( string ):
    pos = -1
    total = 0
    while True:

        if string.find( "7", pos+1) == -1:
            break

        pos = string.find("7", pos+1);

        total += 1
        if total > 3:
            return False

    return True if total == 3 else False

#You can use these lines to test your code. They are not used
#for grading, so feel free to change them.

testStringTrue = "happy777bday"
print(testStringTrue, luckySevens(testStringTrue))
testStringFalse1 = "happy77bday"
print(testStringFalse1, luckySevens(testStringFalse1))
testStringFalse2 = "h777app7y77bday"
print(testStringFalse2, luckySevens(testStringFalse2))
