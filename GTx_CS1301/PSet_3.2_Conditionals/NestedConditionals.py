#We learned earlier in this chapter how conditionals can be nested. Review
#the code below and rewrite the conditionals to be nested, so that they still
#produce the same result.

#As a reminder, here are the age requirements to view movies alone:
#    "R" : 17 and up
#    "PG-13": 13 and up

#hasPermission should be set to True if
#age is above the limit for the given rating,
#otherwise it should be False.

#Assume rating and age are already defined.

hasPermission = True
if rating == "PG-13":
	if age < 13:
		hasPermission = False
elif rating == "R":
	if age < 17:
		hasPermission = False
