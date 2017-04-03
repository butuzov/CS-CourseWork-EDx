#Write a function called "last_n" that accepts two arguments:
#a string searchString and an integer n. The function should
#return the last n characters frm searchString. If
#searchString is shorter than n characters, then it should
#return the entire value of searchString.


#Write your function here!
def last_n(s,i):
    if len(s) < i:
        return s
    return s[len(s):len(s)-i-1:-1][::-1]

#The code below will test your function. If your function
#works correctly, this should print 789, saur, and 1.
print(last_n("123456789", 3))
print(last_n("Bulbasaur", 4))
print(last_n("1", 5))
