#In the previous coding problem, you created a function
#called hideAndSeek that printed the numbers from 1 to 10.
#Now, however, we want to extend that. What if we want to
#count to 20? 30?
#
#Modify your previous function so that it takes as input one
#parameter: count. Then, instead of printing the numbers from
#1 to 10, it should print the numbers from 1 to the value of
#count. Then, end with "Ready or not, here I come!"

#Write your function here!


#Write your function here!
def hideAndSeek(upper=10):
    [print(x) for x in range(1,upper+1)]
    print("Ready or not, here I come!")


#Do not modify the code below; it is used to grade your code.
hideAndSeek(36)
