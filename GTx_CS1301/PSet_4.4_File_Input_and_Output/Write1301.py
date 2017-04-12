#Write a function called write_1301 which will write a file
#in the format described in Coding Problem 4.4.2. The
#sample.cs1301 file has been included to refresh your
#memory. Your function should accept two arguments:
#A string of a filename to write to, and a list of tuples.
#You can assume that each tuple will have the following
#format:
#
#(int, str, int, int, float)
#
#Each tuple will represent a line in the file, and each
#item in the tuple should correspond to the
#assignment number, the assignment name, the student's
#grade, the total possible number of points, and the
#assignment weight respectively.


#Write your function here!

def write_1301( file, myGradesList ) :
    with open( file, "w") as file_handler :
        for line in myGradesList:
            print('{} {} {} {} {}'.format(line[0],line[1],line[2],line[3],line[4]),
            file = file_handler)


#The code below will test your function. It's not used
#for grading, so feel free to modify it!
tuple1 = (1, "exam_1", 80, 100, 0.6)
tuple2 = (2, "exam_2", 30, 50, 0.4)
tupleList = [tuple1, tuple2]
write_1301( "test.cs1301", tupleList)
