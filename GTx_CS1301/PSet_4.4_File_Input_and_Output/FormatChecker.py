#One of the reasons that filetypes work is that everyone
#agrees how they are structured. A ".png" file, for example,
#always contains "PNG" in the first four characters to
#assure the viewer that the file is actually a png. If these
#standards were not set, it would be hard to write programs
#that know how to open and read the file.
#
#Let’s define a new filetype called ".cs1301".
#In this file, every line should be structured like so:
#
#number assignment_name grade total weight
#
#In this file, each component will meet the following
#description:
#
# - number: an integer-like value of the assignment number
#
# - assignment_name: a string value of the assignment name
#
# - grade: an integer-like value of a student’s grade
#
# - total: an integer-like value of the total possible
#   number of points
#
# - weight: a float-like value ranging from 0 to 1
#   representing the percent of the student’s grade this
#   assignment is worth. All the weights should add up to 1.
#
#Each component should be separated with exactly one space.
#A good sample file is available to view as
#"sample.cs1301".
#
#Write a function called format_checker that accepts a
#filename and returns True if the file contents accurately
#conform to the described format. Otherwise the function
#should return False. In other words, it should return True
#if:
#
# - Each line has five elements separated by spaces, AND
# - The first, third, and fourth elements are integers, AND
# - The fifth element is a decimal number, AND
# - All the fifth elements add to 1.
#
#You can make changes to test.cs1301 to test your function,
#or test it with sample.cs1301. Right now, running it on
#sample.cs1301 should return True, and on test.cs1301
#should return False.
#
#Hint 1: .split() will likely help separate each line into
#its components.
#Hint 2: .split() returns a list. So, if you were to do
#something like say splitLine = line.split(), then
#splitLine[0] would give the first item, splitLine[1] would
#give the second item, etc.
#Hint 3: Remember, the moment you find a single place where
#the file doesn't conform to the structure, then you can
#return False. Then, if you reach the end of the file, then
#it must be correct and you should return True.


# Write your function here!
def format_checker( file ):

    total_value = 0.0

    with open(file, "r") as f:
        data = f.read()
        for line in data.split('\n'):

            myLineList = line.split(" ")

            if len(myLineList) != 5:
                return False;
            else:
                number, assignment, grade, total, weight = myLineList

            # checking ints
            # if sum more than 0 - then its not valid.
            if sum([ sum( [0 if d.isdigit() else 1 for d in number ] )
                    for number in [number, grade,  total]
                ]) > 0 :
                return False;

            # checking flaot weight value.
            try:
                if 0.0 < float(weight) > 1.0:
                    return False
                total_value += float(weight);
            except ValueError:
                return False;

    if total_value > 1.0:
        return False;

    return True;

#Test your function below. With the original values of these
#files, these should print True, then False:
print(format_checker("sample.cs1301"))
print(format_checker("test.cs1301"))
