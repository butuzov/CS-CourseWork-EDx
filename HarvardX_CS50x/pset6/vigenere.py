'''
	vigenere.py

	Implements a Vigenère’s cipher based encryption and decryption

	Usage        : python3 vigenere.py k
	Description  : http://docs.cs50.net/problems/vigenere/vigenere.html
	github		 : https://github.com/butuzov/computer-science/tree/master/HarvardX_CS50x/pset6/vigenere.py
'''


import sys

# This is base implementation of Crypto Class.
# basically its Ceasar crypto algorithme
# 
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


# Implementation Vigenere as child class of Ceasar (Crypto) class.
class Vigenere(Crypto):

	cipher_phraze   = 'abc'
	cipher_position = 0
	cipher 		    = 0

	def __init__ (self, **kwargs):
		for k, v in kwargs.items() :
			setattr(self, k, v)

	def get_cipher(self):

		char = self.cipher_phraze[ self.cipher_position ]
		self.cipher = ord( char.lower() ) - 97

		if ( self.cipher_position + 1 ) == len( self.cipher_phraze ) :
			self.cipher_position  = 0
		else :
			self.cipher_position += 1

		return self.cipher


def main() :
	if len(sys.argv) != 2 or not sys.argv[1].isalpha():
		sys.exit("Usage: python3 vigenere.py k")

	v =  Vigenere( cipher_phraze=sys.argv[1] )
	message = input("plaintext: ")
	print( 'ciphertext: {}'.format( v.encrypt( message ) ) )


if __name__ == '__main__':
	main()
