#Last exercise, you wrote a function called wordCount that
#counted the number of words in a string essentially by
#counting the spaces. However, if there were multiple spaces
#in a row, it would incorrectly add additional words. For
#example, it would have counted the string "Hi   David" as
#4 words instead of 2 because there are two additional
#spaces.
#
#Revise your wordCount method so that if it encounters
#multiple consecutive spaces, it does *not* count an
#additional word. For example, these three strings should
#all be counted as having two words:
#
# "Hi David"
# "Hi   David"
# "Hi                 David"
#
#Other than ignoring consecutive spaces, the directions are
#the same: write a function called wordCount that returns an
#integer representing the number of words in the string, or
#return "Not a string" if the input isn't a string. You may
#assume that if the input is a string, it starts with a
#letter word instead of a space.

#Write your function here!
def wordCount ( string ):
    try :
        if type(string) != str:
            raise TypeError
        return len([x for x in string.split(" ") if x.strip() != ""])
    except TypeError:
        return "Not a string"


#You may test your function here. When your function works
#correctly, these lines should output:
#Word Count: 4
#Word Count: 2
#Word Count: Not a string
#Word Count: Not a string
#Word Count: Not a string

print("Word Count:", wordCount("Four words are here!"))
print("Word Count:", wordCount("Hi   David"))
print("Word Count:", wordCount(5))
print("Word Count:", wordCount(5.1))
print("Word Count:", wordCount(True))
