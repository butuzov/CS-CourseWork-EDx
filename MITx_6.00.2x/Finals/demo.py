import random

def run_Coin_Flips( times ):
    return  sum([ random.randint(0,1) for _ in range( times ) ]) / times


def trials( n, function ):
    return  sum([ run_Coin_Flips( 100 )  for _ in range( n ) ]) / n



# print(trials( 100, run_Coin_Flips));
