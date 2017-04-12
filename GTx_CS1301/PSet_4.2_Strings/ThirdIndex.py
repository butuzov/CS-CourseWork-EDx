#Write function called third_index that accepts a string
#as an argument and returns just the third character of
#the string. Ifthe user inputs a string with fewer than
#3 characters, return "too short".


#Write your function here!
def third_index(s):
    if len(s) < 3:
        return 'too short'
    return s[2]

#If you want to write any test cases to test your code,
#you can write them below!
