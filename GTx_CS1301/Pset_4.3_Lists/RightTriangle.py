#Write a function called solveRightTriangle. The function
#solveRightTriangle should have three parameters: opposite,
#adjacent, and useDegrees. opposite and adjacent will be
#floats, and useDegrees will be a boolean. useDegrees
#should be a keyword parameter, and it should have a
#default value of False.
#
#The function should return a tuple containing the
#hypotenuse and angle of the right triangle (in that order).
#If useDegrees is False, the angle should be in radians. If
#useDegrees is True, the angle should be in degrees.
#
#Remember, the formula for the hypotenuse of a right
#triangle is the square root of the sum of the squared side
#lengths. You can find arctan using math.atan(), passing in
#the quotient of the opposite and adjacent as the argument.
#By default, math.atan() returns the angle in radians; you
#can pass that angle as an argument into the math.degrees()
#method to convert it to degrees.


import math

#Write your function here!
def solveRightTriangle(opposite, adjacent, useDegrees=False):
    hypotenuse = ( opposite**2 + adjacent**2 ) ** 0.5
    atan = math.atan( opposite / adjacent)
    return (hypotenuse, math.degrees(atan) if useDegrees is True  else atan )

#The lines below will test your code. They are not used for
#grading, so feel free to modify them. If your code works
#correctly, the output presently should be approximately:
#(5.0, 0.6435).
#
#Don't worry if your output doesn't match this exactly;
#Python has some small idiosyncrasies that slightly alter
#how long decimals appear, but these idiosyncrasies are
#consistent and will occur in our grading code the same
#way as in your code.
print(solveRightTriangle(3.0, 4.0))
