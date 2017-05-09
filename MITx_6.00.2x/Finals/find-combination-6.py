import itertools
import numpy as np

def find_combination(Choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """

    def permutate(choices):
        for i in range(len(choices)):
            yield from itertools.permutations(choices, i+1);

    Perms = [ sorted(list(x)) for x in permutate(Choices) if sum(x) <= total ];
    Perms = sorted(Perms, key=lambda x : sum(x), reverse=True)

    Match = [];
    if len(Perms) != 0:
        Match = Perms[0]

    return np.array([1 if x in Match and Match.pop( Match.index(x) ) else 0 for x in Choices ]);


assert list( find_combination( [1, 2, 2, 3], 4) ) in ( [0, 1, 1, 0], [1, 0, 0, 1] )
assert list( find_combination( [10, 100, 1000, 3, 8, 12, 38], 1171) ) == [1, 1, 1, 1, 1, 1, 1]
assert list( find_combination( [1, 81, 3, 102, 450, 10], 9) ) == [1, 0, 1, 0, 0, 0]
assert list( find_combination( [1, 3, 4, 2, 5], 16) ) == [1, 1, 1, 1, 1]
