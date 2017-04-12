#Do not change the line of code below. It's at the top of
#the file to ensure that it runs before any of your code.
#You will be able to access frenchDict from inside your
#function.
frenchDict = {"me":"moi","hello":"bonjour","goodbye":"au revoir","cat":"chat","dog":"chien"}

#Write a function called french2eng that takes in one string
#parameter called sentence. french2eng should look at each
#word in the sentence and translate it into French if it is
#found in the dictionary, frenchDict. If a word is not found
#in the dictionary, do not translate it: use the original
#word. Then, the function should return a string of the
#translated sentence.
#
#You may assume that the sentence you're translating has no
#punctuation. However, you should convert it to lower case
#before translating.
#
#For example:
#
#  french2end("Hello it's me") -> "bonjour it's moi"
#
#Hint: Use .split() to get a list of strings representing
#each word in the string, then use ' '.join to merge the
#translated list back into one string. Remember, lists are
#mutable, so we can change individual items in the list.
#We write lines like myWords[1] = newWord.
#
#Hint 2: Note that to change the value of an item in the
#list, you need to change the value by its index. For
#example:
#
#Hint 3: If you're stuck, try breaking it down into small
#parts. How do you access an item from a list? How do you
#look up a key in a dictionary? How do you change the
#value of an item in a list? How do you check if a key is
#in the dictionary?


#Write your function here!
def french2eng( string ):
    return ' '.join([ frenchDict.get( word.lower() ) if frenchDict.get( word.lower(), None ) != None else word for word in string.split(" ") ])

#The code below will test your function. It isn't used
#for grading, so feel free to change it. As written
#originally, it should print: bonjour it's moi
print(french2eng("Hello it's me"))
