'''
	credit.py

	This is python version of credit.c

	Usage       : python3 credit.py
	Description : http://docs.cs50.net/problems/credit/credit.html
'''

import sys

def is_valid_luhn( credit_card_number ) :

	# Creating List of digits with help of
	# Comprehensions
	# http://book.pythontips.com/en/latest/comprehensions.html
	digits = [ int(i) for i in str( credit_card_number ) ]

	# And using slices creating initial value for total
	# based on a sum of all odd numbers
	# create by slice
	# [-1::-2] start from the end and moev by every two numbers
	#
	# http://stackoverflow.com/questions/509211/explain-pythons-slice-notation
	total = sum( digits[-1::-2] )

	# and for even numbers created by slice that
	# [-2::-2] take every second number from second number from the end
	for even_digit in digits[-2::-2] :
		# we using "tenary" but tuples.
		# http://book.pythontips.com/en/latest/ternary_operators.html
		total += ( even_digit * 2 , 1 + ( even_digit * 2 % 10 ) )[ even_digit * 2 > 9 ]

	return total % 10 == 0


def main():
	credit_card_number_string = input("Number: ");
	# this is development setting.


	# initial value for number representation of cc number.
	credit_card_number	= 0;

	# if its all numbers trying to convert it to int.
	if credit_card_number_string.isdigit() :
		credit_card_number = int( credit_card_number_string )

	# obtaining number from input string.
	while credit_card_number <= 0 :
		credit_card_number_string = input("Number: ");
		if credit_card_number_string.isdigit() :
			credit_card_number = int( credit_card_number_string )

	if is_valid_luhn( credit_card_number ) :

		length = len( credit_card_number_string )
		first = credit_card_number_string[0:1]
		first_two = credit_card_number_string[0:2]

		if first_two in [ "37", "34" ] and length == 15 :
			sys.exit("AMEX")
		elif first_two in [ "51", "52", "53", "54", "55" ] and length == 16 :
			sys.exit("MASTERCARD")
		elif first == "4" and ( length == 16 or length == 15 ) :
			sys.exit("VISA")

	sys.exit("INVALID")


if __name__ == '__main__':
	main()
