#Write a function called courseInfo that takes as input a
#list of tuples. Each tuple contains two items: the first
#item in each tuple is a student's name as a string, and the
#second item in each tuple is that student's age as an
#integer.
#
#The function should return a dictionary with two keys.
#The key "students" should have as its value a list of all
#the students (in other words, a list made from the first
#value of each tuple). The key "avgAge" should have its
#value a float representing the average age of all the
#students in the list (in other words, the average of all
#the second items in the tuples).
#
#For example:
#
#  courseInfo([("Jackie", 20), ("Marguerite", 21)])
#  -> {"students": ['Jackie', 'Marguerite'], "avgAge": 20.5}
#
#Hint: Concentrate first on building the list of students
#and calculating the average age. Save creating the
#dictionary for last.


#Write your function here!
def courseInfo( listOFTuples ):
    return dict( students=[ x[0] for x in listOFTuples ],
                  avgAge=sum([ x[1] for x in listOFTuples]) / len(listOFTuples)
            );

#The code below will test your function. As written, it
#should output:
#
#{"students": ['Jackie', 'Marguerite'], "avgAge": 20.5}
#
#The order of keys may differ. Note that the students in
#the list should appear in the same order as they appeared
#in the original tuples. This code is not used for grading,
#so feel free to modify it.
courseInfo([("Jackie", 20), ("Marguerite", 21)])
