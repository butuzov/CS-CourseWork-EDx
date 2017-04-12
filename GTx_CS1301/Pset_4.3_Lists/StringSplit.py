#Write a function called stringSplitter tat replicates the
#function of the string type's split() method, assuming that
#we're splitting at spaces. stringSplitter should take as
#input a string, and return as output a list of the
#individual words from the string, assuming that words were
#divided by spaces. The spaces themselves should not be in
#the list that your function returns.
#
#You may assume that the input will have no punctuation,
#and that there will never be more than one space in a row.
#
#You may not use Python's built-in split() method.
#
#For example:
#
#  stringSplitter("Hello world") -> ['Hello', 'world']



#Write your function here!
def stringSplitter(s):
    words = []
    word = ""

    for i in s:
        if i == " ":
            words.append(word)
            word =""
        else:
        	word +=i

    words.append(word)

    return words

#The lines below will test your code. They are not used for
#grading, so feel free to modify them. If your code works
#correctly, the output presently should be:
#['Hello', 'world']
print(stringSplitter("Hello world"))
