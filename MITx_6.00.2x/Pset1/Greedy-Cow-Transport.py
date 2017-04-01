
"""
TODO:
One way of transporting cows is to always pick the heaviest cow that will fit onto the spaceship first. This is an example of a greedy algorithm. So if there are only 2 tons of free space on your spaceship, with one cow that's 3 tons and another that's 1 ton, the 1 ton cow will get put onto the spaceship.

Implement a greedy algorithm for transporting the cows back across space in the function greedy_cow_transport. The function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

Note: Make sure not to mutate the dictionary of cows that is passed in!

Assumptions:

- The order of the list of trips does not matter. That is, [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent lists of trips.
- All the cows are between 0 and 100 tons in weight.
- All the cows have unique names.
- If multiple cows weigh the same amount, break ties arbitrarily.
- The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.


"""
cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
cargo = 10

def greedy_cow_transport( cows, cargo ):

    Trips = []
    CurrentTripIndex = 0;

    Passangers = sorted( [ (k,v) for k, v in cows.items()], \
        key=lambda x:x[1], reverse=True)

    #print(Passangers);

    while len(Passangers) != 0:

        try:
            Trips[CurrentTripIndex]
        except IndexError:
            Trips.append(dict( cargo_limit=cargo, passangers=[]))
        finally:
            BoardedPassengers = [];
            SomebodyBoarded = False

            for i, Passenger in enumerate(Passangers):
                if Passenger[1] <= Trips[CurrentTripIndex]['cargo_limit']:
                    item = Passangers.pop(i)
                    Trips[CurrentTripIndex]['passangers'].append( item[0])
                    Trips[CurrentTripIndex]['cargo_limit'] -= item[1];
                    SomebodyBoarded = True
                    break;

            # ship is full, lets add one more ship trip.
            if SomebodyBoarded == False :
                CurrentTripIndex += 1;

    return [ item.get('passangers') for item in Trips ];







if __name__ == '__main__':

    TestCases = [
        (
            {'Jesse': 6, 'Maybel': 3, 'Callie': 2, 'Maggie': 5},
            10,
            [
                ["Jesse", "Maybel"],
                ["Maggie", "Callie"]
            ]
        ),
        (
            {'Patches': 60, 'MooMoo': 85, 'Clover': 5, 'Milkshake': 75, 'Horns': 50, 'Muscles': 65, 'Lotus': 10, 'Miss Bella': 15, 'Louis': 45, 'Polaris': 20},
            100,
            [
                ['MooMoo', 'Miss Bella'],
                ['Milkshake', 'Polaris', 'Clover'],
                ['Muscles', 'Lotus'],
                ['Patches'],
                ['Horns', 'Louis']
            ]
        ),

        (
            { 'Abby': 38, 'Betsy': 65, 'Lilly': 24, 'Willow': 35, 'Buttercup': 72, 'Rose': 50, 'Dottie': 85, 'Daisy': 50, 'Patches': 12, 'Coco': 10},
            100,
            [
                ['Dottie', 'Patches'],
                ['Buttercup', 'Lilly'],
                ['Betsy', 'Willow'],
                ['Rose', 'Daisy'],
                ['Abby', 'Coco']
            ]
        ),

        (
            {'Abby': 28, 'Betsy': 39, 'Willow': 59, 'Buttercup': 11, 'Rose': 42, 'Coco': 59, 'Luna': 41, 'Starlight': 54},
            120,
            [
                ['Coco', 'Willow'],
                ['Starlight', 'Rose', 'Buttercup'],
                ['Luna', 'Betsy', 'Abby']
            ]
        ),

    ];

    for Case in TestCases:

        Trips = greedy_cow_transport( Case[0], Case[1] );

        Result_Expected = [sorted(i, key=lambda x:x) for i in Case[2]];
        Result_Actual   = [sorted(i, key=lambda x:x) for i in Trips];

        if Result_Actual == Result_Expected:
            print( f'\033[1;102;30m OK \033[0m {Trips}' )
        else :
            print( f'\033[1;101;30m Fail \033[0m {Trips}' );
