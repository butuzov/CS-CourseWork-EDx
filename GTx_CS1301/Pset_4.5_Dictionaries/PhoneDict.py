#Write a function called phoneBook that takes two lists as
#input:
#
# - names, a list of names as strings
# - numbers, a list of phone numbers as strings
#
#phoneBook() should take these two lists and create a
#dictionary that maps each name to its phone number. For
#example, the first name in names should become a key in
#the dictionary, and the first number in numbers should
#become the value corresponding to the first name. Then, it
#should return the dictionary that results.
#
#Hint: Because you're mapping the first name with the first
#number, the second name with the second number, etc., you do
#not need two loops. For a similar exercise, check back on
#Coding Problem 4.3.3, the Scantron grading problem.
#
#You may assume that the two lists have the same number of
#items: there will be no names without numbers or numbers
#without names.


#Write your function here!
def phoneBook(nameList, numberList):
    return { k:v for k,v in zip(nameList, numberList) }


#The code below will test your function. It is not used for
#grading, so feel free to modify it. As written initially,
#it should return this dictionary (although the order of the
#keys may vary):
#{'Jackie': '404-555-1234', 'Joshua': '678-555-5678', 'Marguerite': '770-555-9012'

nameList = ['Jackie', 'Joshua', 'Marguerite']
numberList = ['404-555-1234', '678-555-5678', '770-555-9012']
print(phoneBook(nameList, numberList))
