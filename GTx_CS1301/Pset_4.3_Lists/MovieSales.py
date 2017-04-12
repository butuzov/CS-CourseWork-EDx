#Write a function called findMaxSales. findMaxSales will
#have one parameter: a list of tuples. Each tuple in the
#list will have two items: a string and an integer. The
#string will represent the name of a movie, and the integer
#will represent that movie's total ticket sales (in millions
#of dollars).
#
#The function should return the movie from the list that
#had the most sales. Return only the movie name, not the
#full tuple.


#Write your function here!
def findMaxSales(tuplesList):
    maximum = ('',0)
    for movie in tuplesList:
        if movie[1] > maximum[1]:
            maximum = movie;
    return maximum[0]

#The lines below will test your code. They are not used for
#grading, so feel free to modify them. If your code works
#correctly, the output presently should be: Rogue One.
movieList = [("Finding Dory", 486), ("Captain America: Civil War", 408), ("Deadpool", 363), ("Zootopia", 341), ("Rogue One", 529), ("The Secret Life of Pets", 368), ("Batman v Superman", 330), ("Sing", 268), ("Suicide Squad", 325), ("The Jungle Book", 364)]


print(findMaxSales(movieList))
