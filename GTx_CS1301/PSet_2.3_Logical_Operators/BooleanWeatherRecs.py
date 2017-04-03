#Imagine you're writing a clothing-recommendation app that makes
#suggestions based on the weather. It has booleans representing
#five different kinds of weather: hot, cold, rainy, windy, snowy.
#
#The app has four functions, one for each of four kinds of clothing:
#
# - recommendJacket, which is true if it's either cold or windy.
# - recommendBoots, which is true if it's cold and snowy.
# - recommendFlipFlops, which is true if it's hot, unless it's rainy.
# - recommendTShirt, which is true if it's hot, unless it's rainy or windy.
#
#These four functions are provided below. Complete the designated lines
#so that the booleans receive the right values according to the directions
#above.

def recommendJacket(hot, cold, rainy, windy, snowy):
	result = cold or windy
	return result

def recommendBoots(hot, cold, rainy, windy, snowy):
	result = cold and snowy
	return result

def recommendFlipFlops(hot, cold, rainy, windy, snowy):
	result = hot and not rainy
	return result

def recommendTShirt(hot, cold, rainy, windy, snowy):
	result = hot and not ( rainy or windy )
	return result

#You can modify the variables below to test out your code.
testHot = True
testCold = False
testRainy = True
testWindy = True
testSnowy = False
print("Recommend Jacket:", recommendJacket(testHot, testCold, testRainy, testWindy, testSnowy))
print("Recommend Boots:", recommendBoots(testHot, testCold, testRainy, testWindy, testSnowy))
print("Recommend Flip Flops:", recommendFlipFlops(testHot, testCold, testRainy, testWindy, testSnowy))
print("Recommend T-Shirt:", recommendTShirt(testHot, testCold, testRainy, testWindy, testSnowy))
