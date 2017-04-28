import random;

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    bucket = [ 'red', 'red', 'red', 'green', 'green', 'green']
    bucket_bin = [ 1 if ball == 'red' else 0 for ball in bucket ];
    results = [];

    for i in range(numTrials+1):

        random.shuffle(bucket_bin)
        sampelesize = sum(random.sample( bucket_bin, 3 ));
        results.append( 1 if (sampelesize == 3 or sampelesize == 0) else 0 )


    return sum(results) / len(results);

print( noReplacementSimulation( 100000 ) )
