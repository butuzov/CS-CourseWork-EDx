#We've given you a file called "top500.txt" which contains
#the name and lifetime gross revenue of the top 500
#films at the time this question was written.
#
#Each line of the given file is formatted like so:
# <name>\t<gross revenue in dollars>
#
#In other words, you should call .split("\t") to split
#the line into the movie name (the first item) and the
#gross (the second item).
#
#Unfortunately, these movies are not in order. Write a
#function called "sort_films" that accepts two parameters:
#a string of a source filename and a string of a
#destination filename. Your function should open the
#source file and sort the contents from greatest gross
#revenue to least gross revenue, and write the sorted
#contents to the destination filename. You may assume the
#source file is correctly formatted.


#Write your function here!
def sort_films( inFile, outFile ):
    with open( inFile, "r" ) as file:
        Movies = sorted([(Movie.pop(), " ".join(Movie)) for Movie in
            [line.split() for line in file]], key=lambda v:v[0], reverse=True)
        with open(outFile, "w") as fileout:
            for movie in Movies:
                print( '{} {}'.format(movie[1], movie[0]), file=fileout)


#The line of code below will test your function and put
#your results in top500result.txt. Then, it will print
#"Done!"
sort_films("top500.txt", "top500result.txt")
print("Done!")
