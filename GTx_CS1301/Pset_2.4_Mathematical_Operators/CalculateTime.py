#You're going on a long run, and want to calculate what time you'll be home.
#The problem is, the running app on your phone only gives you the estimated
#length of your run in minutes.
#
#We've provided the following variables you should not change:
#hour and minute below represent 3:48 on an analog clock.
#
#Using the provided variables, calculate the time you should arrive home,
#if your run is estimated to take 172 minutes.

#Do not modify these two lines of code
hour = 3
minute = 48

#Add your code here!
hour = hour + ( 172 // 60) + ( ( minute + 172 % 60 ) // 60 )
minute = (minute + 172 % 60) % 60;

#Feel free to create any temporary variables you need for the math, but by the
#end, change the hour and minute variables to reflect the overall change
#In other words, if you leave at 3:48, then at the end of your code,
#the value of hour and minute should be the hour and minute when you will arrive
#home after a 172 minute run.




#Do not modify the code below this line
print("Expected to arrive home at " + str(hour) + ":" + str(minute))
