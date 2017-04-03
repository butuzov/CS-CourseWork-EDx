#Write two for each loops, one nested within the other, to count how many
#times the letter "t" (not case sensitive) occurs in the given list of
#strings. Print the resulting number.

#Additionally, print the current string every time a "t" (again, not case
#sensitive) is found.

givenStrings = ["Taylor Swift", "Twenty Two", "Georgia Tech"]

#Do not edit the code above this line.
#Write your code here!
counter = 0;
for word in givenStrings :
    for char in word:
        if "T" == char or "t" == char :
            print(word);
            counter += 1;
print(counter)
