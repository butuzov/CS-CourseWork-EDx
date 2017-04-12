#This is a challenging one! We don't expect everyone to be
#able to do it, but it's a good chance to test how far
#you've come!
#
#Write a function called stars that takes in two
#dictionaries:
#
# - movies: a dictionary where the keys are movie titles and
#   the values are the main actor/actress in the movie. For
#   example, movies["Hunger Games"] = "Jennifer Lawrence".
# - tvshows: a dictionary where the keys are TV show titles
#   and the values are the main actor/actress in that show.
#   For example, tvshows["Community"] = "Joel McHale".
#
#The function stars should return a new dictionary. The keys
#of the new dictionary should be the actors'/actresses'
#names, and the values for each key should be the list of
#shows and movies in which that actor/actress has appeared.
#
#For example:
#
# movies = {"Fences": "Viola Davis", "Hick": "Blake Lively",
#           "The Hunger Games": "Jennifer Lawrence"}
# tvshows = {"How to Get Away with Murder": "Viola Davis",
#            "Gossip Girl": "Blake Lively",
#            "The Office": "Steve Carrell"}
# stars(movies, tvshows) ->
#  {"Viola Davis": ["Fences", "How to Get Away with Murder"],
#   "Steve Carrell": ["The Office"], "Jennifer Lawrence":
#   ["The Hunger Games"], "Blake Lively": ["Hick",
#   "Gossip Girl"]}


#Write your function here!
def stars(movies, tvshows):
    stars = dict();
    for movie, star in movies.items():
        StarList = stars.get(star, list())
        StarList.append(movie)
        stars.update({ star:StarList  })

    for show, star in tvshows.items():

        StarList = stars.get(star, list())
        StarList.append(show)

        stars.update({ star: StarList })

    return stars

#Test your function below. With the given input, your function
#should print the dictionary shown in the instructions above.
#Remember, the keys may appear in a different order.
movies = {"Fences": "Viola Davis", "Hick": "Blake Lively",
           "The Hunger Games": "Jennifer Lawrence"}

tvshows = {"How to Get Away with Murder": "Viola Davis",
            "Gossip Girl": "Blake Lively",
            "The Office": "Steve Carrell"}
print(stars(movies, tvshows))
