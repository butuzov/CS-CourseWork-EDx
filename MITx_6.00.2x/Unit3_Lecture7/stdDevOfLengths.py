def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    Sample_Size = len(L)

    if Sample_Size == 0:
        return float('NaN')

    mean = sum( [ len(word) for word in L ] ) / Sample_Size
    return (
        sum(
            [ ( len(word) - mean ) ** 2 for word in L ]
        ) / Sample_Size
    ) ** .5


Expectations = [
    ( [''], 0.0 ),
    ( [], float('NaN') ),
    ( ['a', 'z', 'p'], 0.0 ),
    ( ['apples', 'oranges', 'kiwis', 'pineapples'], 1.8708286933869707 ),
    ( ['vqxbasdyil', 'wedbm', 'kwu'], 2.943920288775949 ),
    ( ['apples', 'oranges', 'kiwis', 'pineapples'], 1.8708286933869707 ),
    ( ['ktrbri', 'ksd', 'elxvcdtjhwrnmm', 'kwqvqwvwqpnqfu', 'adplwab', 'iwgnxr'], 4.189935029992179 )
]

for Test in Expectations:
    Result = stdDevOfLengths( Test[0] );

    Message = f'Testing ({Test[0]}) : Results  Expected({Test[1]}) and Actual({Result})'
    if  Test[1] == Result  :
        print( f'\033[1;102;30m OK \033[0;102;30m {Message} \033[0m' )
    else :
        print( f'\033[1;101;30m Fail \033[0;101;30m {Message} \033[0m' )
