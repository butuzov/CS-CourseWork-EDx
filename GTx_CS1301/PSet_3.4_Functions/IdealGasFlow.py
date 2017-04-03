#In chemistry, the ideal gas law states:
#
# pressure * volume = # of moles * gas constant * temperature
#
#This is usually abbreviated to:
#
# PV = nRT
#
#We can solve this for any of these five variables, but let's
#solve it for Pressure. In terms of Pressure, the ideal gas
#law states:
#
# P = (nRT) / V
#
#Write a function called findPressure that takes as input
#three variables: number of moles, temperature, and volume.
#You can call these variables in the function whatever you
#want, but they must be specified in that order: moles, then
#temperature, then volume. You should assume all three are
#floats. Then, return as output your calculation for
#pressure. For the gas constant, you should use the value
#0.082057.

#Write your function here!
def findPressure(N, T, V):
    R = 0.082057;

    return (N*R*T)/V

#You may use these lines to test your function. With the
#values initially supplied here, you should get a value of
#roughly 48.9.
testN = 10
testT = 298
testV = 5
print("Result:", findPressure(testN, testT, testV))
