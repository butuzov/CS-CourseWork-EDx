#A year is considered a leap year if it abides by the
#following rules:
#
#  - Every 4th year IS a leap year, EXCEPT...
#  - Every 100th year is NOT a leap year, EXCEPT...
#  - Every 400th year IS a leap year.
#
#This starts at year 0. For example:
#
#  - 1993 is not a leap year because it is not a multiple of 4.
#  - 1996 is a leap year because it is a multiple of 4.
#  - 1900 is not a leap year because it is a multiple of 100,
#    even though it is a multiple of 4.
#  - 2000 is a leap year because it is a multiple of 400,
#    even though it is a multiple of 100.
#
#Write a function called isLeapYear. isLeapYear should take
#one parameter: year, an integer. It should return True if
#that year is a leap year, False if it is not.

#Write your function here!
def isLeapYear(year):
    return True if (year%4==0 and not year%100==0) or (year%400 == 0) else False


#You may use the code below to test your function. This will
#not be used for grading.
print("1993 is a leap year:", isLeapYear(1993))
print("1996 is a leap year:", isLeapYear(1996))
print("1900 is a leap year:", isLeapYear(1900))
print("2000 is a leap year:", isLeapYear(2000))
