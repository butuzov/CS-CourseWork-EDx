#Write a function called "angry_file_finder" that accepts a
#filename as a parameter. The function should open the file,
#read it, and return True if the file contains "!" on every
#line. Otherwise the function should return False.


#Write your function here!
def angry_file_finder( filename ):
    f = open(filename);
    for line in f:
        if "!" not in line:
            return False

    return True

#We've supplied a file called AngryFileFinderInput.txt that you
#can use to test your function. As written right now, the
#line below should print True:
print(angry_file_finder("AngryFileFinderInput.txt"))
