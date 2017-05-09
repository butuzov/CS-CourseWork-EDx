import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    # Human OK
    bucket = [ 'red', 'red', 'red', 'red',  'green', 'green', 'green']

    # No Humans needed
    bucket_bin = [ 1 if ball == 'red' else 0 for ball in bucket ];
    results = [];

    for _ in range( numTrials + 1 ):
        random.shuffle(bucket_bin)
        sampelesize = sum(random.sample( bucket_bin, 3 ));
        results.append( 1 if (sampelesize == 3 or sampelesize == 0) else 0 )

    return  sum(results) / numTrials;


print( drawing_without_replacement_sim( 10000 ) )
