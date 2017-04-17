"""
    You are given a list of unique positive integers L sorted in descending order and a positive integer sum s. The list has n elements. Consider writing a program that finds values for multipliers m0,m1,...,mn−1 such that the following equation holds:

    `s=L[0]∗m0+L[1]∗m1+...+L[n−1]∗mn−1`

    Assume a greedy approach to this problem. You calculate the integer multipliers m_0, m_1, ..., m_(n-1) by finding the largest multiplier possible for the largest value in the list, then for the second largest, and so on. Write a function that returns the sum of the multipliers using this greedy approach. If the greedy approach does not yield a set of multipliers such that the equation above sums to s, return the string "no solution". Write the function implementing this greedy algorithm with the specification below:
"""
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order

        Use the greedy approach where you find the largest multiplier for
        the largest value in L then for the second largest, and so on to
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does
                not yield a set of multipliers such that the equation sums to 's'
    """

    multipliers = [];

    for number in L:
        # getting bbiggest muptiplier of s and number
        bmi = s // number;

        # descrising s by amount of muliplication of number
        # and biggest multiplier int from s
        s -= ( bmi * number)
        multipliers.append( bmi );

    if s != 0:
        return 'no solution';

    return sum(multipliers)

if __name__ == '__main__':

    testDrives = [
        ( [ ], 10, 'no solution' ),
        ( [1], 20, 20 ),
        ( [2], 5 , 'no solution' ),
        ( [11, 10, 8, 5, 1], 16, 2 ),
        ( [12, 10, 8, 5, 2], 17, 2 ),
        ( [20, 10, 4, 3, 1], 21, 2 ),
        ( [21, 10, 8, 3, 1], 11, 2 ),
        ( [30, 20, 10], 60, 2 ),
        ( [50, 25, 5], 5,  1),
        ( [101, 51, 11, 2, 1], 3000, 36 )
    ]

    for Drive in testDrives :

        Return = greedySum(Drive[0], Drive[1]);
        Message = f'return {Return} for {Drive[0]} and sum {Drive[1]}'
        if Return != Drive[2]:
            print( f'\033[1;101;30m Tests Failed \033[0;101;30m {Message} \033[0m' )
        else:
            print( f'\033[1;102;30m Tests OK \033[0;102;30m {Message} \033[0m' )
