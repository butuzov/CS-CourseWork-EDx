#In Chapter 3.4, we wrote a function that calculated pressure
#given number of moles, temperature, volume, and optionally,
#a value for R. If no value was given for R, we assumed its
#value should be 0.082057.
#
#However, as written, that function could crash: what about
#when the user enters a Volume of 0? That would cause a
#ZeroDivisonError!
#
#Revise that function to catch that error. If that error
#occurs, return "Volume must be greater than 0."
#
#Feel free to copy your answer to that exercise and work
#from there. If you'd prefer to start from scratch, remember:
#you're creating a function called findPressure that returns
#a value for pressure given variables n, T, V, and optionally
#R, according to this formula:
#
# Pressure = (nRT) / V
#
#You may not use a conditional.


#Write your function here!
def findPressure(N, T, V, R=0.082057):
    try:
        return (N*R*T)/V
    except ZeroDivisionError:
        return "Volume must be greater than 0."

#You may use these lines to test your function. With the
#values initially supplied here, your function should return
#"Volume must be great than 0."
testN = 10
testT = 298
testV = 0
testR = 62.364 #Torr!
print("Result:", findPressure(testN, testT, testV, R = testR))
