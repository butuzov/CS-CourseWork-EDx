#This program is supposed to print the location of the 'o'
#in each word in the list. However, line 14 generates an
#error when 'o' is not in the word. Add try/except blocks
#to print "Not found" when the word does not have an 'o'.
#However, when the current word does not have an 'o', the
#program should keep going on to the next word.
#
#You may not use any conditionals.

words = ["dog", "ago", "cat", "fog"]

#Do not edit anything above this line! Edit only the code
#below.

for word in words:
    try :
        print(word.index("o"))
    except ValueError:
        print("Not found")
