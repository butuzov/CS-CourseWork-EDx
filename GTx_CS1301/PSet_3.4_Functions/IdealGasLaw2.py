#Last problem, we wrote a function that calculated pressure
#given number of moles, temperature, and volume. We told you
#to assume a value of 0.082057 for R. This value means that
#pressure must be given in atm.
#
#atm is the most common unit for pressure, but there are
#others: mmHg, Torr, Pa, kPa, bar, and mb, for example. what
#if pressure was sent in using one of these units? Our
#calculation would be wrong!
#
#So, we want to assume that pressure is in atm (and thus,
#that R should be 0.082057), but we want to let the person
#calling our function change that if need be. So, revise
#your findPressure function so that R is a keyword parameter.
#Its default value should be 0.082057, but the person calling
#the function can override that. The name of the parameter for
#the gas constant must be R for this to work.
#
#As a reminder, you're writing a function that calculates:
#
# P = (nRT) / V
#

#Write your function here!

#Write your function here!
def findPressure(N, T, V, R=0.082057):
    return (N*R*T)/V


#You may use these lines to test your function. With the
#values initially supplied here, you should get a value of
#roughly 48.9.
testN = 10
testT = 298
testV = 5
testR = 62.364 #Torr!
print("Result:", findPressure(testN, testT, testV, R = testR))
