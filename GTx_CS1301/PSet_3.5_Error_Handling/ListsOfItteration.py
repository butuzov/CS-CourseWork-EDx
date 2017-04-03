#Write a program that iterates through the items in the
#given list. For each item, you should attempt to iterate
#through the item and print each character seperately.
#
#If this fails, print "Not iterable".
#
#Hint: Although we'll cover lists more in Unit 4, all
#you need to know right now is that this syntax will run
#a loop over a list, a string, or any other iterable
#type of information:
#
#  for item in givenItems:
#
#To iterate over the items in 'item', you can do the
#same thing. Start out by building the nested for-each
#loops that you'll need, then figure out where to put
#the try-except structure.
#
#This one's tricky, but you can do it!

givenItems = ["one", "two", 3, 4, "five", ["six", "seven", "eight"]]

#Do not edit anything above this line!

for _ in givenItems:
    try :
        for _ in _ :
            print( _ )
    except TypeError:
        print ( "Not iterable" )
