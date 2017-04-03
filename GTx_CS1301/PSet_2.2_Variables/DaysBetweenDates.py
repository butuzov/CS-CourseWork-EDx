#In the code below, we've created two dates. Complete this
#code so that it prints the number of days that have passed
#between the two dates. It's safe to assume both dates will
#have the same month and year, so you need only access the
#days themselves.

from datetime import date
earlierDate = date(2017, 6, 15)
laterDate = date(2017, 6, 29)

#Do not modify the code above!

daysBetweenDates = int(laterDate.day) - int(earlierDate.day)

#Calculate and print the number of days that have passed between earlierDate and laterDate.
#Set the result equal to a variable named daysBetweenDates.

#Do not modify the code below!
print("There are", daysBetweenDates, "days between", earlierDate, "and", laterDate)
