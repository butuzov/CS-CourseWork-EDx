'''
	ceasar.py

	Implements a Cceasar’s cipher based encryption and decryption

	Usage        : python3 ceasar.py k
	Description  : http://docs.cs50.net/problems/ceasar/ceasar.html
	Github	   : https://github.com/butuzov/computer-science/tree/master/HarvardX_CS50x/pset6/ceasar.py

'''

import sys

# This is base implementation of Crypto Class.
# basically its Ceasar crypto algorithm


class Crypto(object):

	# cipher by default.
	cipher = 1

	def __init__(self, **kwargs) :
		for k,v in kwargs.items() :
			setattr(self, k, v)

	def __str__(self) :
		return 'Cypher is {}'.format( self.get_cipher() )

	def encrypt(self, string):
		encrypted_string = "";

		for char in string :
			if char.isalpha() :
				encrypted_string += self.move( char, 'encrypt')
			else :
				encrypted_string += char
		return encrypted_string


	def decrypt(self, string):
		decrypted_string = "";
		for char in string :
			if char.isalpha() :
				decrypted_string += self.move( char, 'decrypt')
			else :
				decrypted_string += char
		return decrypted_string


	def move( self, char, direction='encrypt' ) :

		cipher = self.get_cipher()
		code = ord(char)
		base = (65, 97)[ code >= 65 and 90 <= code ]

		if direction == 'decrypt' :
			## Direction Left stands for decryption.
			code = ( ( code - base - cipher ) % 26 ) + base;

		elif direction == 'encrypt':
			## Direction Left stands for encryption.
			code = ( ( code - base + cipher ) % 26 ) + base;

		else :
			pass

		return chr(code)


	def get_cipher(self):
		return self.cipher

# Implementation Ceasar as additional class.
class Ceasar(Crypto):
	pass

def main():
	if len(sys.argv) != 2 :
		sys.exit( print("Usage: python3 caesar.py k") )

	c =  Ceasar( cipher=int(sys.argv[1]) )
	message = input("plaintext: ")
	print('ciphertext: {}'.format( c.encrypt( message ) ) )

if __name__ == '__main__':
	main()
