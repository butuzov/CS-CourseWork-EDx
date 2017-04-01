#From codereview.stackexchange.com
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

"""
Finds the allocation of cows that minimizes the number of spaceship trips
via brute force.  The brute force algorithm should follow the following method:

1. Enumerate all possible ways that the cows can be divided into separate trips
2. Select the allocation that minimizes the number of trips without making any trip that does not obey the weight limitation

Does not mutate the given dictionary of cows.

Parameters:
cows  - a dictionary of name (string), weight (int) pairs
limit - weight limit of the spaceship (an int)

Returns:
A list of lists, with each inner list containing the names of cows
transported on a particular trip and the overall list containing all the
trips
"""

def brute_force_cow_transport( cows, cargo ):
    Trips = []
    CurrentTripIndex = 0;

    Passangers = sorted( [ (k,v) for k, v in cows.items()], \
        key=lambda x:x[1], reverse=True)

    def validCargo( SetOfPassengers ):
        return cargo >= max([sum([item[1] for item in block]) for block in SetOfPassengers]);

    Variations = [I for I in get_partitions(Passangers) if validCargo(I)]

    MinTrips = len(cows)

    for Variation in Variations:
        # count number of trips.
        TripsNumber = sum([1 for Passengers in Variation]);
        MinTrips = MinTrips if MinTrips <= TripsNumber else TripsNumber;

        passengers = [ [item[0] for item in items ] for items in Variation];
        rank = [ sum( [item[1] for item in items] ) for items in Variation];

        Trips.append( dict( total=TripsNumber, passengers=passengers, rank=rank ) )

    # Filter all Items that are bigger than minimum trips number,
    Trips = [item for item in Trips  if item.get('total', None) == MinTrips ]
    Trips = sorted(Trips, key = lambda x: x.get('rank'), reverse=True )

    return Trips[0].get('passengers');




if __name__ == '__main__':

    TestCases = [
        (
            {'Jesse': 6, 'Maybel': 3, 'Callie': 2, 'Maggie': 5},
            10,
            [
                ['Maybel', 'Maggie', 'Callie'],
                ['Jesse']
            ]
        ),

        (
            {'Milkshake': 40, 'Lotus': 40, 'Miss Bella': 25, 'MooMoo': 50, 'Boo': 20, 'Horns': 25},
            100,
            [
                ['Lotus', 'Milkshake', 'Boo'],
                ['MooMoo', 'Miss Bella', 'Horns']
            ]
        ),

        (
            {'Buttercup': 72, 'Daisy': 50, 'Betsy': 65},
            75,
            [
                ['Daisy'], ['Betsy'], ['Buttercup']
            ]
        ),

        (
            {'Luna': 41, 'Buttercup': 11, 'Betsy': 39, 'Starlight': 54},
            145,
            [
                ['Betsy', 'Starlight', 'Buttercup', 'Luna']
            ]
        ),

    ];

    for Case in TestCases:

        Trips = brute_force_cow_transport( Case[0], Case[1] );

        Result_Expected = [sorted(i, key=lambda x:x) for i in Case[2]];
        Result_Actual   = [sorted(i, key=lambda x:x) for i in Trips];

        if Result_Actual == Result_Expected:
            print( f'\033[1;102;30m OK \033[0m {Trips}' )
        else :
            print( f'\033[1;101;30m Fail \033[0m {Trips}' );
