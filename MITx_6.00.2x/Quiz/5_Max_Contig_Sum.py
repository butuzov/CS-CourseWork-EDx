"""
    Consider a list of positive (there is at least one positive) and negative numbers. You are asked to find the maximum sum of a contiguous subsequence. For example,

    in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11
    in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16

    One algorithm goes through all possible subsequences and compares the sums of each contiguous subsequence with the largest sum it has seen. What is the time complexity of this algorithm in terms of the length of the list, N?

    answer a. O(n^2)
    and solution for task
"""
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """

    max = 0;
    for i in range(len(L)):
        for j in range(len(L),0,-1):
            sum_of_slice = sum(L[i:j])
            if max < sum_of_slice:
                max = sum_of_slice
    return max



if __name__ == '__main__':

    testDrives = [
        ( [3, 4, -1, 5, -4], 11 ),
        ( [3, 4, -8, 15, -1, 2], 16 ),
        ( [1], 1 ),
        ( [1, -1], 1 ),
        ( [10, 9, 8, -1], 27 ),
        ( [-2, 6, 8, 10], 24 ),
        ( [5, -7, 1], 5 ),
        ( [-3, -2, 1, -1, -5], 1 ),
        ( [3, 4, -1, 5, -4], 11 ),
        ( [3, 4, -8, 15, -1, 2], 16 ),
        ( [3, 4, -8, 3, 3, 1, -7, 15, -1, 2], 16 ),
        ( [0, -2, -7, 3, 3, -7, 15, 2], 17 ),
        ( [3, -3, 3, -3], 3 ),
    ]

    for Drive in testDrives :

        Return = max_contig_sum(Drive[0]);
        Message = f'Sum of max sontif ints is {Return} for List {Drive[0]} (expected {Drive[1]})'
        if Return != Drive[1]:
            print( f'\033[1;101;30m Tests Failed \033[0;101;30m {Message} \033[0m' )
        else:
            print( f'\033[1;102;30m Tests OK \033[0;102;30m {Message} \033[0m' )
