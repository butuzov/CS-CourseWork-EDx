#Write a function called modifyDict. modifyDict takes one
#parameter, a dictionary. The dictionary's keys are people's
#last names, and the dictionary's values are people's first
#names. For example, the key "Joyner" would have the value
#"David".
#
#modifyDict should delete any key-value pair for which the
#key's first letter is not capitalized. For example, the
#key-value pair "joyner"-"David" would be deleted, but the
#key-value pair "Joyner"-"david" would not be deleted. Then,
#return the modified dictionary.
#
#Remember, the keyword del deletes items from lists and
#dictionaries. For example, to remove the key "key!" from
#the dictionary myDict, you would write: del myDict["key!"]
#Or, if the key was the variable myKey, you would write:
#del myDict[myKey]
#
#Hint: If you try to delete items from the dictionary while
#looping through the dictionary, you'll run into problems!
#We should never change the number if items in a list or
#dictionary while looping through those items. Think about
#what you could do to keep track of which keys should be
#deleted so you can delete them after the loop is done.
#
#Hint 2: To check if the first letter of a string is a
#capital letter, use string[0].isupper().


#Write your function here!
def modifyDict( myDict ):
    deleteDict = [];
    for key, item in myDict.items():
        if not key[0].isupper():
            deleteDict.append( key )

    for key in deleteDict:
        del myDict[key];

    return myDict

#The code below will test your function. If your function
#works correctly, it should output:
#  {'Diaddigo':'Joshua', 'Elliott':'jackie'}
#It is not used for grading, so feel free to modify it.
myDict = {'Joshua':'Diaddigo', 'joyner':'David', 'Elliott':'jackie', 'murrell':'marguerite'}
print(modifyDict(myDict))
