'''
	greedy.py

	The objective of this application is  to use the greedy algorithm to display
	the least amount of coins that can be used in USD for change owed.

	Usage        : python3 greedy.py
	Description  : http://docs.cs50.net/problems/mario/more/mario.html
'''

from re import search
import sys

# Actually clone of get_float by cs50 team.
def get_float( StringOfFloat ) :
	if StringOfFloat is None or len(StringOfFloat) is 0 :
		return False
	elif search( r"^[+-]?\d*(?:\.\d*)?$", StringOfFloat ) :
		try:
			return float( StringOfFloat )
		except ValueError:
			pass
	return False

def main():
	# Initial value for coins storage. In False.
	Coins = False;

	# Getting Value from User.
	while  Coins is False or Coins <= 0.0 :
		CoinsStr = input( "O hai! How much change is owed?\n" )
		Coins = get_float( CoinsStr )

	# Bring value to Int
	Coins = int( Coins * 100 );

	# List of coins amounts.
	CoinsAmount = [ 25, 10, 5, 1 ];
	# TOtal value init value.
	TotalCoins = 0;

	# Do math.
	for coinAmount in CoinsAmount :
		TotalCoins +=  Coins // coinAmount;
		Coins %= coinAmount;
		#print(Coins, TotalCoins);

	# Print value.
	print( int( TotalCoins ) );


if __name__ == '__main__':
	main();
