#Write a function called attendanceCheck. attendanceCheck
#should have two parameters: roster and present. Both roster
#and present will be lists of strings. Return a list of all
#strings in the list roster that are not in the list
#present. In other words, if roster is a list of students
#enrolled in a class and present is a list of students in
#class today, return a list of students that are absent.
#
#You may assume that every item in each list will be a
#string. You may also assume that every name in the list
#present will be in the list roster. If no students are
#absent, return an empty list.


#Write your function here!
def attendanceCheck(l1, l2):
    return [x for x in l1 if x not in l2]


#The lines below will test your code. They are not used for
#grading, so feel free to modify them. If your code works
#correctly, the output presently should be:
#['Ferguson', 'Winston']
testRoster = ['Jessica', 'Nick', 'Winston', 'Schmidt', 'Cece', 'Ferguson']
testPresent = ['Nick', 'Cece', 'Schmidt', 'Jessica']
print(attendanceCheck(testRoster, testPresent))
