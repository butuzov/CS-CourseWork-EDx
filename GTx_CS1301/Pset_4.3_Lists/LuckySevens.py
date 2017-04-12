#Write a function, called luckySevens, that takes in one
#parameter, a list of integers, and returns True if the list
#has three '7's  in a row and False if the list doesn't.
#
#For example:
#
#  luckySevens([4, 7, 8, 2, 7, 7, 7, 3, 4]) -> True
#  luckySevens([4, 7, 7, 2, 8, 3, 7, 4, 3]) -> False
#
#Hint: As soon as you find one instance of three sevens, you
#could go ahead and return True -- you only have to find it
#once for it to be True! Then, if you get to the end of the
#function and haven't returned True yet, then you might
#want to return False.


#Write your function here!
def luckySevens(listOfNumbers):
    sequence = 0;
    for i in listOfNumbers:
        if i == 7:
            sequence+=1
            if sequence == 3:
                break;
        else:
            sequence=0;

    if sequence == 3:
        return True
    return False;

#The lines below will test your code. They are not used for
#grading, so feel free to modify them. If your code works
#correctly, the output presently should be:
#True
#False
print(luckySevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(luckySevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))
