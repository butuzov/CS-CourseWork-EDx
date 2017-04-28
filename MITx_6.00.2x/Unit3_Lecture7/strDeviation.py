def strDeviation(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    sample_Size = len(L)

    if sample_Size == 0:
        return float('NaN')

    mean = sum( L) / sample_Size

    return (
        sum(
            [ ( number - mean ) ** 2 for number in L ]
        ) / sample_Size
    ) ** .5, sum( L) / sample_Size

stdDev , mean = strDeviation( [0.1, 0.1, 0.1] )

print( stdDev , mean )
print( stdDev / mean )
