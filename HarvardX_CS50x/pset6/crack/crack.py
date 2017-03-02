'''
	crack.py

	This is python version of crack.c

	Usage       : python3 crack.py hash
	Alt Usage	: cat crack.txt | awk '{split($0,a,":"); print  a[2]}' | xargs -L1 python3 crack.py
	Description : http://docs.cs50.net/problems/credit/credit.html
'''

import sys, crypt, string

def genpass( password ) :
	if len(password) == length :
		if crypt.crypt(password, salt) == hash :
			sys.exit(password)
		return

	for char in pw_generate_string:
		genpass( password + char )

def main():
	if len(sys.argv) != 2 :
		sys.exit( "Usage: python3 crack.py hash" )

	hash = sys.argv[1];
	salt = hash[0:2]

	pw_generate_string = string.ascii_lowercase + string.ascii_uppercase;

	for length in range(2,5):
		genpass('')


if __name__ == '__main__':
	main()
