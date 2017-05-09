import random
import pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist( values, numBins, histtype="barstacked", align="mid" );

    if title is not None:
        pylab.title( title )

    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()


# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls

      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      ------------------------------------------------------------------------
      - Returns the mean calculated
    """
    Trials=[]
    while numTrials:
        number_previous = -1;
        longestRun = 0;
        currentRun = 0;

        for number in [ die.roll() for _ in range(numRolls) ]:

            if number == number_previous:
                currentRun += 1;
            else:
                if currentRun > longestRun:
                    longestRun = currentRun

                number_previous = number
                currentRun = 1;

        Trials.append(longestRun);
        numTrials -= 1;

    makeHistogram( Trials, 10,  'Longest Run', 'Frequency of Occurance',
                                    'Distribution of consecutive dice rolls' )

    return round( sum( Trials ) / len( Trials ), 3)
