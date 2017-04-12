#Write a function called "reader" that reads in a ".cs1301"
#file described in the previous problem. The function should
#return a list of tuples representing the lines in the file like so:
#
#[(line_1_number, line_1_assignment_name, line_1_grade, line_1_total, line_1_weight),
#(line_2_number, line_2_assignment_name, line_2_grade, line_2_total, line_2_weight)]
#
#All items should be of type int except for the name (string)
#and the weight (float). You can assume the file will be in the
#proper format.
#
#Hint: Although you could use readlines() to read in all
#the lines at once, they would all be strings, not a list.
#You still need to go line-by-line and convert each string
#to a list.


#Write your function here!

def reader( file ):
    grades = [];

    with open(file, "r") as f:
        data = f.read()
        for line in data.split('\n'):

            myLineList = line.split(" ")

            if len(myLineList) == 5:
                number, assignment, grade, total, weight = myLineList
                grades.append( ( int(number), assignment, int(grade), int(total), float(weight) ) )

    return grades

#We have supplied the same sample.cs1301 from the previous
#exercise. Feel free to test your code with it to see if it
#works:
print(reader("sample.cs1301"))
