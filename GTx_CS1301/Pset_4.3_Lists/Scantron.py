#Write a function called gradeScantron. gradeScantron should
#take as input two lists: answers and key. Each list contain
#strings. Each string will be only one letter, a character
#from A to E. Your code should return an integer
#representing for how many indices in the lists the value of
#answers is equal to the value of key. In other words, if we
#assume that the list answers is the ordered list of answers
#to a test, and the list key is the ordered list of correct
#answers, the function should return how many answers they
#got right.
#
#If the lists do not have the same number of items, return
#-1 to indicate that the answer key did not belong to the
#same test as the student's answers.


#Write your function here!
def gradeScantron( Answers,Keys):
    if len(Answers) != len(Keys):
        return -1
    valid = 0;
    for _ in range(len(Answers)):
        if Answers[_] == Keys[_] :
            valid += 1;

    return valid;


#The lines below will test your code. They are not used for
#grading, so feel free to modify them. If your code works
#correctly, the output presently should be: 7
testAnswers = ["A", "B", "B", "A", "D", "A", "B", "A", "E"]
testKey = ["A", "B", "B", "A", "D", "E", "B", "A", "D"]
print(gradeScantron(testAnswers, testKey))
