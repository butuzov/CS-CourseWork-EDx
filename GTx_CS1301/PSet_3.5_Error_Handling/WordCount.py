#We've come a long way in this unit! You've learned about
#conditionals, loops, functions, and error handling. To end
#the unit, let's do a couple problems that tie all these
#concepts together.
#
#Write a function called wordCount. wordCount takes as input
#a string called myString, and returns as output the number
#of words in the string. For the purposes of this problem,
#you can assume that every space indicates a new word; so,
#the number of words should be one more than the number of
#spaces.
#
#Note, though, that it could be the case that a non-string
#is accidentally passed in as the argument for myString. If
#that happens, an error will arise. If such an error arises,
#you should instead return, "Not a string". Otherwise,
#return an integer representing the number of words in the
#string.

#Write your function here!
def wordCount ( string ):
    try :
        if type(string) != str:
            raise TypeError
        return len(string.split(" "))
    except TypeError:
        return "Not a string"

#You may test your function here. When your function works
#correctly, these lines should output:
#Word Count: 4
#Word Count: 1
#Word Count: 7
#Word Count: Not a string
#Word Count: Not a string
#Word Count: Not a string

print("Word Count:", wordCount("Four words are here!"))
print("Word Count:", wordCount("One."))
print("Word Count:", wordCount("There are seven words in this sentence."))
print("Word Count:", wordCount(5))
print("Word Count:", wordCount(5.1))
print("Word Count:", wordCount(True))
