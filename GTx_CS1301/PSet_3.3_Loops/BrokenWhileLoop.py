#This while loop results in an infinite loop; it does not ever stop.
#Fix it so that it counts down from 100 by 3s, stopping when it reaches 0.
#
#Hint: != means 'not equal'. So, x != 0 is the same as not x == 0.

x = 100
while x > 0:
    print(x)
    x -= 3
